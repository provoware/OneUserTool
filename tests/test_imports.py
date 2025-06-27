import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import importlib

modules = [
    "main",
    "songtext_modul",
    "genres_modul",
    "zufallsgenerator_modul",
]

pyqt_available = True
try:
    import PyQt5  # noqa: F401
except ImportError:
    pyqt_available = False


@pytest.mark.parametrize("name", modules)
def test_import(name):
    if not pyqt_available:
        pytest.skip("PyQt5 nicht installiert")
    importlib.import_module(name)
