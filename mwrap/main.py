# -*- coding: utf-8 -*-

import argparse
import colorama

from . import commands

def main():
    colorama.init()

    parser = argparse.ArgumentParser(description='Meson subproject tool', prog='mwrap')
    subparsers = parser.add_subparsers(title='Commands', dest='command')
    subparsers.required = True #kwarg doesn't work

    p = subparsers.add_parser('diff-wrap', help='Show wrap file differences between subproject and subsubproject')
    p.add_argument('name', help='subproject name', nargs='?')
    p.set_defaults(command=commands.diff_wrap)

    args = parser.parse_args()
    return args.command(args)

