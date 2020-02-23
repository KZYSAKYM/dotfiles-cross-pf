#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
from typing import *
from . import class_base
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

TypeConfig = TypeVar('{"<platform>": {"prehook": {"cmd": [str], "args": [str]}, '
                     '"main": {"cmd": [str], "args": [str]}, '
                     '"posthook": {"cmd": [str], "args": [str]}}',
                     bound=Dict[str, Dict[str, Dict[str, List[str]]]])
TypeFlow = TypeVar('{"prehook": {"cmd": [str], "args": [str]}, '
                   '"main": {"cmd": [str], "args": [str]}, '
                   '"posthook": {"cmd": [str], "args": [str]}',
                   bound=Dict[str, Dict[str, List[str]]])


class Cmd(class_base.ProjectBase):
    def __init__(self, configs: TypeConfig, workdir: str,
                 stdout=sys.stdout, stderr=sys.stderr,
                 indent=4, width=80, compact=False):
        super().__init__(stdout, stderr, indent, width, compact)
        self.configs = configs
        self.workdir = workdir if os.path.isdir(workdir) else None

    def execute(self) -> bool:
        flow: TypeFlow = self.parse()

        if 'prehook' in flow:
            self._execute('prehook', flow)

        if 'main' not in flow:
            self.print_err('Must require main key in cmd and args')
            return False
        self._execute('main', flow)

        if 'posthook' in flow:
            self._execute('posthook', flow)

        return True

    def _execute(self, part: str, flow: TypeFlow):
        self.print_out("[EXEC: %s] %s" % (
            part, ' '.join([*flow[part]['cmd'], *flow[part]['args']])))
        proc = subprocess.run(" ".join([*flow[part]['cmd'], *flow[part]['args']]),
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              cwd=self.workdir, shell=True)
        if proc.returncode != 0:
            self.print_err(
                '[ERROR: %s: %s] return with %d' % (
                    part, ' '.join([*flow[part]['cmd'], *flow[part]['args']]),
                    proc.returncode))
        self.print_out('%s' % proc.stdout.decode('utf-8'), 1)
        self.print_err('%s' % proc.stderr.decode('utf-8'), 1)

    def parse(self) -> TypeFlow:
        flow: Any = {}
        if   ((sys.platform == 'linux') and
              ('linux' in self.configs)):
            flow = self.configs['linux']
        elif ((sys.platform == 'win32') and
              ('windows' in self.configs)):
            flow = self.configs['windows']
        elif ((sys.platform == 'darwin') and
              ('mac' in self.configs)):
            flow = self.configs['mac']
        else:
            flow = self.configs

        return flow


TypeAction = TypeVar('Cmd', bound=Cmd)
