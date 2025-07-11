from base_parser import EarningsParserStrategy

class InlineXBRLEarningsParser(EarningsParserStrategy):
    def parse(self, filepath: str) -> dict:
        # lógica usando BeautifulSoup o lxml para iXBRL
        return {
            "revenue": "...",
            "eps": "...",
            "net_income": "..."
        }