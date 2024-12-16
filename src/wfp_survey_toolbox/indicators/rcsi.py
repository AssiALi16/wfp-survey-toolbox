import pandas as pd

from ..core.base import Indicator
from ..core.constants import RCSI_COLUMNS, RCSI_THRESHOLDS
from ..validation.validators import (
    check_columns_exist,
    check_missing_values,
    check_numeric_columns,
    check_value_ranges,
)


class ReducedCopingStrategyIndex(Indicator):
    def __init__(self):
        super().__init__(
            name="Reduced Coping Strategy Index",
            description="Index measuring frequency and severity of food consumption behaviors due to food shortage",
        )

    def validate(self, df: pd.DataFrame) -> tuple[bool, str]:
        """
        Validate the input DataFrame for rCSI calculation.

        Args:
        - df (pd.DataFrame): Input DataFrame.

        Returns:
        - tuple[bool, str]: A tuple containing a boolean indicating validity and a message.

        Additional information:
            **Reference:**
                https://resources.vam.wfp.org/data-analysis/quantitative/food-security/reduced-coping-strategies-index

        """
        columns = list(RCSI_COLUMNS.keys())

        # Step 1: Check columns existence
        cols_exist, missing_cols = check_columns_exist(df, columns)
        if not cols_exist:
            return False, f"Missing required columns: {', '.join(missing_cols)}"

        # Step 2: Check missing values
        no_missing, cols_with_missing = check_missing_values(df, columns)
        if not no_missing:
            return (
                False,
                f"Missing values found in columns: {', '.join(cols_with_missing)}",
            )

        # Step 3: Check numeric type
        all_numeric, non_numeric_cols = check_numeric_columns(df, columns)
        if not all_numeric:
            return (
                False,
                f"Non-numeric values found in columns: {', '.join(non_numeric_cols)}",
            )

        # Step 4: Check value ranges (0-7 for days in a week)
        in_range, out_of_range_cols = check_value_ranges(df, columns)
        if not in_range:
            return (
                False,
                f"Values outside 0-7 range in columns: {', '.join(out_of_range_cols)}",
            )

        return True, "All validations passed successfully"

    def calculate(self, df: pd.DataFrame) -> pd.Series:
        """
        Calculate the Reduced Coping Strategy Index.

        The rCSI measures the frequency and severity of food consumption behaviors
        households engage in when facing food shortages in the previous 7 days.

        Args:
            df: Survey dataset with standard variable names

        Returns:
            A Pandas Series of the Reduced Coping Strategy Index scores

        Additional information:
            **Reference:**
                https://resources.vam.wfp.org/data-analysis/quantitative/food-security/reduced-coping-strategies-index
        """
        is_valid, message = self.validate(df)
        if not is_valid:
            print(f"\nError calculating rCSI:\n\n- {message}")
            return None

        return (
            df["rCSILessQlty"]
            + (df["rCSIBorrow"] * 2)
            + df["rCSIMealNb"]
            + df["rCSIMealSize"]
            + (df["rCSIMealAdult"] * 3)
        )

    def classify(self, scores: pd.Series) -> pd.Series:
        """
        Classify the rCSI scores into severity categories.
        This method can be implemented based on specific thresholds if needed.

        Args:
            scores (pd.Series): Series of rCSI scores

        Returns:
            pd.Series: Classified rCSI scores

        Additional information:
            **Reference:**
                https://resources.vam.wfp.org/data-analysis/quantitative/food-security/reduced-coping-strategies-index
        """

        thresholds = RCSI_THRESHOLDS["standard"]
        labels = ["Minimal", "Moderate", "Severe"]
        bins = [0] + thresholds + [float("inf")]
        return pd.cut(scores, bins=bins, labels=labels, right=False)
