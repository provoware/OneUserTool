# Version 0.1.9
import os
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QFileDialog, QMessageBox
)

class DateiumbenennungModul(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datei umbenennen")
        self.filepath = ""
        v = QVBoxLayout(self)

        self.btn_choose = QPushButton("Datei wählen")
        self.btn_choose.clicked.connect(self.choose_file)
        v.addWidget(self.btn_choose)

        self.lbl = QLabel("Keine Datei gewählt")
        v.addWidget(self.lbl)

        v.addWidget(QLabel("Neuer Dateiname:"))
        self.new_name = QLineEdit()
        v.addWidget(self.new_name)

        self.btn_rename = QPushButton("Umbenennen")
        self.btn_rename.clicked.connect(self.rename)
        v.addWidget(self.btn_rename)

    def choose_file(self):
        fn, _ = QFileDialog.getOpenFileName(self, "Datei wählen")
        if fn:
            self.filepath = fn
            self.lbl.setText(fn)

    def rename(self):
        if not self.filepath:
            return QMessageBox.warning(self, "Fehler", "Keine Datei gewählt")
        new = self.new_name.text().strip()
        if not new:
            return QMessageBox.warning(self, "Fehler", "Neuer Name fehlt")
        new_path = os.path.join(os.path.dirname(self.filepath), new)
        try:
            os.rename(self.filepath, new_path)
            QMessageBox.information(self, "Erfolg", "Datei umbenannt")
            self.filepath = new_path
            self.lbl.setText(new_path)
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Umbenennen fehlgeschlagen:\n{e}")
