# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    #This code below reads the csv file
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data row
        for row in csvreader:
            data.append(row)
    return data

    #This function below save csv
def save_csv(csvpath, data, header= "N"):
    #Wriiting newline = "w" If there is a header, we would write row header, and if there is data the csvrows  writes the data
    with open(csvpath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        if header:
            csvwriter.writerow(header)
        csvwriter.writerows(data)

    #Finish the code
