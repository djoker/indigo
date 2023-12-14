import pytest
from src.DataCapture.capture import Capture


def test_creation():
    cap_test = Capture()
    assert cap_test.data == []

def test_charge():
    cap_test = Capture()
    cap_test.add(1)
    cap_test.add(2)
    cap_test.add(3)

    assert cap_test.data == [1,2,3]

def test_wrong_type_entry():
    cap_test = Capture()
    with pytest.raises(ValueError):
        cap_test.add("X")

def test_create_stat():
    cap_test = Capture()
    cap_test.add(3)
    cap_test.add(9)
    cap_test.add(3)
    cap_test.add(4)
    cap_test.add(6)
    stats = cap_test.build_stats()

    assert stats.data == [3,3,4,6,9]
