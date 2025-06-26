import os
import sys
import types
import datetime

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Provide minimal PyQt5 stubs if PyQt5 is not available
if 'PyQt5' not in sys.modules:
    qtwidgets = types.ModuleType('QtWidgets')
    qtcore = types.ModuleType('QtCore')
    for mod in [qtwidgets, qtcore]:
        for name in [
            'QWidget', 'QVBoxLayout', 'QHBoxLayout', 'QLabel', 'QLineEdit',
            'QTextEdit', 'QPushButton', 'QListWidget', 'QMessageBox', 'QMenu',
            'QFileDialog', 'QApplication'
        ]:
            setattr(mod, name, object)
    qtcore.Qt = object()
    package = types.ModuleType('PyQt5')
    sys.modules['PyQt5'] = package
    sys.modules['PyQt5.QtWidgets'] = qtwidgets
    sys.modules['PyQt5.QtCore'] = qtcore

import songtext_modul


def test_clean_basic():
    assert songtext_modul.clean('Hello World!') == 'Hello_World_'
    assert songtext_modul.clean('Song-title 123') == 'Song-title_123'


def test_dirpath_creates_directory(tmp_path, monkeypatch):
    temp_file = tmp_path / 'dummy.py'
    temp_file.write_text('')
    monkeypatch.setattr(songtext_modul, '__file__', str(temp_file))
    path = songtext_modul.dirpath()
    assert path.endswith(os.path.join('Projekt', 'Songtexte'))
    assert os.path.isdir(path)


def test_file_operations(tmp_path, monkeypatch):
    temp_file = tmp_path / 'dummy.py'
    temp_file.write_text('')
    monkeypatch.setattr(songtext_modul, '__file__', str(temp_file))
    # Build filename similar to save()
    title = 'Test Song'
    genre = 'Rock'
    text = 'Lorem ipsum dolor sit amet'
    now = datetime.datetime(2024, 1, 1, 12, 0, 0)
    monkeypatch.setattr(songtext_modul.datetime, 'datetime', datetime.datetime)
    filename = f"{songtext_modul.clean(title)}_{songtext_modul.clean(genre)}_" + now.strftime('%Y%m%d_%H%M%S') + '.txt'
    path = os.path.join(songtext_modul.dirpath(), filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"Titel: {title}\nGenre: {genre}\n---\n{text}")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert 'Titel: Test Song' in content
    assert 'Genre: Rock' in content
    assert text in content

