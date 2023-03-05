from f.parsing import parse
from plot import plot
from solve.method.interval import Interval
from solve.method import half

if __name__ == '__main__':
    f = 'x ^ 3 + 2.64 * x ^ 2 - 5.41 * x - 11.76'
    f = parse(f)

    plot('res/plot.png', f, Interval(-5, 5))

    intervals = [Interval(l, r) for l, r in [
        (-4, -2.5), (-2.5, 0), (1, 3)
    ]]
    methods = [half.root, half.root, half.root]
    for i in range(len(intervals)):
        interval = intervals[i]
        method = methods[i]
        with open(f'res/0{i + 2}-table.part', 'w') as file:
            print(f'Таблица трассировки {i + 1}', file=file)
            print(method(
                f, interval, 0.01, 
                lambda *args: print(
                    '',
                    *args, 
                    sep = ' | ',
                    end='|\n',
                    file = file,
                )
            ))
            print(file=file)

