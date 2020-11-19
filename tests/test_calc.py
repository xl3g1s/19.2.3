import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_summ_correctly(self):
        assert self.calc.adding(self, 5,3) == 8

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 9,4) == 5

    def test_division_correctly(self):
        assert self.calc.division(self, 12,5) == 2.4

    def test_multiply_correctly(self):
        assert self.calc.multiply(self, 9,4) == 36

