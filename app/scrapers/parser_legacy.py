from base_parser import EarningsParserStrategy


class LegacyEarningsParser(EarningsParserStrategy):
    def parse(self, filepath: str) -> dict:
        # lógica específica para HTML plano o XBRL antiguo
        return {"revenue": "...", "eps": "...", "net_income": "..."}
