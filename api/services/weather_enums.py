from enum import Enum


class TemperatureRangeEnum(str, Enum):
    temp1 = "less than 12"
    temp2 = "Greater than 12 and less than 20"
    temp3 = "Greater 20 and less than 30"
    temp4 = "Greater than 30"
