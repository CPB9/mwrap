# -*- coding: utf-8 -*-

import os

def _extract_value_from_wrap(wrap_path, key_name):
    f = open(wrap_path, 'r')
    for line in f.readlines():
        parts = line.split('=')
        if len(parts) != 2:
            continue
        key = parts[0].strip()
        value = parts[1].strip()
        if key == key_name:
            return value
    return None


def find_wrap(name, path = ''):
    wrap_path = os.path.join(path, 'subprojects', name + '.wrap')
    if os.path.exists(wrap_path):
        return wrap_path
    return None


def find_wraps(path = ''):
    subp_path = os.path.join(path, 'subprojects')
    if not os.path.exists(subp_path):
        return []
    return [os.path.join(subp_path, f) for f in os.listdir(subp_path) if f.endswith('.wrap')]


def find_wraps_recursive(path = ''):
    wraps = find_wraps(path)
    for wrap in wraps:
        d = _extract_value_from_wrap(wrap, 'directory')
        if d is not None:
            proj_path = os.path.join(os.path.dirname(wrap), d)
            wraps += find_wraps(proj_path)
    return wraps

