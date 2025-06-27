import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
try:
    from songtext_modul import clean
except ModuleNotFoundError:
    pytest.skip("PyQt5 not available", allow_module_level=True)

@pytest.mark.parametrize("inp,expected", [
    ("Hello World", "Hello_World"),
    ("special-äöü", "special-_"),
])
def test_clean(inp, expected):
    assert clean(inp) == expected

