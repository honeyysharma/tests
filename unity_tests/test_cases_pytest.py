from inverter import invert
import pytest

def test_invert():
    inverted = invert(None)
    assert inverted == ""

    inverted = invert("a")
    assert inverted == "a"

    inverted = invert("abcd")
    assert inverted == "dcba"