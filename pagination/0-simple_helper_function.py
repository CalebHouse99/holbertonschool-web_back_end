#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    """Tuple of size two with start and end"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
