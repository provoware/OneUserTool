"""Main window of OneUserTool."""

import argparse
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QListWidget,
    QMainWindow,
    QStackedWidget,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
)
from PyQt5.QtCore import Qt

from design_manager import apply_stylesheet
from genres_modul import GenresModul
from songtext_modul import SongtextModul
from version import __version__
from zufallsgenerator_modul import ZufallsGeneratorModul


class HauptModul(QMainWindow):
    def __init__(self, theme: str = "dark", fontsize: int = 16) -> None:
        super().__init__()
        self.theme = theme
        self.fontsize = fontsize
        self.setWindowTitle("OneUserTool")
        self.resize(1000, 700)
        apply_stylesheet(QApplication.instance(), self.theme, self.fontsize)
        self._build_ui()

    def _build_ui(self) -> None:
        self.sidebar = QListWidget()
        for name in ["Songtexte", "Genres", "Zufallsgenerator"]:
            self.sidebar.addItem(name)
        self.sidebar.setFixedWidth(180)
        self.sidebar.itemClicked.connect(self._toggle_module)

        self.stack = QStackedWidget()
        self.stack.addWidget(QWidget())
        self.stack.addWidget(SongtextModul())
        self.stack.addWidget(GenresModul())
        self.stack.addWidget(ZufallsGeneratorModul())

        header = QLabel(f"OneUserTool v{__version__}")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size:18px; padding:6px;")

        central = QWidget()
        v = QVBoxLayout(central)
        v.addWidget(header)
        h = QHBoxLayout()
        h.addWidget(self.sidebar)
        h.addWidget(self.stack, 1)
        v.addLayout(h)
        self.setCentralWidget(central)

    def _toggle_module(self, item) -> None:
        idx = {"Songtexte": 1, "Genres": 2, "Zufallsgenerator": 3}[item.text()]
        if self.stack.currentIndex() == idx:
            self.stack.setCurrentIndex(0)
            self.sidebar.clearSelection()
        else:
            self.stack.setCurrentIndex(idx)

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Start OneUserTool")
    parser.add_argument(
        "--theme",
        choices=["dark", "light", "highcontrast"],
        default="dark",
        help="Farbschema der Anwendung",
    )
    parser.add_argument(
        "--fontsize",
        type=int,
        default=16,
        help="Grundlegende Schriftgröße",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    app = QApplication(sys.argv)
    win = HauptModul(args.theme, args.fontsize)
    win.show()
    sys.exit(app.exec_())
