#!/usr/bin/env python3

from typing import Optional, List
from tabulate import tabulate
from collections import OrderedDict

def print_tab_obj(it, attr):
    from tabulate import tabulate
    data = [[getattr(t, at, None) for at in attr] for t in it]
    print(tabulate(data, headers=attr))

def print_tab_dict(it, attr):
    from tabulate import tabulate
    data = [[t[at] for at in attr if at in t.keys ()] for t in it]
    print(tabulate(data, headers=attr))

def print_attributes(obj, attr:Optional [List[str]]= None, trim=True, use_str=True):
    """
    Print attribute names in one column, values in the other. If not list of 
    attributes is supplies, the attributes are gather from `dir()`.
    :trim: If true, trim value column to max `ncolumns` ncolumns (80)
    :use_str: Jeśli nieprawda, to użyk `repr()` zamiast `str()`
    """
    ncolumns = 80
    if attr == None:
        attr = dir (obj)
    table = OrderedDict ()
    for at in dir (obj):
        try:
            table[at] = getattr (obj,at)
        except Exception as e:
            table [at] = ""
    table = list (table.items ())
    table = [list (kv_pair) for kv_pair in table]

    for row in table:
        if use_str:
            row[1] = str (row[1])
        else:
            row[1] = repr (row[1])
        if trim:
            row[1] =  row[1][:ncolumns]
    print (tabulate (table, headers = ['name', 'value']))
