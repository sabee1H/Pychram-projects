# Data Science Project: Handling Missing Data

This project focuses on handling missing data in a dataset using Python and the pandas library. The primary objective is to clean and impute missing values in both numeric and non-numeric columns in a CSV file. This is a common preprocessing task in data analysis that ensures the integrity of the dataset before conducting further analysis or machine learning tasks.

## Project Overview

The project loads a CSV file containing data, checks for missing values, and handles them by performing the following steps:
- Calculating the percentage of missing values for each column.
- Dropping columns with more than 50% missing values.
- Filling missing numeric values with the mean of the respective columns.
- Filling missing non-numeric values with the most frequent value (mode).

## Prerequisites

- Python 3.x
- pandas library

You can install the required library using pip:

```bash
pip install pandas
