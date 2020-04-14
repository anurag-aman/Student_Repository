import os
from datetime import datetime, timedelta
from typing import Tuple , Iterator, IO , List
from prettytable import PrettyTable


def file_reader(path, num_fields, sep, header=False) -> Iterator[Tuple[str]]:
    """ function to return the tuple separated with separator , if any value error comes it should display the error on the line and expected value"""
    try:
        fp:IO = open(path , 'r')
    except FileNotFoundError:
        raise FileNotFoundError("path not found")
    else:
        with fp:
            for n , line in enumerate(fp , 1):
                fields: List[str] = line.rstrip('\n').split(sep)
                if len(fields) != num_fields:
                    raise ValueError(f"'{path}' line:{n} read {len(fields)} but expected {num_fields}")
                elif n > 1 or header is False:
                    yield tuple(fields)