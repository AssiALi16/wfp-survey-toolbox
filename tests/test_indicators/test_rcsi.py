import pandas as pd

from wfp_survey_toolbox import ReducedCopingStrategyIndex


def test_rcsi_calculation():
    test_data = pd.DataFrame(
        {
            "rCSILessQlty": [7, 3, 0],  # weight 1
            "rCSIBorrow": [4, 1, 0],  # weight 2
            "rCSIMealNb": [7, 0, 0],  # weight 1
            "rCSIMealSize": [2, 1, 0],  # weight 1
            "rCSIMealAdult": [7, 2, 1],  # weight 3
        }
    )

    rcsi = ReducedCopingStrategyIndex()
    result = rcsi.calculate(test_data)

    expected_scores = [45.0, 12.0, 3.0]

    # Print comparison of results
    print("\rCSI Calculation Test Results:")
    print("Calculated Scores:", list(result))
    print("Expected Scores:", expected_scores)
    print(
        "Scores Match:", all(abs(a - b) < 0.01 for a, b in zip(result, expected_scores))
    )


def test_fcs_classification():
    # Create test cases with edge values
    test_data = pd.DataFrame(
        {
            "rCSI": [
                0,  # Minimal
                3,  # Minimal
                4,  # Moderate
                18,  # Moderate
                18.5,  # Severe
                19,  # Severe
                56,  # Severe
            ]
        }
    )

    rcsi = ReducedCopingStrategyIndex()

    # Test standard thresholds
    standard_results = rcsi.classify(test_data["rCSI"])
    expected_standard = [
        "Minimal",
        "Minimal",
        "Moderate",
        "Moderate",
        "Severe",
        "Severe",
        "Severe",
    ]

    # Print results comparison
    print("\nrCSI Classification Test Results:")
    print("rCSI Values:", test_data["rCSI"].tolist())
    print("Calculated:", list(standard_results))
    print("Expected:", expected_standard)
    print("Classifications Match:", list(standard_results) == expected_standard)


test_rcsi_calculation()
test_fcs_classification()
