# Version 0.1.0
import os, datetime
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit,
    QPushButton, QListWidget, QMenu, QMessageBox
)
from PyQt5.QtCore import Qt


def dirpath():
    base = os.path.dirname(os.path.abspath(__file__))
    p = os.path.join(base, "Projekt", "Notizen")
    os.makedirs(p, exist_ok=True)
    return p


class NotizenModul(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notizen")
        self.resize(500, 400)
        v = QVBoxLayout(self)
        v.addWidget(QLabel("Notiz:"))
        self.te = QTextEdit()
        v.addWidget(self.te)
        v.addWidget(QPushButton("Speichern", clicked=self.save))
        v.addWidget(QLabel("Gespeicherte Notizen:"))
        self.lst = QListWidget()
        self.lst.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lst.customContextMenuRequested.connect(self.ctx)
        v.addWidget(self.lst)
        self.load()

    def save(self):
        txt = self.te.toPlainText().strip()
        if not txt:
            return
        fn = datetime.datetime.now().strftime('%Y%m%d_%H%M%S.txt')
        with open(os.path.join(dirpath(), fn), 'w', encoding='utf-8') as f:
            f.write(txt)
        self.te.clear()
        self.load()

    def load(self):
        self.lst.clear()
        for fn in sorted(os.listdir(dirpath()), reverse=True):
            if fn.endswith('.txt'):
                self.lst.addItem(fn)

    def ctx(self, pos):
        it = self.lst.itemAt(pos)
        if not it:
            return
        menu = QMenu(self)
        show = menu.addAction("Anzeigen")
        delete = menu.addAction("Löschen")
        ch = menu.exec_(self.lst.mapToGlobal(pos))
        fp = os.path.join(dirpath(), it.text())
        if ch == show:
            with open(fp, 'r', encoding='utf-8') as f:
                QMessageBox.information(self, it.text(), f.read())
        elif ch == delete and QMessageBox.question(
            self, "Löschen", f"{it.text()} löschen?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            os.remove(fp)
            self.load()
