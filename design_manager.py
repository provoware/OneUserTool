# Version 0.1.7
"""Hilfsfunktionen zur Anwendung eines konsistenten Qt-Designs."""
from PyQt5.QtWidgets import QApplication
def apply_stylesheet(app, theme="dark", fontsize=16):
    """Setze ein einfaches Stylesheet für die angegebene QApplication."""
    if theme=="dark":
        bg,fg,inp="#23272E","#f2f2f2","#2b2f36"
    elif theme=="light":
        bg,fg,inp="#f5f5f5","#1a1a1a","#ffffff"
    elif theme=="highcontrast":
        bg,fg,inp="#000000","#FFFF00","#101010"; fontsize+=2
    else:
        bg,fg,inp="#1c2233","#e3f2fd","#212c44"
    style = f"""
    QWidget {{ background: {bg}; color: {fg}; font-size: {fontsize}px; }}
    QPushButton {{ background: {inp}; color: {fg}; border-radius: 6px; padding: 6px; }}
    QLineEdit,QTextEdit,QListWidget {{ background: {inp}; color: {fg}; border-radius: 4px; }}
    """
    app.setStyleSheet(style)
