from sympy.parsing.sympy_parser import parse_expr
from eq.f.core import Function, SympyPoweredFunction


def parse(input: str) -> Function:
    return SympyPoweredFunction(
        parse_expr(
            s = input, 
            evaluate = False,
            transformations = 'all'
        )
    )
