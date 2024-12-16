"""Package containing functionality to analyse WFP surveys."""

import sys
from importlib import metadata as importlib_metadata

from .indicators import FoodConsumptionScore, ReducedCopingStrategyIndex


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
