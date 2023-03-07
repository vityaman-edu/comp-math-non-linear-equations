import numpy as np
import matplotlib.pyplot as plt
from eq.f.core import Function
from eq.solve.method.interval import Interval

def plot(
    filepath: str, 
    f: Function, 
    interval: Interval
) -> None:
    df = f.diff()

    figure, axis = plt.subplots(1, 2)

    for i in range(2):    
        axis[i].spines['left'].set_position('center')
        axis[i].spines['bottom'].set_position('zero')
        axis[i].spines['right'].set_color('none')
        axis[i].spines['top'].set_color('none')
        axis[i].xaxis.set_ticks_position('bottom')
        axis[i].yaxis.set_ticks_position('left')

    l, r = interval.left, interval.right
    x = np.linspace(l, r, 100)
    
    axis[0].plot(x, df(x))
    axis[0].set_title(f'f\'([{l}, {r}])')

    axis[1].plot(x, f(x))
    axis[1].set_title(f'f([{l}, {r}])')

    plt.savefig(filepath)
