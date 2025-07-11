import os

from sec_edgar_downloader import Downloader


def fetch_and_store_10k_reports(ticker: str, count: int):
    """Downloads and stores 10-K reports for a given ticker.

    Args:
        ticker (str): company ticker symbol.
        count (int): amount of reports to download.
    """

    dl = Downloader("Trendear", "adrianfernandezfazio@gmail.com", os.path.join("data"))
    dl.get("10-K", ticker, limit=count)
