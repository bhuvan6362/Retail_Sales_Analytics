# Retail Sales Analytics Project

## 1. Project Overview
This project demonstrates **end-to-end retail sales analysis** using Python, MySQL, Excel, and Power BI.  
The goal is to provide business insights on sales trends, customer demographics, top-selling products, and forecasting inventory needs.

Key objectives:
- Analyze sales by category, month, and customer demographics
- Perform feature engineering and data cleaning
- Visualize trends and KPIs in Excel and Power BI dashboards
- Forecast future sales for inventory management

---

## 2. Tech Stack
- **Python** – Pandas, Matplotlib, Statsmodels (ARIMA for forecasting)
- **MySQL** – Store raw sales data and queries
- **Excel** – PivotTables, charts, dashboards
- **Power BI** – Interactive dashboards and KPIs
- **CSV** – Intermediate data export between Python, Excel, and Power BI

---

## 3. Dataset
The main dataset `FACT_SALES_NEW` includes the following columns:
- `Transaction ID` – Unique ID for each sale
- `Date` – Transaction date
- `Customer ID` – Unique customer identifier
- `Gender` – Customer gender
- `Age` – Customer age
- `Product Category` – Product category
- `Quantity` – Quantity sold
- `Price per Unit` – Unit price
- `Total Amount` – Total transaction value

Additional CSV outputs:
- `monthly_sales.csv` – Sales by month and category
- `age_group_sales.csv` – Sales by customer age groups
- `forecast_output.csv` – Forecasted sales for upcoming months

---

## 4. Project Steps

### Step 1 – Load Data
- Connect Python to MySQL
- Load sales data from `FACT_SALES_NEW` table

### Step 2 – Data Cleaning & EDA
- Convert date column to datetime
- Handle missing values (`fillna`) and remove duplicates
- Basic statistics and charts: line chart for sales trends, bar chart for category contribution, histogram for age, pie chart for gender

### Step 3 – Feature Engineering
- Extract `Month` and `Year` from Date
- Create `AgeGroup` buckets
- Summarize monthly sales by category and age group

### Step 4 – Export Data
- Export cleaned and feature-engineered tables as CSV files:
  - `cleaned_sales_data.csv`
  - `monthly_sales.csv`
  - `age_group_sales.csv`
  - `forecast_output.csv` (ARIMA forecasting)

### Step 5 – Excel Dashboards
- Load CSVs → PivotTables & charts
  - Total Sales by Month → Line Chart
  - Sales by Product Category → Bar Chart
  - Sales by Age Group → Column Chart
  - Gender Split → Pie Chart
- Add KPIs: Total Sales, Average Order Value, Unique Customers
- Add slicers to filter data dynamically

### Step 6 – Power BI / Tableau Dashboards
- Load same CSVs or connect directly to MySQL
- Build pages:
  - Overview → Total Sales, Monthly Growth, Average Order Value
  - Category Insights → Revenue & Units Sold per Category
  - Customer Insights → Age & Gender Distribution
  - Forecast / Inventory → Forecasted sales & ROP tables
- Add interactivity with slicers for Category, Month, Year, Gender

### Step 7 – Documentation & GitHub
- Organize project folder:


project/
│─ data/ # raw CSVs
│─ notebooks/ # Python scripts
│─ excel/ # Excel dashboards
│─ dashboards/ # Power BI/Tableau files
│─ sql/ # MySQL scripts
│─ README.md # project explanation



---

## 5. Key Insights
- Top-selling product categories and peak sales months
- Customer demographics (age group & gender) affecting sales
- Forecasted sales trends to plan inventory
- Monthly growth and average order value trends for business strategy

---

## 6. How to Run
1. Open MySQL Workbench and create the `retail_analytics_new` database.
2. Load `FACT_SALES_NEW` table using CSV import or SQL scripts.
3. Run Python scripts for cleaning, feature engineering, and forecasting.
4. Export CSV files from Python.
5. Load CSVs into Excel or Power BI to create dashboards.
6. Explore dashboards with slicers and interactive charts.

---

## 7. Screenshots


---

## 8. License
This project is for educational purposes and personal portfolio use.
