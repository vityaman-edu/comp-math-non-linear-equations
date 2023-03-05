from sympy import Symbol, Function as SympyFunction


class Function:
    def value(self, vars: dict[str, float]) -> float:
        raise NotImplementedError()


class SympyPoweredFunction(Function):
    def __init__(self, func: SympyFunction) -> None:
        self.func = func

    def value(self, vars: dict[str, float]) -> float:
        func = self.func
        for var, value in vars.items():
            func = func.subs(Symbol(var), value)
        return float(func.evalf())
