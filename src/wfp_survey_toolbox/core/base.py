from typing import Optional

import pandas as pd


class Indicator:
    """Base class for all food security indicators"""

    def __init__(self, name: str, description: Optional[str] = None):
        self.name = name
        self.description = description

    def validate(self, df: pd.DataFrame) -> bool:
        raise NotImplementedError

    def calculate(self, df: pd.DataFrame) -> pd.Series:
        raise NotImplementedError
