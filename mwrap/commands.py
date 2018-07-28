# -*- coding: utf-8 -*-

import os
from collections import defaultdict

from .find import find_wraps_recursive
from .diff import print_wrap_differences

def diff_wrap(args):
    wraps = find_wraps_recursive()
    wrap_map = defaultdict(list)

    for wrap in wraps:
        name = os.path.splitext(os.path.basename(wrap))[0]
        if (args.name is not None) and (name != args.name):
            continue
        wrap_map[name] += [wrap]

    if (args.name is not None) and len(wrap_map) == 0:
        print('No wrap with name', args.name)
        return 1

    for name, wrap_list in wrap_map.items():
        print_wrap_differences(name, wrap_list)
    return 0
