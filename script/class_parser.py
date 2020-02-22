#!/usr/bin/env python3
# -*- cording: utf-8 -*-

from typing import *
import sys
import os
import yaml
import copy
from enum import Enum
from . import class_base
from . import class_action
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

"""
Parse sh-like dotfile setup definition yaml
"""


def _split_cmd_args(cmd_args: object) -> object:
    cmd_args['prehook']['cmd'] = cmd_args['prehook']['cmd'].split()
    cmd_args['main']['cmd'] = cmd_args['main']['cmd'].split()
    cmd_args['posthook']['cmd'] = cmd_args['posthook']['cmd'].split()
    return cmd_args


class Template(class_base.ProjectBase, Enum):
    ERROR = 0
    CMD_ARGS = 1
    FLOW = 2
    VALIANT = 3


class Parser(class_base.ProjectBase):
    def __init__(self, parser_library: Any = yaml,
                 stdout=sys.stdout, stderr=sys.stderr,
                 indent=4, width=80, compact=False):
        super().__init__(stdout, stderr, indent, width, compact)
        self.parserlib = parser_library

        self.cmd_args_template = {
            'cmd': ['echo', ],
            'args': ['NaN', ],
        }
        self.flow_template = {
            'prehook': copy.deepcopy(self.cmd_args_template),
            'main': copy.deepcopy(self.cmd_args_template),
            'posthook': copy.deepcopy(self.cmd_args_template),
        }
        self.valiant_template = {
            'linux': copy.deepcopy(self.flow_template),
            'mac': copy.deepcopy(self.flow_template),
            'windows': copy.deepcopy(self.flow_template),
        }
        self.cmd_args_key_list = sorted(
            self.walk_dict(self.cmd_args_template))
        self.flow_key_list = sorted(
            self.walk_dict(self.flow_template))
        self.variant_key_list = sorted(
            self.walk_dict(self.valiant_template))

    def walk_dict(self, d: Dict) -> List[str]:
        ret: List = [
            k if not isinstance(d[k], dict) else None
            for k in d.keys()
        ]
        nest: List = [
            k if isinstance(d[k], dict) else None
            for k in d.keys()
        ]
        ret = list(filter(lambda i: i is not None, ret))
        nest = list(filter(lambda i: i is not None, nest))
        for k in nest:
            nest_ret = self.walk_dict(d[k])
            for i in nest_ret:
                ret.append('%s/%s' % (k, i))

        return ret

    def validate_config(self, validated: Dict) -> Template:
        key_list = sorted(self.walk_dict(validated))
        match_keys_simple = lambda kl1, kl2: all(
            [k1 in kl2 for k1 in kl1]
        )
        match_keys = lambda kl1, kl2: all(
            [k1 in kl2 if not (
                ('prehook' == k1.split('/')[-2]) or
                ('posthook' == k1.split('/')[-2])) else True
                for k1 in kl1]
        )
        if match_keys_simple(self.cmd_args_key_list, key_list):
            return Template.CMD_ARGS
        elif match_keys(self.flow_key_list, key_list):
            return Template.FLOW
        elif match_keys(self.variant_key_list, key_list):
            return Template.VALIANT

        return Template.ERROR

    def walk(self, dirname: str) -> None:
        """
        walk in dotfiles dirs.
        sub directories should be processed after files.
        It's because of representing dependencies

        :param dirname: dotfiles dirs
        :return: None
        """
        files = [f.name if not f.name.startswith('.') else None
                 for f in os.scandir(dirname)]
        files = list(filter(lambda x: x is not None, files))
        if sys.platform == 'win32':
            files = list(map(lambda x: dirname + '\\' + x, files))
        else:
            files = list(map(lambda x: dirname + '/' + x, files))
        dirs: list = []
        self.print_debug('walk in %s' % dirname)
        for f in files:
            if not os.path.isdir(f):
                self.process(f)
            else:
                dirs.append(f)
        for d in dirs:
            self.walk(d)

    def process(self, filename: str):
        self.print_debug('process %s' % filename, depth=0)
        configs = self.create_config(filename)
        action = self.create_action(configs, os.path.dirname(filename))
        ret = action.execute()
        if ret is not True:
            self.print_err("[ERROR] in %s with config: %s" % (filename, configs))

    @staticmethod
    def parse_cmd_args(parsed: Dict) -> class_action.TypeFlow:
        """
        - cmd_args_template:
            cmd: str
            args: str
            this should be parsed to {
                'main': {
                    'cmd': List[str],
                    'args': List[str],
                },
            }

        :param parsed: parsed dict
        :return:
        """
        ret: Dict[str, Dict[str, List[str]]] = {}
        if not ((isinstance(parsed['cmd'], str))
           and  (isinstance(parsed['args'], str))):
            raise TypeError('subentry of cmd and args should be str')
        ret['main'] = {
            'cmd': parsed['cmd'].split(),
            'args': parsed['args'].split(),
        }

        return ret

    def parse_flow(self, parsed: Dict) -> class_action.TypeFlow:
        """
        - flow_template:
            prehook:
                cmd: str
                args: str
            main:
                cmd: str
                args: str
            posthook:
                cmd: str
                args: str
            this should be parsed to {
                'prehook': {
                    'cmd': List[str],
                    'args': List[str],
                },
                'main': {
                    'cmd': List[str],
                    'args': List[str],
                },
                'posthook': {
                    'cmd': List[str],
                    'args': List[str],
                },
            }

        :param parsed:  parsed dict
        :return:
        """
        ret: Dict[str, Dict[str, List[str]]] = {}
        for key in parsed.keys():
            if key in ('prehook', 'main', 'posthook'):
                ret[key] = self.parse_cmd_args(parsed[key])['main']
            else:
                self.print_err(
                    "[WARNING] Found Invalid Key %s" % key)
        return ret

    def parse_valiant(self, parsed: Dict) -> class_action.TypeConfig:
        """
        - valiant_template:
            linux:
                prehook:
                    cmd: str
                    args: str
                main:
                    cmd: str
                    args: str
                posthook:
                    cmd: str
                    args: str
            windows:
                prehook:
                    cmd: str
                    args: str
                main:
                    cmd: str
                    args: str
                posthook:
                    cmd: str
                    args: str
            mac:
                prehook:
                    cmd: str
                    args: str
                main:
                    cmd: str
                    args: str
                posthook:
                    cmd: str
                    args: str
            this should be parsed to {
                'linux': {
                    'prehook': {
                        'cmd': List[str],
                        'args': List[str],
                    },
                    'main': {
                        'cmd': List[str],
                        'args': List[str],
                    },
                    'posthook': {
                        'cmd': List[str],
                        'args': List[str],
                    },
                },
                'windows: {
                    'prehook': {
                        'cmd': List[str],
                        'args': List[str],
                    },
                    'main': {
                        'cmd': List[str],
                        'args': List[str],
                    },
                    'posthook': {
                        'cmd': List[str],
                        'args': List[str],
                    },
                },
                'mac': {
                    'prehook': {
                        'cmd': List[str],
                        'args': List[str],
                    },
                    'main': {
                        'cmd': List[str],
                        'args': List[str],
                    },
                    'posthook': {
                        'cmd': List[str],
                        'args': List[str],
                    },
                }.
            }

        :param parsed: parsed dict
        :return:
        """
        ret: Dict[str, Dict[str, Dict[str, List[str]]]] = {}
        for key in parsed.keys():
            if key in ('linux', 'mac', 'windows'):
                ret[key] = self.parse_flow(parsed[key])
            else:
                self.print_err(
                    "[WARNING] Found Invalid Key %s" % key)
        return ret

    def create_config(self, filename: str) -> class_action.TypeConfig:
        """
        accept 3 pattern:
        - cmd_args_template
        - flow_template
        - valiant_template
        """
        config_parsed: dict = self.parse(filename)
        template_type = self.validate_config(config_parsed)
        self.print_debug('create_config %s' % filename, depth=1)
        ret: Any

        if   template_type == Template.CMD_ARGS:
            self.print_debug('%s is Template.CMD_ARGS' % filename, depth=2)
            ret = self.parse_cmd_args(config_parsed)
        elif template_type == Template.FLOW:
            self.print_debug('%s is Template.FLOW' % filename, depth=2)
            ret = self.parse_flow(config_parsed)
        elif template_type == Template.VALIANT:
            self.print_debug('%s is Template.VALIANT' % filename, depth=2)
            ret = self.parse_valiant(config_parsed)
        else:
            raise KeyError('%s does not valid format' % filename)
        self.print_debug('%s' % ret, depth=3)
        return ret

    def parse(self, filename: str) -> Dict:
        ret: dict
        with open(filename, 'r') as f:
            ret = self._parse(f)
        self.print_debug('parsed: %s' % ret, depth=2)
        return ret

    def _parse(self, fd: Any) -> Any:
        return self.parserlib.safe_load(fd)

    @staticmethod
    def create_action(configs: class_action.TypeConfig, workdir: str)\
            -> class_action.TypeAction:
        return class_action.Cmd(configs, workdir)
