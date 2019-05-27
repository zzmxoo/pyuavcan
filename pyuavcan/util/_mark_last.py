#
# Copyright (c) 2019 UAVCAN Development Team
# This software is distributed under the terms of the MIT License.
# Author: Pavel Kirienko <pavel.kirienko@zubax.com>
#

import typing


ML = typing.TypeVar('ML')


def mark_last(it: typing.Iterable[ML]) -> typing.Iterable[typing.Tuple[bool, ML]]:
    """
    This is an iteration helper like enumerate(). It amends every item with a boolean flag which is False
    for all items except the last one. If the input iterable is empty, yields nothing.
    """
    it = iter(it)
    try:
        last = next(it)
    except StopIteration:
        pass
    else:
        for val in it:
            yield False, last
            last = val
        yield True, last


def _unittest_util_mark_last() -> None:
    assert [] == list(mark_last([]))
    assert [(True, 123)] == list(mark_last([123]))
    assert [(False, 123), (True, 456)] == list(mark_last([123, 456]))
    assert [(False, 123), (False, 456), (True, 789)] == list(mark_last([123, 456, 789]))
