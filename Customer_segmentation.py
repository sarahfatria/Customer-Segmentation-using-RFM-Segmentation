import datetime as dt
import pandas as pd

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Read in the data and create a copy
df = pd.read_excel("datasets/online_retail_II.xlsx", sheet_name="Year 2010-2011")
df = df.copy()

# Initial data exploration
df.head()
df.shape
df.describe().T

# Handle missing values
df.isnull().sum()
df.dropna(inplace=True)
df.shape

# Remove canceled orders
df = df[~df["Invoice"].str.contains("C", na=False)]

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["Price"]

# Calculate RFM scores
today_date = dt.datetime(2011, 12, 11)

rfm = df.groupby("Customer ID").agg({
    "InvoiceDate": lambda x: (today_date - x.max()).days,
    "Invoice": "nunique",
    "TotalPrice": "sum"
})

rfm.columns = ["recency", "frequency", "monetary"]
rfm = rfm[rfm["monetary"] > 0]

rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])
rfm["RFM_SCORE"] = (rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str))

# Map RFM scores to segments
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm["segment"] = rfm["RFM_SCORE"].replace(seg_map, regex=True)

# Group by segment and calculate means and counts
rfm.groupby("segment").agg(["mean", "count"])
