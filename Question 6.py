# Question 6 - Crime levels and comparing unemployment rates between the groups.
#==================================================================================

import pandas as pd
import numpy as np

def convert_csv_as_dataframe(crime_file):
    # Converts the crime csv as a dataframe.
    crime_dataframe = pd.read_csv(crime_file)

    return crime_dataframe


def create_column_risk(crime_dataframe):
    # Creates a new column in the dataframe called "risk", with risk being high crime or low crime.
    crime_dataframe["Risk"] = np.where(crime_dataframe["ViolentCrimesPerPop"] >= 0.5, "HighCrime", "LowCrime")


def group_data_by_risk(crime_dataframe_with_risk):
    # Groups the data by the risk column, with the average value for the percent of unemployed for each risk group.
    grouped_crime_dataframe = crime_dataframe_with_risk.groupby("Risk").agg({
        "PctUnemployed": "mean",
    }).reset_index()

    return grouped_crime_dataframe

def print_highcrime_lowcrime_unemployment_averages(risk_crime_dataframe):
    # Prints out the unemployment averages for each risk group.
    print(f"Unemployment rate for high crime individuals: {risk_crime_dataframe["PctUnemployed"][0]}")
    print(f"Unemployment rate for low crime individuals: {risk_crime_dataframe["PctUnemployed"][1]}")

# ===================================================================================

def main():
    with open("crime.csv", "r") as crime_information_file:

        crime_information_dataframe = convert_csv_as_dataframe(crime_information_file)

        create_column_risk(crime_information_dataframe)

        risk_crime_dataframe = group_data_by_risk(crime_information_dataframe)

        print_highcrime_lowcrime_unemployment_averages(risk_crime_dataframe)


main()