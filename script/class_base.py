#!/usr/bin/env python3
# -*- cording: utf-8 -*-

import sys
import os
import pprint

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
import main


class ProjectBase:
    def __init__(self, stdout: object = sys.stdout, stderr: object = sys.stderr,
                 indent: int = 4, width: int = 80, compact: bool = False) -> object:
        self.pp = pprint.PrettyPrinter(
                indent=indent, width=width, compact=compact)
        self.stdout = stdout
        self.stderr = stderr
        self.indent = indent
        self.width = width
        self.compact = compact

    def recursive_eval(self, o: object) -> str:
        ret: object
        if pprint.isreadable(o):
            try:
                ret = self.recursive_eval(eval(o))
            except Exception:
                ret = o
        else:
            ret = o
        return o

    def print_out(self, o: object, depth: int = 0) -> None:
        o = self.recursive_eval(o)
        lines = eval(pprint.pformat(o,
                    indent=self.indent,
                    width=self.width, depth=depth + 1, compact=self.compact
                )).split('\n')
        for line in lines:
            print("%s" % line, file=self.stdout)

    def print_err(self, o: object, depth: int = 0) -> None:
        o = self.recursive_eval(o)
        lines = eval(pprint.pformat(o,
                    indent=self.indent,
                    width=self.width, depth=depth + 1, compact=self.compact
                )).split('\n')
        for line in lines:
            print("%s" % line, file=self.stderr)

    def print_debug(self, o: object, depth: int = 0) -> None:
        if main.DEBUG:
            o = self.recursive_eval(o)
            lines = pprint.pformat(o,
                        indent=self.indent,
                        width=self.width, depth=depth + 1, compact=self.compact
                    ).split('\n')
            for line in lines:
                print("%s" % line, file=self.stderr)
