from collections.abc import Callable, Sequence
from typing import Literal, Optional

Operator = Literal['+', '-', '*', '/']
Calc = Callable[[float, float], float]

OPERATORS: dict[Operator, Calc] = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

PRECEDENCES: dict[Operator, int] = { '+': 1, '-': 1, '*': 2, '/': 2 }

def evaluate(expression: str, threaded=False) -> Optional[float]:
    if not expression or expression.isspace(): return None
    tokens = expression.strip().split()

    return _evaluate_infix(tokens
        ) if not threaded else _evaluate_infix(tokens, [], [])


def _evaluate_infix(
    tokens: Sequence[str], _ops: list[Operator] = [], _vals: list[float] = []
) -> float:
    _ops.clear()
    _vals.clear()

    for token in tokens:
        if token in OPERATORS:
            while _ops and PRECEDENCES[_ops[-1]] >= PRECEDENCES[token]:
                _apply_operator(_ops, _vals)
            _ops.append(token)
        else:
            try: _vals.append(float(token))
            except ValueError: raise ValueError("invalid token: " + token)

    while _ops: _apply_operator(_ops, _vals)

    if len(_vals) != 1: raise ValueError("invalid expression")
    return _vals[0]


def _apply_operator(operators: list[Operator], values: list[float]):
    if not operators: return
    operator = operators.pop()

    if len(values) < 2:
        raise ValueError("not enough operands for operator " + operator)

    b = values.pop()
    a = values.pop()
    values.append( OPERATORS[operator](a, b) )


__all__ = "evaluate", "Operator", "Calc", "OPERATORS", "PRECEDENCES"
