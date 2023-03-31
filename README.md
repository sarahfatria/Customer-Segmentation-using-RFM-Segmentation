# Customer-Segmentation-using-RFM-Segmentation
This code demonstrates RFM (Recency, Frequency, Monetary) segmentation technique, which is widely used in marketing and customer relationship management (CRM).

## Dataset
The dataset used in this project is from [Online Retail II Data Set](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)

## Step by step
- **Data Exploration**: This is done through printing the shape of the DataFrame, as well as its summary statistics using the 'describe()' function, isnull(), and dropna().
- **Data Cleaning**: The code removes the rows containing returns by selecting only the rows that do not contain the letter 'C' in the 'Invoice' column using the '~' operator. It then adds a new column 'TotalPrice' to the DataFrame by multiplying the 'Quantity' and 'Price' columns.
- **RFM Metrics**: Created by grouping the DataFrame by 'Customer ID' and calculating the recency, frequency, and monetary values for each customer.
- **RFM Scores and Segments**: Assigns RFM scores to each customer by dividing each metric into five equal parts or quintiles, then mapping the RFM scores to meaningful segment names.

## Conclusion
The code groups the customers by segment and calculates the mean and count for each segment. This information can be used to analyze the segments and formulate marketing strategies.
