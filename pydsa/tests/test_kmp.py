"""Test for kmp function."""
from pydsa import kmp


def test_bubble_sort():
    a = "BBC ABCDAB ABCDABCDABDE"
    b = "ABCDABD"
    assert kmp(a, b) == 15
