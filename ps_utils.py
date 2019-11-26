#!/usr/bin/env python3


def print_tab_obj(it, attr):
    from tabulate import tabulate
    data = [[getattr(t, at, None) for at in attr] for t in it]
    print(tabulate(data, headers=attr))

def print_tab_dict(it, attr):
    from tabulate import tabulate
    data = [[t[at] for at in attr if at in t.keys ()] for t in it]
    print(tabulate(data, headers=attr))
