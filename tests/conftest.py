from pathlib import Path

import pandas as pd
import pytest


@pytest.fixture(scope="session")
def data_dir() -> Path:
    # Path to the data folder within tests
    return Path(__file__).parent / "data"


@pytest.fixture(scope="session")
def cari_data(data_dir: Path) -> pd.DataFrame:
    # Sample CARI survey dataset
    df = pd.read_csv(data_dir / "CARI_Sample_Data.csv")
    return df


@pytest.fixture(scope="session")
def fcs_data(data_dir: Path) -> pd.DataFrame:
    # Sample CARI survey dataset
    df = pd.read_csv(data_dir / "FCS_Sample_Survey.csv")
    return df
