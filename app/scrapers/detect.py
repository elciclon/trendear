def is_inline_xbrl(html_path: str) -> bool:
    """This function checks if the given HTML file contains Inline XBRL tags."""
    with open(html_path, "r", encoding="utf-8") as f:
        head = f.read(50_000).lower()       # just 50 KB
    return any(tag in head
               for tag in ("xmlns:ix", "<ix:nonnumeric", "<ix:nonfraction"))