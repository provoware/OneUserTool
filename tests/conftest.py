import sys
import os
import types

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Provide minimal stubs for PyQt5 if the real package is unavailable
try:
    import PyQt5  # noqa: F401
except ModuleNotFoundError:
    pyqt = types.ModuleType("PyQt5")
    qtwidgets = types.ModuleType("PyQt5.QtWidgets")
    qtcore = types.ModuleType("PyQt5.QtCore")
    dummy_names = [
        "QWidget", "QVBoxLayout", "QHBoxLayout", "QLabel", "QLineEdit",
        "QTextEdit", "QPushButton", "QListWidget", "QMessageBox",
        "QMenu", "QFileDialog", "QApplication"
    ]
    for name in dummy_names:
        setattr(qtwidgets, name, type(name, (), {}))
    qtcore.Qt = type("Qt", (), {})
    sys.modules['PyQt5'] = pyqt
    sys.modules['PyQt5.QtWidgets'] = qtwidgets
    sys.modules['PyQt5.QtCore'] = qtcore
