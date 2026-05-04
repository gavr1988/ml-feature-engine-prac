# ML Feature Engineering Practice

Small practice project for loading sales data with pandas and identifying outliers in Total_Sales using the Interquartile Range (IQR) method.

## Project Files

- run.py: Main script that loads data and prints outliers.
- sales_data.csv: Input dataset used by the script.
- .gitignore: Ignores local environment and generated files.

## Requirements

- Python 3.9+
- pandas

## Setup

1. Create and activate a virtual environment.

	python3 -m venv venv
	source venv/bin/activate

2. Install dependencies.

	pip install pandas

## Run

From the project root directory:

python run.py

## What the Script Does

1. Loads sales records from sales_data.csv.
2. Computes Q1, Q3, and IQR for Total_Sales.
3. Flags rows outside the IQR fences as outliers.
4. Prints the outlier rows as a quick report.

## Notes

- If sales_data.csv is missing, the script falls back to an empty DataFrame with expected columns.
- At least 4 rows are required for IQR-based outlier detection.
