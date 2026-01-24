import pandas as pd;


# file Read
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')
# print(df)   error bc of large excel file 

# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe()) 

# col1 = df[["ORDERNUMBER","QUANTITYORDERED","PRICEEACH"]]
# print(col1)

# Filtering
# col2 = df[df["SALES"] > 3000]
# print(col2)

# col3 = df.query("CITY == 'NYC' and SALES > 6000")
# print(col3)

# col4 = df["profit"] = df["SALES"] - df["MSRP"]
# print(col4)


# col5 = df.groupby("CITY")["SALES"].sum()
# print(col5)


# col6 = df.groupby(["CITY", "PRODUCTCODE"])["SALES"].agg(["count", "sum", "sum"])
# print(col6)



data = {
    "Country": ["Pakistan", "India", "USA", "UK", "China", "Italy", "Spain", "France", "Germany", "Brazil"],
    "Total_Cases": [1580000, 45000000, 105000000, 24000000, 9900000, 26000000, 14000000, 40000000, 38000000, 38000000],
    "Total_Deaths": [30000, 530000, 1150000, 220000, 120000, 190000, 120000, 170000, 170000, 700000],
    "Total_Recovered": [1540000, 44500000, 103000000, 23500000, 9850000, 25500000, 13800000, 39500000, 37500000, 37000000],
    "Active_Cases": [10000, 200000, 1500000, 300000, 5000, 200000, 80000, 300000, 200000, 300000],
    "New_Cases": [50, 120, 300, 90, 10, 70, 60, 110, 95, 130],
    "New_Deaths": [1, 2, 5, 3, 0, 2, 1, 2, 1, 4],
    "Tests_Performed": [30000000, 900000000, 1200000000, 500000000, 160000000, 300000000, 350000000, 450000000, 500000000, 600000000],
    "Population": [241000000, 1420000000, 331000000, 67000000, 1440000000, 60000000, 47000000, 65000000, 83000000, 215000000],
    "Vaccination_Rate_%": [75, 72, 81, 79, 92, 85, 88, 84, 86, 80]
}


data_frame = pd.DataFrame(data)
print(data_frame)
csv_file = data_frame.to_csv("covid_19.csv", index=False)
print(csv_file)