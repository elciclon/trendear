from detect import is_inline_xbrl
from base_parser import EarningsParserStrategy
from parser_inline_xbrl import InlineXBRLEarningsParser
from parser_legacy import LegacyEarningsParser


class EarningsParser:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.strategy = self._select_strategy()

    def _select_strategy(self) -> EarningsParserStrategy:
        if is_inline_xbrl(self.filepath):
            return InlineXBRLEarningsParser()
        else:
            return LegacyEarningsParser()

    def extract(self) -> dict:
        return self.strategy.parse(self.filepath)
