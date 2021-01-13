import pytest
from hog_pytest.pytestcode.calculator import Calulator


class TestCalc:
    def setup_class(self):
        self.calc = Calulator()
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect", [(3, 5, 8)],
                             ids=["add"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.test_add(a, b)

    @pytest.mark.parametrize("a,b,expect", [(-1, -2, 1)],
                             ids=["subt"])
    def test_subt(self, a, b, expect):
        assert expect == self.calc.test_subtract(a, b)

    @pytest.mark.parametrize("a,b,expect", [(100, 300, 30000)],
                             ids=["mult"])
    def test_mult(self, a, b, expect):
        assert expect == self.calc.test_multiplication(a, b)

    @pytest.mark.parametrize("a,b,expect", [(10, 5, 2)],
                             ids=["divi"])
    def test_divi(self, a, b, expect):
        assert expect == self.calc.test_division(a, b)
