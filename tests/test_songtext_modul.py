import importlib
import os
import sys
import types

# Stub PyQt5 modules to allow importing songtext_modul without PyQt5 installed
qtwidgets = types.ModuleType('PyQt5.QtWidgets')
for name in [
    'QWidget','QVBoxLayout','QHBoxLayout','QLabel','QLineEdit',
    'QTextEdit','QPushButton','QListWidget','QMessageBox','QMenu',
    'QFileDialog','QApplication']:
    setattr(qtwidgets, name, object)
qtcore = types.ModuleType('PyQt5.QtCore')
qtcore.Qt = object
pyqt5 = types.ModuleType('PyQt5')
pyqt5.QtWidgets = qtwidgets
pyqt5.QtCore = qtcore
sys.modules.setdefault('PyQt5', pyqt5)
sys.modules.setdefault('PyQt5.QtWidgets', qtwidgets)
sys.modules.setdefault('PyQt5.QtCore', qtcore)

# Ensure the project root is on sys.path
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

songtext_modul = importlib.import_module('songtext_modul')


def test_clean_basic():
    assert songtext_modul.clean('Hello World!') == 'Hello_World_'


def test_clean_special_chars():
    result = songtext_modul.clean('a-b_c?d')
    assert result == 'a-b_c_d'
