# Version 0.1.7
import sys
import os
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QStackedWidget,
    QLabel,
    QTextEdit,
    QMessageBox,
)
from PyQt5.QtCore import Qt
from design_manager import apply_stylesheet
from songtext_modul import SongtextModul
from genres_modul import GenresModul
from zufallsgenerator_modul import ZufallsGeneratorModul

VERSION = "0.1.7"


class HauptModul(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theme = "dark"
        self.fontsize = 16
        self.setWindowTitle("OneUserTool")
        self.resize(1000, 700)
        apply_stylesheet(QApplication.instance(), self.theme, self.fontsize)
        if not os.path.isdir(os.path.join(os.path.dirname(__file__), "venv")):
            QMessageBox.information(
                self,
                "Hinweis",
                'Bitte fuehren Sie vor dem ersten Start "bash setup.sh" aus.',
            )
        self._build_ui()

    def _build_ui(self):
        self.sidebar = QListWidget()
        for name in ["Songtexte", "Genres", "Zufallsgenerator"]:
            self.sidebar.addItem(name)
        self.sidebar.setFixedWidth(180)
        self.sidebar.itemClicked.connect(self._toggle_module)

        self.stack = QStackedWidget()
        self.stack.addWidget(QWidget())
        self.stack.addWidget(SongtextModul(self.log))
        self.stack.addWidget(GenresModul(self.log))
        self.stack.addWidget(ZufallsGeneratorModul(self.log))

        header = QLabel(f"OneUserTool v{VERSION}")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size:18px; padding:6px;")

        self.log_widget = QTextEdit()
        self.log_widget.setReadOnly(True)
        self.log_widget.setFixedHeight(100)

        central = QWidget()
        v = QVBoxLayout(central)
        v.addWidget(header)
        h = QHBoxLayout()
        h.addWidget(self.sidebar)
        h.addWidget(self.stack, 1)
        v.addLayout(h)
        v.addWidget(self.log_widget)
        self.setCentralWidget(central)
        self.log("Anwendung gestartet")

    def _toggle_module(self, item):
        idx = {"Songtexte": 1, "Genres": 2, "Zufallsgenerator": 3}[item.text()]
        if self.stack.currentIndex() == idx:
            self.stack.setCurrentIndex(0)
            self.sidebar.clearSelection()
        else:
            self.stack.setCurrentIndex(idx)

    def log(self, text):
        self.log_widget.append(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = HauptModul()
    win.show()
    sys.exit(app.exec_())
