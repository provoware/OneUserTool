# Version 0.1.7
"""Graphische Hauptanwendung für OneUserTool."""
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout, QListWidget,
    QStackedWidget, QLabel
)
from PyQt5.QtCore import Qt
from design_manager import apply_stylesheet
from songtext_modul import SongtextModul
from genres_modul import GenresModul
from zufallsgenerator_modul import ZufallsGeneratorModul

VERSION = "0.1.7"

class HauptModul(QMainWindow):
    """Hauptfenster mit Navigationsleiste und Modulinhalt."""
    def __init__(self):
        super().__init__()
        self.theme="dark"; self.fontsize=16
        self.setWindowTitle("OneUserTool")
        self.resize(1000,700)
        apply_stylesheet(QApplication.instance(), self.theme, self.fontsize)
        self._build_ui()

    def _build_ui(self):
        self.sidebar=QListWidget()
        for name in ["Songtexte","Genres","Zufallsgenerator"]:
            self.sidebar.addItem(name)
        self.sidebar.setFixedWidth(180)
        self.sidebar.itemClicked.connect(self._toggle_module)

        self.stack=QStackedWidget()
        self.stack.addWidget(QWidget())
        self.stack.addWidget(SongtextModul())
        self.stack.addWidget(GenresModul())
        self.stack.addWidget(ZufallsGeneratorModul())

        header=QLabel(f"OneUserTool v{VERSION}")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size:18px; padding:6px;")

        central=QWidget(); v=QVBoxLayout(central)
        v.addWidget(header)
        h=QHBoxLayout(); h.addWidget(self.sidebar); h.addWidget(self.stack,1)
        v.addLayout(h)
        self.setCentralWidget(central)

    def _toggle_module(self,item):
        """Wechselt das angezeigte Modul in der zentralen Ansicht."""
        idx={"Songtexte":1,"Genres":2,"Zufallsgenerator":3}[item.text()]
        if self.stack.currentIndex()==idx:
            self.stack.setCurrentIndex(0); self.sidebar.clearSelection()
        else:
            self.stack.setCurrentIndex(idx)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=HauptModul(); win.show()
    sys.exit(app.exec_())
