# -*- coding: utf-8 -*-

import difflib
import sys
import colorama

def print_unified_diff(diff):
    for d in diff:
        if d.startswith('+++') or d.startswith('---'):
            sys.stdout.write(colorama.Style.BRIGHT)
        elif d.startswith('@@'):
            sys.stdout.write(colorama.Fore.CYAN)
        elif d.startswith('-'):
            sys.stdout.write(colorama.Fore.RED)
        elif d.startswith('+'):
            sys.stdout.write(colorama.Fore.GREEN)
        sys.stdout.write(d + colorama.Style.NORMAL + colorama.Fore.RESET)


def print_wrap_differences(name, wraps):
    if len(wraps) > 1:
        w1, w2 = wraps[0], wraps[1]
        tail = wraps[1:]
        diff = difflib.unified_diff(open(w1, 'r').readlines(), open(w2, 'r').readlines(), fromfile=w1, tofile=w2)
        print_unified_diff(diff)
        print_wrap_differences(name, tail)


