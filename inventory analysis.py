#load the all the files
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
sales = pd.read_csv("data/SalesFINAL.csv")
purchases = pd.read_csv("data/PurchasesFINAL.csv")
begin_inv = pd.read_csv("data/BegInvFINAL.csv")
end_inv = pd.read_csv("data/EndInvFINAL.csv")
invoice = pd.read_csv("data/InvoicePurchases.csv")
purchase_prices = pd.read_csv("data/2017PurchasePricesDec.csv")


#inspect of structure
print(sales.head())

print(sales.columns)
print(sales.info())

#converting the dates

sales['SalesDate'] = pd.to_datetime(sales['SalesDate'])
purchases['PODate'] = pd.to_datetime(purchases['PODate'])
purchases['ReceivingDate'] = pd.to_datetime(purchases['ReceivingDate'])


#removing the missing values
sales = sales.dropna()
purchases = purchases.dropna()

#create revenue column

sales['SalesDate'] = pd.to_datetime(sales['SalesDate'], dayfirst=True)
purchases['PODate'] = pd.to_datetime(purchases['PODate'], dayfirst=True)
purchases['ReceivingDate'] = pd.to_datetime(purchases['ReceivingDate'], dayfirst=True)

sales['Revenue'] = sales['SalesQuantity'] * sales['SalesPrice']

#total revenue & monthly sales trend

total_revenue = sales['Revenue'].sum()
print("Total Revenue:", total_revenue)

#monthly
monthly_sales = sales.set_index('SalesDate')['Revenue'].resample('M').sum()

monthly_sales.plot()
plt.title("Monthly Revenue Trend")
plt.show()

#some top products
top_products = sales.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)

print(top_products)

#analysis like ABC 

abc = sales.groupby('Description')['Revenue'].sum().sort_values(ascending=False)

abc_df = abc.reset_index()
abc_df.columns = ['Product', 'Revenue']

abc_df['CumPct'] = abc_df['Revenue'].cumsum() / abc_df['Revenue'].sum()

def classify(x):
    if x <= 0.7:
        return 'A'
    elif x <= 0.9:
        return 'B'
    else:
        return 'C'

abc_df['Category'] = abc_df['CumPct'].apply(classify)

print(abc_df.head(20))

#lead time analysis

purchases['LeadTime'] = (purchases['ReceivingDate'] - purchases['PODate']).dt.days

supplier_lead = purchases.groupby('VendorName')['LeadTime'].mean().sort_values()

print(supplier_lead.head())

#inventory turnover

cogs = sales['Revenue'].sum()

avg_inventory = (begin_inv['onHand'].sum() + end_inv['onHand'].sum()) / 2

inventory_turnover = cogs / avg_inventory

print("Inventory Turnover:", inventory_turnover)

#EOQ
D = sales['SalesQuantity'].sum()
S = 500
H = 20

EOQ = np.sqrt((2 * D * S) / H)

print("EOQ:", EOQ)

#Re-order point

avg_daily_demand = sales['SalesQuantity'].mean()
lead_time_avg = purchases['LeadTime'].mean()

reorder_point = avg_daily_demand * lead_time_avg

print("Reorder Point:", reorder_point)

#Demand Forcecasting

from statsmodels.tsa.holtwinters import ExponentialSmoothing

monthly_qty = sales.set_index('SalesDate')['SalesQuantity'].resample('M').sum()

model = ExponentialSmoothing(monthly_qty, trend='add')
fit = model.fit()

forecast = fit.forecast(3)

print("Next 3 months forecast:")
print(forecast)

#saving outputs

#forcecast

forecast.to_csv("outputs/demand_forecast.csv", index=False)

#other output

abc_df.to_csv("outputs/abc_analysis.csv", index=False)
monthly_sales.to_csv("outputs/monthly_revenue.csv")
plt.savefig("outputs/monthly_trend.png")

