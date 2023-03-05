import numpy as np
import matplotlib.pyplot as plt
from common import f, df


if __name__ == '__main__':
    figure, axis = plt.subplots(1, 2)

    for i in range(2):    
        axis[i].spines['left'].set_position('center')
        axis[i].spines['bottom'].set_position('zero')
        axis[i].spines['right'].set_color('none')
        axis[i].spines['top'].set_color('none')
        axis[i].xaxis.set_ticks_position('bottom')
        axis[i].yaxis.set_ticks_position('left')

    l, r, n = -3, 2, 100
    x = np.linspace(l, r, n)
    axis[0].plot(x, df(x))
    axis[0].set_title(f'f\'([{l}, {r}])')

    l, r, n = -5, 3, 100
    x = np.linspace(l, r, n)
    axis[1].plot(x, f(x))
    axis[1].set_title(f'f([{l}, {r}])')

    plt.savefig('res/plot.png')
