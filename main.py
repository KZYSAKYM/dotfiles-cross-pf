#!/usr/bin/env python3
# -*- cording: utf-8 -*-

import os
import sys
import argparse
from script import class_parser
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

parser = argparse.ArgumentParser()
parser.add_argument(
        "--debug",
        action="store_true",
        help="enable debug messages")
parser.add_argument(
        "--recipe",
        nargs="*",
        action="store",
        help="specify recipes")

args = parser.parse_args()
DEBUG: bool = args.debug
RECIPES: tuple
if args.recipe:
    RECIPES = tuple(args.recipe)
    print("specified recipes: {}".format(RECIPES))
else:
    RECIPES = ()

if __name__ == "__main__":
    dotfiles_parser = class_parser.Parser()
    dotfiles = os.path.abspath(os.path.dirname(__file__))
    homedir = os.path.expanduser('~')
    os.environ['TOP_DIR'] = dotfiles
    if sys.platform == 'win32':
        os.environ['DOT_DIR'] = dotfiles + '\\dotfiles'
        os.environ['CONF_DIR'] = dotfiles + '\\config'
        os.environ['HOME_CONF'] = homedir + '\\.config'
        os.environ['HOME_CACHE'] = homedir + '\\.cache'
        os.environ['HOME_LOCAL'] = homedir + '\\.local'
    else:
        os.environ['DOT_DIR'] = dotfiles + '/dotfiles'
        os.environ['CONF_DIR'] = dotfiles + '/config'
        os.environ['HOME_CONF'] = homedir + '/.config'
        os.environ['HOME_CACHE'] = homedir + '/.cache'
        os.environ['HOME_LOCAL'] = homedir + '/.local'
    dotfiles_parser.walk(os.environ['DOT_DIR'], RECIPES)
