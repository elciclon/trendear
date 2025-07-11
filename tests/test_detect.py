import tempfile
import os
from app.scrapers.detect import is_inline_xbrl


def test_is_inline_xbrl_true():
    html = "<html><head><ix:nonnumeric></ix:nonnumeric></head></html>"
    with tempfile.NamedTemporaryFile("w+", suffix=".html", delete=False) as f:
        f.write(html)
        f.flush()
        path: str = f.name
        assert is_inline_xbrl(path) is True
        os.remove(path)


def test_is_inline_xbrl_false():
    html = "<html><head><title>No XBRL</title></head></html>"
    with tempfile.NamedTemporaryFile("w+", suffix=".html", delete=False) as f:
        f.write(html)
        f.flush()
        path: str = f.name
        assert is_inline_xbrl(path) is False
        os.remove(path)
