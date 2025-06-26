# Version 0.1.0
import os, json
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QListWidget, QListWidgetItem, QMessageBox
)
from PyQt5.QtCore import Qt

def data_path():
    p = os.path.join(os.path.dirname(__file__), "Projekt", "todo_list.json")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if not os.path.exists(p):
        with open(p, "w", encoding="utf-8") as f:
            json.dump([], f)
    return p

def load_tasks():
    with open(data_path(), "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(data_path(), "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

class TodoModul(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo-Liste")
        self.resize(400, 360)
        v = QVBoxLayout(self)
        # Eingabezeile
        h = QHBoxLayout()
        self.input = QLineEdit()
        self.input.setPlaceholderText("Neue Aufgabe…")
        self.input.returnPressed.connect(self.add_task)
        h.addWidget(self.input)
        h.addWidget(QPushButton("Hinzufügen", clicked=self.add_task))
        v.addLayout(h)
        # Aufgabenliste
        self.lst = QListWidget()
        self.lst.itemChanged.connect(self.update_state)
        v.addWidget(self.lst)
        v.addWidget(QPushButton("Tipps", clicked=self.show_help))
        self.tasks = load_tasks()
        self.load_list()

    def load_list(self):
        self.lst.clear()
        for t in self.tasks:
            it = QListWidgetItem(t.get("text", ""))
            it.setFlags(it.flags() | Qt.ItemIsUserCheckable)
            it.setCheckState(Qt.Checked if t.get("done") else Qt.Unchecked)
            self.lst.addItem(it)

    def add_task(self):
        txt = self.input.text().strip()
        if not txt:
            return
        self.tasks.append({"text": txt, "done": False})
        self.input.clear()
        save_tasks(self.tasks)
        self.load_list()

    def update_state(self, item):
        idx = self.lst.row(item)
        if 0 <= idx < len(self.tasks):
            self.tasks[idx]["done"] = item.checkState() == Qt.Checked
            save_tasks(self.tasks)

    def show_help(self):
        QMessageBox.information(self, "Tipps – Todo-Liste",
            "• Halte Aufgaben kurz und prägnant.\n"
            "• Teile große Vorhaben in kleine Schritte.\n"
            "• Überprüfe erledigte Punkte regelmäßig und passe die Liste an.")

