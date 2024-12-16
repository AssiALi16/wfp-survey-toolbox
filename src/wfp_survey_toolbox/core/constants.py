# FCS Constants
FCS_COLUMNS = {
    "FCSStap": 2,
    "FCSPulse": 3,
    "FCSVeg": 1,
    "FCSFruit": 1,
    "FCSPr": 4,
    "FCSDairy": 4,
    "FCSSugar": 0.5,
    "FCSFat": 0.5,
}

FCS_THRESHOLDS = {"standard": [21.5, 35.5], "high_sugar_oil": [28.5, 42.5]}

# RCSI Constants
RCSI_COLUMNS = {
    "rCSILessQlty": 1,
    "rCSIBorrow": 2,
    "rCSIMealNb": 1,
    "rCSIMealSize": 1,
    "rCSIMealAdult": 3,
}

RCSI_THRESHOLDS = {
    "standard": [4, 18.5],
}
