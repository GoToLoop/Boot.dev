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

def evaluate(
    expression: str, _ops: list[Operator] = [], _vals: list[float] = []
) -> Optional[float]:
    if not expression or expression.isspace(): return None
    _ops.clear; _vals.clear()
    return _evaluate_infix(expression.strip().split(), _ops, _vals)


def evaluate_threaded(
    expression: str, ops: list[Operator], vals: list[float]
) -> Optional[float]:
    if not expression or expression.isspace(): return None
    return _evaluate_infix(expression.strip().split(), ops, vals)


def _evaluate_infix(
    tokens: Sequence[str], ops: list[Operator], vals: list[float]
) -> float:
    for token in tokens:
        if token in OPERATORS:
            while ops and PRECEDENCES[ops[-1]] >= PRECEDENCES[token]:
                _apply_operator(ops, vals)
            ops.append(token)
        else:
            try: vals.append(float(token))
            except ValueError: raise ValueError("invalid token: " + token)

    while ops: _apply_operator(ops, vals)

    if len(vals) != 1: raise ValueError("invalid expression")
    return vals[0]


def _apply_operator(operators: list[Operator], values: list[float]):
    if not operators: return
    operator = operators.pop()

    if len(values) < 2:
        raise ValueError("not enough operands for operator " + operator)

    b = values.pop(); a = values.pop()
    values.append( OPERATORS[operator](a, b) )


__all__ = (
    "evaluate", "evaluate_threaded",
    "Operator", "Calc",
    "OPERATORS", "PRECEDENCES"
)
