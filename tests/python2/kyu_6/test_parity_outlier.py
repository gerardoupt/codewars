# pylint: disable=missing-docstring

"""Find The Parity Outlier"""

from python2.kyu_6.parity_outlier import find_outlier


def test_odd_number():
    assert find_outlier([2, 3, 4, 6, 8]) == 3


def test_even_number():
    assert find_outlier([3, 5, 7, 2]) == 2
