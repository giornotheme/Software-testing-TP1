from unittest import TestCase

from rpn import rpn


class Test(TestCase):
    def test_rpn_add(self):
        result = rpn("20 2 +")
        assert result == 22

    def test_rpn_sub(self):
        result = rpn("4 2 + 3 -")
        assert result == 3

    def test_rpn_mul(self):
        result = rpn("2 3 * 4 *")
        assert result == 24
