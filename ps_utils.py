#!/usr/bin/env python3


def print_tab_iter(it, attr):
    from tabulate import tabulate
    data = [[getattr(t, at, None) for at in attr] for t in it]
    print(tabulate(data, headers=attr))
