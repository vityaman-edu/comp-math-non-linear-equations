import sys
from eq import example

if __name__ == '__main__':
    match sys.argv[1]:
        case 'examaple':
            example()
        case other:
            print(f'invalid mode {other}')
