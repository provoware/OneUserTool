import os
import json
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton,
    QLineEdit, QLabel, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt

from log_helper import log

FAV_PATH = os.path.join(os.path.dirname(__file__), 'Projekt', 'favoriten.json')


def load_favs():
    if not os.path.exists(FAV_PATH):
        os.makedirs(os.path.dirname(FAV_PATH), exist_ok=True)
        with open(FAV_PATH, 'w', encoding='utf-8') as f:
            json.dump([], f)
    with open(FAV_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_favs(data):
    with open(FAV_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


class HooklineFavoritenModul(QWidget):
    """Einfache Verwaltung von Hookline-Favoriten."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hookline-Favoriten')
        self.resize(400, 300)
        v = QVBoxLayout(self)

        self.search = QLineEdit(placeholderText='Suchen…')
        self.search.textChanged.connect(self.update_list)
        v.addWidget(self.search)

        self.lst = QListWidget()
        self.lst.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lst.customContextMenuRequested.connect(self.delete_selected)
        v.addWidget(self.lst)

        h = QHBoxLayout()
        self.input = QLineEdit(placeholderText='Neue Hookline')
        self.input.setToolTip('Text eingeben und Hinzufügen klicken')
        h.addWidget(self.input)
        btn_add = QPushButton('Hinzufügen', clicked=self.add)
        btn_add.setToolTip('Hookline zu den Favoriten hinzufügen')
        h.addWidget(btn_add)
        v.addLayout(h)

        h2 = QHBoxLayout()
        btn_exp = QPushButton('Exportieren', clicked=self.export)
        h2.addWidget(btn_exp)
        btn_del = QPushButton('Entfernen', clicked=self.delete_selected)
        h2.addWidget(btn_del)
        v.addLayout(h2)

        self.status = QLabel('Anzahl: 0')
        v.addWidget(self.status)

        self.favs = load_favs()
        self.update_list()

    # --- core actions -------------------------------------------------
    def update_list(self):
        term = self.search.text().lower()
        self.lst.clear()
        for line in self.favs:
            if term in line.lower():
                self.lst.addItem(line)
        self.status.setText(f'Anzahl: {self.lst.count()}')

    def add(self):
        text = self.input.text().strip()
        if not text:
            return
        if text not in self.favs:
            self.favs.append(text)
            save_favs(self.favs)
            log(f'Hookline hinzugefügt: {text}')
        self.input.clear()
        self.update_list()

    def delete_selected(self, *_):
        items = self.lst.selectedItems()
        if not items:
            return
        for it in items:
            self.favs.remove(it.text())
        save_favs(self.favs)
        log('Hookline(s) gelöscht')
        self.update_list()

    def export(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Exportieren', 'favoriten.txt', 'Text (*.txt)')
        if not fn:
            return
        try:
            with open(fn, 'w', encoding='utf-8') as f:
                for line in self.favs:
                    f.write(line + '\n')
            QMessageBox.information(self, 'Export', 'Favoriten gespeichert')
            log(f'Favoriten exportiert nach {fn}')
        except Exception as e:
            QMessageBox.warning(self, 'Fehler', str(e))

