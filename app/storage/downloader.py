import os
import shutil
from sec_edgar_downloader import Downloader


def fetch_and_store_10k_reports(ticker: str, count: int):
    base_dir = os.path.join("data", "sec-edgar-filings")
    company_dir = os.path.join(base_dir, ticker, "10-K")

    # Downlad the 10-K reports
    dl = Downloader("Trendear", "adrianfernandezfazio@gmail.com", os.path.join("data"))
    dl.get("10-K", ticker, limit=count)


# Ejemplo de uso:
if __name__ == "__main__":
    fetch_and_store_10k_reports("GOOGL", count=10)
