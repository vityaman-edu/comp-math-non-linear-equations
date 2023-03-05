from f.parse import parse

if __name__ == '__main__':
    f = parse(input('f(x) = '))
    print('f(1) =', f.value({'x': 1}))
