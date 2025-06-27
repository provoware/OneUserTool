from songtext_modul import clean


def test_clean_replaces_special_chars():
    assert clean('Hello World!') == 'Hello_World_'


def test_clean_keeps_alnum_and_dash():
    assert clean('abc-123') == 'abc-123'
