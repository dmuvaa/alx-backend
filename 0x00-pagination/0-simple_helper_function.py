#!/usr/bin/env python3

"""create a function"""

def index_range(page, page_size):
    """ function should return a tuple of size two"""
    index1 = (page - 1) * page_size
    index2 = page * page_size
    return (index1, index2)
