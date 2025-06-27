# Version 0.1.8
import os, re, datetime, shutil
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QListWidget,
    QMessageBox,
    QMenu,
    QFileDialog,
)
from PyQt5.QtCore import Qt


def clean(s):
    return re.sub(r"[^\w\-]", "_", s)


def dirpath():
    base = os.path.dirname(os.path.abspath(__file__))
    p = os.path.join(base, "Projekt", "Songtexte")
    os.makedirs(p, exist_ok=True)
    return p


class SongtextModul(QWidget):
    def __init__(self, log=lambda *a: None):
        super().__init__()
        self.log = log
        self.setWindowTitle("Songtext-Editor")
        self.resize(700, 600)
        v = QVBoxLayout(self)
        # Titel + Genre
        v.addWidget(QLabel("Songtitel*:"))
        self.t = QLineEdit()
        self.t.returnPressed.connect(self.save)
        v.addWidget(self.t)
        h = QHBoxLayout()
        self.g = QLineEdit()
        self.g.returnPressed.connect(self.save)
        h.addWidget(self.g)
        h.addWidget(QPushButton("Aus Zwischenablage", clicked=self.paste))
        v.addLayout(h)
        # Text
        v.addWidget(QLabel("Songtext*:"))
        self.te = QTextEdit()
        v.addWidget(self.te)
        v.addWidget(QPushButton("Speichern", clicked=self.save))
        # Übersicht
        v.addWidget(QLabel("Übersicht:"))
        self.lst = QListWidget()
        self.lst.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lst.customContextMenuRequested.connect(self.ctx)
        v.addWidget(self.lst)
        self.load()
        self.log("Songtext-Modul geladen")

    def paste(self):
        from PyQt5.QtWidgets import QApplication

        self.g.setText(QApplication.clipboard().text())

    def save(self):
        ti = self.t.text().strip()
        tx = self.te.toPlainText().strip()
        if not ti or not tx:
            return QMessageBox.warning(self, "Fehler", "Titel und Text erforderlich")
        fn = f"{clean(ti)}_{clean(self.g.text() or 'ohneGenre')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(os.path.join(dirpath(), fn), "w", encoding="utf-8") as f:
                f.write(f"Titel: {ti}\nGenre: {self.g.text()}\n---\n{tx}")
            QMessageBox.information(self, "OK", "Gespeichert")
            self.log(f"Songtext '{fn}' gespeichert")
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Speichern fehlgeschlagen:\n{e}")
        self.t.clear()
        self.g.clear()
        self.te.clear()
        self.load()

    def load(self):
        self.lst.clear()
        for fn in sorted(os.listdir(dirpath()), reverse=True):
            if fn.endswith(".txt"):
                self.lst.addItem(fn)

    def ctx(self, pos):
        it = self.lst.itemAt(pos)
        if not it:
            return
        menu = QMenu(self)
        e = menu.addAction("Bearbeiten")
        d = menu.addAction("Löschen")
        ch = menu.exec_(self.lst.mapToGlobal(pos))
        fp = os.path.join(dirpath(), it.text())
        if (
            ch == d
            and QMessageBox.question(
                self,
                "Löschen",
                f"{it.text()} löschen?",
                QMessageBox.Yes | QMessageBox.No,
            )
            == QMessageBox.Yes
        ):
            os.remove(fp)
            self.load()
        if ch == e:
            try:
                with open(fp, "r", encoding="utf-8") as f:
                    lines = f.read().splitlines()
                self.t.setText(lines[0][7:])
                self.g.setText(lines[1][7:])
                self.te.setText("\n".join(lines[3:]))
            except Exception as e:
                QMessageBox.critical(self, "Fehler", f"Öffnen fehlgeschlagen:\n{e}")
