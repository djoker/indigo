import pytest
from src.DataCapture.stats import Stats

def test_creation_stat():
    lst = [3,9,3,4,6]
    stat = Stats(lst)
    assert stat.data == [3,3,4,6,9]

def test_less_stat():
    lst = [3,9,3,4,6]
    stat = Stats(lst)
    assert stat.less(6) == 3

def test_between_stat():
    lst = [3,9,3,4,6]
    stat = Stats(lst)
    assert stat.between(3,6) == 4

def test_greater_stat():
    lst = [3,9,3,4,6]
    stat = Stats(lst)
    assert stat.greater(4) == 2


