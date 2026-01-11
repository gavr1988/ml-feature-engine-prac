import pandas as pd

# loading the data from the csv file
def load_data(filename='sales_data.csv'):
    print("loaded data...")
    try:
        df = pd.read_csv(filename)
        print(f"successfully loaded {len(df)} data!")
        return df
    except FileNotFoundError:
        print("Sales data not found")
        return pd.DataFrame(columns=['Day','Customers', 'Total_Sales','Top_Selling_Item'])

# now to detect the outlier 
# Will be using InterQuartile Ranges
# Need at least 4 data points to calculate the interquartile ranges (IQR)
def detect_outlier(df):
    print('detecting outlier')
    if len(df) < 4:
        return pd.DataFrame()
    Q1 = df['Total_Sales'].quantile(0.25)
    Q3 = df['Total_Sales'].quantile(0.75)
    IQR = Q3 - Q1
    upper_fence = Q3 + (1.5 * IQR)
    lower_fence = Q1 - (1.5 * IQR)
    outliers = df[(df['Total_Sales'] > upper_fence) | (df['Total_Sales'] < lower_fence)]
    print(outliers)
    return outliers

def show_report(df):
    outliers = detect_outlier(df)
    print(outliers)
    return outliers

def main():
    print("running app....")
    data = load_data()
    show_report(data)

main()