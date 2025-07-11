from abc import ABC, abstractmethod
from typing import Any


class EarningsParserStrategy(ABC):
    @abstractmethod
    def parse(self, filepath: str) -> dict[str, Any]:
        """Parses a financial statement and returns a dictionary with key earnings data."""
        pass
