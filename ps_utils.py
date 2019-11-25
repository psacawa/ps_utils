#!/usr/bin/env python3

from tabulate import tabulate

def print_tab_iter(it, attr):
    data = [[getattr(t, at, None) for at in attr] for t in it]
    print(tabulate(data, headers=attr))
