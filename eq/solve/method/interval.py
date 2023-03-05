from typing import NamedTuple

T = float

class Interval(NamedTuple):
    left: T
    right: T

    @property
    def length(self) -> T:
        return self.right - self.left
    
    @property
    def middle(self) -> T:
        return (self.left + self.right) / 2
    
    @property
    def left_half(self) -> 'Interval':
        return Interval(self.left, self.middle)

    @property
    def right_half(self) -> 'Interval':
        return Interval(self.middle, self.right)
