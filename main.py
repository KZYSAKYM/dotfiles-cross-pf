#!/usr/bin/env python3
# -*- cording: utf-8 -*-

import os
import sys
from script import class_parser
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

DEBUG: bool = False

if __name__ == "__main__":
    dotfiles_parser = class_parser.Parser()
    dotfiles = os.path.abspath(os.path.dirname(__file__))
    if sys.platform == 'win32':
        dotfiles += '\\dotfiles'
    else:
        dotfiles += '/dotfiles'
    dotfiles_parser.walk(dotfiles)
