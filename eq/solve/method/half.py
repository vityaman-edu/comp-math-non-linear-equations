from typing import Callable, List
from eq.solve.method.interval import Interval

T = float

def is_interesting(
    interval: Interval, 
    f: Callable[[T], T]
) -> bool:
    return f(interval.left) * f(interval.right) < 0


def root(
    f: Callable[[T], T], 
    interval: Interval,
    eps: T,
    log: Callable[[List[object]], None] = lambda s: None
) -> T:
    assert is_interesting(interval, f)
    log(
        'i', 
        'a', 
        'b', 
        'x', 
        'f(a)', 
        'f(b)', 
        'f(x)', 
        'b - a'
    )
    log(
        *['---' for i in range(8)]
    )
    i = 0
    while eps < interval.length:
        i += 1
        log(
            i,
            "%.2f" % round(interval.left, 2),
            "%.2f" % round(interval.right, 2),
            "%.2f" % round(interval.middle, 2),
            "%.2f" % round(f(interval.left), 2),
            "%.2f" % round(f(interval.right), 2),
            "%.2f" % round(f(interval.middle), 2),
            "%.2f" % round(interval.length, 2)
        )
        interval = interval.left_half \
            if is_interesting(interval.left_half, f) \
            else interval.right_half
    return interval.middle
