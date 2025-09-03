from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# --- Step 1: Connect to MySQL ---
engine = create_engine("mysql+pymysql://root:Bhuvan2004%40@localhost/retail_analytics_new")

try:
    conn = engine.connect()
    print("Connected successfully!")
except Exception as e:
    print("Connection Error:", e)
    exit()

# --- Step 2: Load data ---
df = pd.read_sql("SELECT * FROM FACT_SALES_NEW", conn, parse_dates=["Date"])
conn.close()  # Close connection after loading

# --- Step 3: Data Cleaning & EDA ---

# Convert date to datetime (if not already)
df['Date'] = pd.to_datetime(df['Date'])

# Add Month column
df['Month'] = df['Date'].dt.month

# --- Visualizations ---

# 1. Sales over time (line chart)
df.groupby('Date')['Total Amount'].sum().plot()
plt.title("Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Amount")
plt.show()

# 2. Category contribution (bar chart)
df.groupby('Product Category')['Total Amount'].sum().plot(kind='bar')
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Amount")
plt.show()

# 3. Age distribution (histogram)
df['Age'].hist()
plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# 4. Gender split (pie chart)
df['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Split of Customers")
plt.show()
df.groupby('Product Category')['Total Amount'].sum().plot(kind='bar')
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Amount")
plt.show()
# First look at the data
print(df.head())        # first 5 rows
print(df.info())        # column types & nulls
print(df.describe())    # summary stats for numeric columns
print(df.isnull().sum())  # missing values check
df['Total Amount'] = df['Total Amount'].fillna(0)
# --- Step 4: Feature Engineering ---

# Add Year column
df['Year'] = df['Date'].dt.year

# Create Age Groups
df['AgeGroup'] = pd.cut(
    df['Age'],
    bins=[0, 18, 30, 45, 60, 100],
    labels=['Teen', 'Young Adult', 'Adult', 'Middle Aged', 'Senior']
)

# Monthly Sales by Category
monthly_sales = df.groupby(['Year', 'Month', 'Product Category'])['Total Amount'].sum().reset_index()

# Sales by Age Group
age_group_sales = df.groupby('AgeGroup')['Total Amount'].sum().reset_index()

# Optional: preview
print("\nMonthly Sales by Category:")
print(monthly_sales.head())
print("\nSales by Age Group:")
print(age_group_sales)

# --- Step 5: Export for Excel/Power BI ---

monthly_sales.to_csv("monthly_sales.csv", index=False)
age_group_sales.to_csv("age_group_sales.csv", index=False)
df.to_csv("cleaned_sales_data.csv", index=False)

print("\n✅ Feature engineering complete. CSV files ready for Excel or Power BI.")
# Export to CSV for Excel / Power BI
monthly_sales.to_csv("monthly_sales.csv", index=False)
age_group_sales.to_csv("age_group_sales.csv", index=False)
df.to_csv("cleaned_sales_data.csv", index=False)

print("\n✅ Data exported to CSV for Excel/Power BI analysis.")
print("Total Sales:", df['Total Amount'].sum())
print("Average Sale Value:", df['Total Amount'].mean())
print("Unique Customers:", df['Customer ID'].nunique())
print("Top Categories:\n", df.groupby("Product Category")['Total Amount'].sum().sort_values(ascending=False).head())
monthly_sales = df.groupby(['Month', 'Product Category'])['Total Amount'].sum().reset_index()
monthly_sales.to_csv("monthly_sales.csv", index=False)
print("Monthly sales CSV exported!")
from statsmodels.tsa.arima.model import ARIMA

forecast_dfs = []

for category in df['Product Category'].unique():
    cat_data = df[df['Product Category'] == category].groupby('Month')['Total Amount'].sum()
    
    # Fit ARIMA model (simple example)
    model = ARIMA(cat_data, order=(1,1,1))
    model_fit = model.fit()
    
    # Forecast next 3 months
    forecast = model_fit.forecast(steps=3)
    
    # Prepare DataFrame
    forecast_df = pd.DataFrame({
        'Month': [13, 14, 15],  # example future months
        'Product Category': category,
        'Forecasted Sales': forecast.values
    })
    
    forecast_dfs.append(forecast_df)

# Combine all categories
forecast_output = pd.concat(forecast_dfs)
forecast_output.to_csv("forecast_output.csv", index=False)
print("Forecast CSV created!")

