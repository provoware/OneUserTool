# Version 0.1.8
import random
from profiles_utils import data_path, load_profiles
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QComboBox, QListWidget, QMessageBox, QApplication
)
from PyQt5.QtCore import Qt

class ZufallsGeneratorModul(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zufallsgenerator")
        self.resize(450,360)
        v = QVBoxLayout(self)
        h = QHBoxLayout()
        # Profil-ComboBox alphabetisch
        profiles = sorted(load_profiles().keys(), key=str.lower)
        if not profiles:
            QMessageBox.warning(self, "Fehler", "Keine Genre-Profile vorhanden!")
        self.cb = QComboBox()
        self.cb.addItems(profiles)
        self.cb.currentIndexChanged.connect(self.reload)
        v.addWidget(QLabel("Profil:"))
        v.addWidget(self.cb)
        # Ergebnis-Liste
        self.lst = QListWidget()
        v.addWidget(self.lst)
        # Schnelltasten
        for n in [4,6,8,10,12,14,16,18,20]:
            btn = QPushButton(f"{n} Genres")
            btn.clicked.connect(lambda _,x=n: self.pick(x))
            h.addWidget(btn)
        v.addLayout(h)
        # Kopieren-Knopf
        v.addWidget(QPushButton("Kopieren", clicked=self.copy))
        self.reload()

    def reload(self):
        self.genres = load_profiles().get(self.cb.currentText(), [])
        self.lst.clear()

    def pick(self, n):
        if not self.genres:
            return QMessageBox.warning(self, "Fehler", "Keine Genres geladen")
        sel = random.sample(self.genres, min(n, len(self.genres)))
        self.lst.clear()
        for g in sel:
            self.lst.addItem(g)
        QApplication.clipboard().setText(", ".join(sel))

    def copy(self):
        txt = ", ".join(self.lst.item(i).text() for i in range(self.lst.count()))
        QApplication.clipboard().setText(txt)
        QMessageBox.information(self, "Kopiert", "Genres in Zwischenablage")
