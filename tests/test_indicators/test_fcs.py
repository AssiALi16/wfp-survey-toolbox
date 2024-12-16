import pandas as pd

from wfp_survey_toolbox import FoodConsumptionScore


def test_fcs_calculation():
    test_data = pd.DataFrame(
        {
            "FCSStap": [7, 3, 0],  # weight 2
            "FCSPulse": [4, 1, 0],  # weight 3
            "FCSDairy": [7, 0, 0],  # weight 4
            "FCSPr": [2, 1, 0],  # weight 4
            "FCSVeg": [7, 3, 1],  # weight 1
            "FCSFruit": [3, 0, 0],  # weight 1
            "FCSFat": [7, 2, 1],  # weight 0.5
            "FCSSugar": [7, 4, 0],  # weight 0.5
        }
    )

    fcs = FoodConsumptionScore()
    result = fcs.calculate(test_data)

    expected_scores = [79.0, 19.0, 1.5]

    # Print comparison of results
    print("\nFCS Calculation Test Results:")
    print("Calculated Scores:", list(result))
    print("Expected Scores:", expected_scores)
    print(
        "Scores Match:", all(abs(a - b) < 0.01 for a, b in zip(result, expected_scores))
    )


def test_fcs_classification():
    # Create test cases with edge values
    test_data = pd.DataFrame(
        {
            "FCS": [
                0,  # Poor (both)
                21,  # Poor (both)
                21.5,  # Borderline (standard)
                28,  # Poor (adjusted)
                28.5,  # Borderline (adjusted)
                35,  # Borderline (standard)
                35.5,  # Acceptable (standard)
                42,  # Borderline (adjusted)
                42.5,  # Acceptable (adjusted)
                112,  # Acceptable (both)
            ]
        }
    )

    fcs = FoodConsumptionScore()

    # Test standard thresholds
    standard_results = fcs.classify(test_data["FCS"], high_sugar_oil=False)
    expected_standard = [
        "Poor",
        "Poor",
        "Borderline",
        "Borderline",
        "Borderline",
        "Borderline",
        "Acceptable",
        "Acceptable",
        "Acceptable",
        "Acceptable",
    ]

    # Test adjusted thresholds - High Oil & Sugar Consumption
    adjusted_results = fcs.classify(test_data["FCS"], high_sugar_oil=True)
    expected_adjusted = [
        "Poor",
        "Poor",
        "Poor",
        "Poor",
        "Borderline",
        "Borderline",
        "Borderline",
        "Borderline",
        "Acceptable",
        "Acceptable",
    ]

    # Print results comparison
    print("\nFCS Classification Test Results:")
    print("\nStandard Thresholds:")
    print("FCS Values:", test_data["FCS"].tolist())
    print("Calculated:", list(standard_results))
    print("Expected:", expected_standard)
    print("Classifications Match:", list(standard_results) == expected_standard)

    print("\nAdjusted Thresholds - High Sugar & Oil Consumption:")
    print("FCS Values:", test_data["FCS"].tolist())
    print("Calculated:", list(adjusted_results))
    print("Expected:", expected_adjusted)
    print("Classifications Match:", list(adjusted_results) == expected_adjusted)


test_fcs_calculation()
test_fcs_classification()
