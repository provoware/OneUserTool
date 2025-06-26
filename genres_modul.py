# Version 0.1.8
import os, json, shutil
from data_utils import genres_profile_path
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QListWidget, QMessageBox, QComboBox,
    QInputDialog, QMenu, QFileDialog
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

def load_profiles():
    path = genres_profile_path()
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"Favoriten":[]}, f)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f) or {"Favoriten":[]}

def save_profiles(d):
    with open(genres_profile_path(), "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

class GenresModul(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genre-Archiv")
        self.setMinimumSize(480,400)
        v = QVBoxLayout(self)
        # Profil-Auswahl
        h1 = QHBoxLayout()
        self.cb = QComboBox()
        self.cb.currentTextChanged.connect(self.load_list)
        btn_new = QPushButton(QIcon.fromTheme("list-add"), "")
        btn_new.clicked.connect(self.new_profile)
        h1.addWidget(QLabel("Profil:"))
        h1.addWidget(self.cb)
        h1.addWidget(btn_new)
        # Suche + Eingabe
        h2 = QHBoxLayout()
        self.search = QLineEdit(placeholderText="Schnellsuche…")
        self.search.textChanged.connect(self.load_list)
        self.input = QLineEdit(placeholderText="Genres, Komma-getrennt")
        # ENTER-Taste auslösen wie Klick auf „Hinzufügen“
        self.input.returnPressed.connect(self.add_genres)
        btn_add = QPushButton("Hinzufügen")
        btn_add.clicked.connect(self.add_genres)
        btn_help = QPushButton("?")
        btn_help.clicked.connect(self.show_help)
        for w in (self.search, self.input, btn_add, btn_help):
            h2.addWidget(w)
        # Liste + Status
        self.lst = QListWidget()
        self.lst.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lst.customContextMenuRequested.connect(self.ctx_menu)
        self.lbl = QLabel("Anzahl: 0")
        # Export/Import/Backup
        h3 = QHBoxLayout()
        for txt, fn in [("Export", self.export),
                        ("Import", self.import_),
                        ("Backup", self.backup)]:
            h3.addWidget(QPushButton(txt, clicked=fn))
        # Zusammensetzen
        v.addLayout(h1)
        v.addLayout(h2)
        v.addWidget(self.lst)
        v.addWidget(self.lbl)
        v.addLayout(h3)
        # Daten initialisieren
        self.profiles = load_profiles()
        # ComboBox alphabetisch sortieren
        for name in sorted(self.profiles.keys(), key=str.lower):
            self.cb.addItem(name)
        self.cb.setCurrentText("Favoriten")
        self.load_list()

    def load_list(self):
        prof = self.cb.currentText()
        arr = self.profiles.get(prof, [])
        filt = self.search.text().lower()
        self.lst.clear()
        for g in sorted(arr, key=str.lower):
            if filt in g.lower():
                self.lst.addItem(g)
        self.lbl.setText(f"Anzahl: {self.lst.count()} von {len(arr)}")

    def new_profile(self):
        name, ok = QInputDialog.getText(self, "Neues Profil", "Name:")
        if ok and name and name not in self.profiles:
            self.profiles[name] = []
            save_profiles(self.profiles)
            self.cb.addItem(name)
            self.cb.setCurrentText(name)

    def add_genres(self):
        txt = self.input.text().strip()
        if not txt:
            return QMessageBox.warning(self, "Fehler", "Bitte Genres eingeben")
        arr = [g.strip() for g in txt.split(",") if g.strip()]
        prof = self.cb.currentText()
        for g in arr:
            if g not in self.profiles[prof]:
                self.profiles[prof].append(g)
        # sortiere alphabetisch
        self.profiles[prof] = sorted(self.profiles[prof], key=str.lower)
        save_profiles(self.profiles)
        self.input.clear()
        self.load_list()
        # kopieren
        QApplication.clipboard().setText(", ".join(arr))
        QMessageBox.information(self, "Info", f"{len(arr)} Genre(s) hinzugefügt & kopiert")

    def ctx_menu(self, pos):
        it = self.lst.itemAt(pos)
        if not it: return
        m = QMenu(self)
        e = m.addAction("Bearbeiten")
        d = m.addAction("Löschen")
        a = m.exec_(self.lst.mapToGlobal(pos))
        if a == e: self.edit(it)
        if a == d: self.delete(it)

    def edit(self, it):
        old = it.text()
        new, ok = QInputDialog.getText(self, "Bearbeiten", "Neu:", text=old)
        prof = self.cb.currentText()
        if ok and new and new not in self.profiles[prof]:
            idx = self.profiles[prof].index(old)
            self.profiles[prof][idx] = new
            self.profiles[prof].sort(key=str.lower)
            save_profiles(self.profiles)
            self.load_list()

    def delete(self, it):
        if QMessageBox.question(self, "Löschen", f"{it.text()} löschen?",
                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
            prof = self.cb.currentText()
            self.profiles[prof].remove(it.text())
            save_profiles(self.profiles)
            self.load_list()

    def export(self):
        fn,_ = QFileDialog.getSaveFileName(self, "Export", "genres.json", "JSON (*.json)")
        if fn:
            with open(fn, "w", encoding="utf-8") as f:
                json.dump(self.profiles, f, ensure_ascii=False, indent=2)
            QMessageBox.information(self, "Export", "Erfolgreich exportiert")

    def import_(self):
        fn,_ = QFileDialog.getOpenFileName(self, "Import", "", "JSON (*.json)")
        if fn:
            try:
                data = json.load(open(fn, "r", encoding="utf-8"))
                if isinstance(data, dict):
                    self.profiles = data
                    save_profiles(data)
                    self.cb.clear()
                    for name in sorted(data.keys(), key=str.lower):
                        self.cb.addItem(name)
                    self.cb.setCurrentText(list(data.keys())[0])
                    self.load_list()
                    QMessageBox.information(self, "Import", "Erfolgreich importiert")
            except Exception:
                QMessageBox.warning(self, "Fehler", "Import fehlgeschlagen")

    def backup(self):
        d = QFileDialog.getExistingDirectory(self, "Backup-Ordner wählen")
        if d:
            dst = os.path.join(d, "OneUserTool_Backup")
            shutil.rmtree(dst, ignore_errors=True)
            shutil.copytree(os.path.join(os.path.dirname(__file__), "Projekt"), dst)
            QMessageBox.information(self, "Backup", f"Backup in: {dst}")

    def show_help(self):
        QMessageBox.information(self, "Hilfe – Genre-Archiv",
            "• Genres eingeben, ENTER = hinzufügen\n"
            "• Rechtsklick auf Eintrag = Bearbeiten/Löschen\n"
            "• Liste wird alphabetisch sortiert\n"
            "• Export/Import/Backup per Knopf"
        )
