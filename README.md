# OneUserTool

OneUserTool ist eine kleine Desktop-Anwendung auf Basis von PyQt5. Sie verwaltet Songtexte, Genre-Profile und erzeugt zufällige Genre-Listen.

## Einrichtung

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## Debian-Paket bauen

Eine einfache Paketierung ist möglich. Legen Sie dazu einen Ordner `debian_pkg` an, kopieren Sie den Projektinhalt hinein und erstellen Sie im Unterordner `DEBIAN` eine `control`-Datei. Mit `dpkg-deb --build debian_pkg` entsteht ein installierbares `.deb`-Paket.

Weitere Hinweise finden Sie im Code und in den Shellskripten.
