class DummyApp:
    def __init__(self):
        self.stylesheet = None

    def setStyleSheet(self, style):
        self.stylesheet = style


from design_manager import apply_stylesheet


def test_apply_stylesheet_dark():
    app = DummyApp()
    apply_stylesheet(app, theme="dark", fontsize=12)
    assert "background: #23272E" in app.stylesheet
    assert "font-size: 12px" in app.stylesheet
