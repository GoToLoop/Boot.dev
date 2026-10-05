#!/usr/bin/env python3

from unittest import TestCase, main
from math import inf, isnan
from typing import Final, final, override
from pkg.calculator import evaluate

neg_inf: Final = -inf

@final
class TestCalculator(TestCase):
    @override
    def setUp(self): self.calculator = evaluate

    def test_addition(self):
        self.assertEqual(self.calculator("3 + 5"), 8)

    def test_subtraction(self):
        self.assertEqual(self.calculator("10 - 4"), 6)

    def test_multiplication(self):
        self.assertEqual(self.calculator("3 * 4"), 12)

    def test_division(self):
        self.assertEqual(self.calculator("10 / 2"), 5)

    def test_division_by_zero_edges(self) -> None:
        # Positive numerator divided by zero -> inf
        self.assertEqual(self.calculator("5 / 0"), inf)

        # Negative numerator divided by zero -> -inf
        self.assertEqual(self.calculator("-5 / 0"), neg_inf)

        # Zero divided by zero -> nan (must use math.isnan because nan != nan)
        result = self.calculator("0 / 0")
        assert result is not None
        self.assertTrue(isnan(result))

    def test_floor_division(self) -> None:
        self.assertEqual(self.calculator("7 // 2"), 3)

    def test_floor_division_by_zero_edges(self) -> None:
        self.assertEqual(self.calculator("5 // 0"), inf)
        self.assertEqual(self.calculator("-5 // 0"), neg_inf)

        result = self.calculator("0 // 0")
        assert result is not None
        self.assertTrue(isnan(result))

    def test_modulo(self) -> None:
        self.assertEqual(self.calculator("7 % 3"), 1)

    def test_modulo_by_zero(self) -> None:
        # Modulo by zero is always undefined (nan)
        result1 = self.calculator("5 % 0")
        result2 = self.calculator("0 % 0")

        assert result1 is not None and result2 is not None

        self.assertTrue(isnan(result1))
        self.assertTrue(isnan(result2))

    def test_exponentiation(self) -> None:
        self.assertEqual(self.calculator("2 ** 3"), 8)

    def test_zero_to_negative_power(self) -> None:
        # Zero to a negative power should safely yield inf instead of crashing
        self.assertEqual(self.calculator("0 ** -2"), inf)

    def test_exponentiation_precedence(self) -> None:
            # 3**2 evaluates first (9), then 2 + 9 = 11 (not (2 + 3) ** 2 = 25)
            self.assertEqual(self.calculator("2 + 3 ** 2"), 11)
            # 3**2 evaluates first (9), then 2 * 9 = 18
            self.assertEqual(self.calculator("2 * 3 ** 2"), 18)

    def test_nested_expression(self):
        self.assertEqual(self.calculator("3 * 4 + 5"), 17)

    def test_complex_expression(self):
        self.assertEqual(self.calculator("2 * 3 - 8 / 2 + 5"), 7)

    def test_empty_expression(self):
        self.assertIsNone(self.calculator(""))

    def test_invalid_operator(self):
        with self.assertRaises(ValueError): self.calculator("$ 3 5")

    def test_not_enough_operands(self):
        with self.assertRaises(ValueError): self.calculator("+ 3")


if __name__ == "__main__": main()
