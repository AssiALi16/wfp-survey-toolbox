import pandas as pd

from ..core.base import Indicator
from ..core.constants.fcs_constants import FCS_COLUMNS, FCS_THRESHOLDS
from ..validation.validators import (
    check_columns_exist,
    check_missing_values,
    check_numeric_columns,
    check_value_ranges,
)


class FoodConsumptionScore(Indicator):
    def __init__(self):
        super().__init__(
            name="Food Consumption Score",
            description="Composite score based on dietary diversity, food consumption frequency, and relative nutritional value",
        )

    def validate(self, df: pd.DataFrame) -> tuple[bool, str]:
        """
        Validate the input DataFrame for FCS calculation.

        Args:
        - df (pd.DataFrame): Input DataFrame.

        Returns:
        - tuple[bool, str]: A tuple containing a boolean indicating validity and a message.

        Additional information:
            **Reference:**
                https://resources.vam.wfp.org/data-analysis/quantitative/food-security/food-consumption-score

        """
        columns = list(FCS_COLUMNS.keys())

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

        # Step 4: Check value ranges
        in_range, out_of_range_cols = check_value_ranges(df, columns)
        if not in_range:
            return (
                False,
                f"Values outside 0-7 range in columns: {', '.join(out_of_range_cols)}",
            )

        return True, "All validations passed successfully"

    def calculate(self, df: pd.DataFrame) -> pd.Series:
        """
        Compute the Food Consumption Score with standard weights and variable names.

        The Food Consumption Score (FCS) is the most commonly used food security indicator by WFP and partners.
        This indicator is a composite score based on households’ dietary diversity, food consumption frequency, and relative nutritional value of different food groups.
        The FCS is calculated by asking how often households consume food items from the 8 different food groups (plus condiments) during a 7-day reference period.

        Args:
            df: Survey dataset with standard variable names

        Returns:
            A Pandas Series of the Food Consumption Score

        Additional information:
            **Reference:**
                https://resources.vam.wfp.org/data-analysis/quantitative/food-security/food-consumption-score

        """
        is_valid, message = self.validate(df)
        if not is_valid:
            print(f"\nError calculating FCS:\n\n- {message}")
            return None
        return sum(df[col] * weight for col, weight in FCS_COLUMNS.items())

    def classify(self, scores: pd.Series, high_sugar_oil: bool = True) -> pd.Series:
        """
        Classify the Food Consumption Score (FCS) into three categories: Poor, Borderline, and Acceptable.

        Args:
            scores (pd.Series): Series of Food Consumption Scores.
            high_sugar_oil (bool, optional): Whether to use high sugar/oil thresholds. Defaults to True.

        Returns:
                A Pandas Series of the Food Consumption Score classification.

        Additional information:
            **Reference:**
                https://resources.vam.wfp.org/data-analysis/quantitative/food-security/food-consumption-score

        """
        thresholds = FCS_THRESHOLDS["high_sugar_oil" if high_sugar_oil else "standard"]
        labels = ["Poor", "Borderline", "Acceptable"]
        bins = [0] + thresholds + [float("inf")]
        return pd.cut(scores, bins=bins, labels=labels, right=False)
