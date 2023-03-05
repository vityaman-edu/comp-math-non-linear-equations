from typing import Callable, Iterable, List

from numpy import sign
from interval import Interval

T = float

def find_root_intervals(
    f: Callable[[T], T],
    interval: Interval,
    window: int
) -> Iterable[Interval]:
    assert window > 0
    while True:
        left = interval.left
        right = left + window
        if interval.right < right:
            break
        if f(left) * f(right) < 0:
            yield Interval(left, right)
