from sympy import Function as SympyFunction
from sympy import diff
from sympy import lambdify
from sympy.abc import x


class Function:
    def __call__(self, x: float) -> float:
        raise NotImplementedError()
    
    def diff(self) -> 'Function':
        raise NotImplementedError()


class SympyPoweredFunction(Function):
    def __init__(self, func: SympyFunction) -> None:
        self.func = func
        self.lmbd = lambdify(x, self.func)

    def __call__(self, x: float) -> float:
        return self.lmbd(x)
    
    def diff(self) -> Function:
        return SympyPoweredFunction(diff(self.func))
