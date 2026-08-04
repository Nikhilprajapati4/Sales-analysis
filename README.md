# E-Commerce Sales Analysis Project
## Project Overview
This project is an end-to-end e-commerce sales analytics solution built using the **Olist Brazilian E-commerce dataset**. The objective is to design a complete data analytics pipeline that automates data ingestion, stores data in a relational database, performs SQL-based business analysis, prepares analytical datasets, and creates interactive dashboards for business decision-making.
The project begins with raw CSV files downloaded from the Olist dataset. Instead of manually importing the files into PostgreSQL, a Python-based data ingestion pipeline was developed using **Pandas** and **SQLAlchemy**. The pipeline automatically loads all datasets into PostgreSQL, and every time the ingestion script is executed, the database is updated with the latest data. A logging system was also implemented to record the execution process, making it easier to monitor successful loads and troubleshoot errors.
After loading the data into PostgreSQL, SQL was used to explore the database and answer key business questions related to revenue, customer behavior, product performance, geographical sales distribution, and order trends. Multiple relational tables were joined to create a consolidated summary table that simplifies business analysis and reporting.
The summary table was then imported back into PostgreSQL as a separate analytical table. This table served as the primary dataset for further data cleaning and exploratory analysis using Python. During preprocessing, missing values were handled, duplicate records were removed, and data quality issues were corrected to prepare a clean dataset for visualization.
Finally, the cleaned data was used to create an interactive Tableau dashboard that presents key performance indicators (KPIs), sales trends, customer insights, regional performance, product category analysis, and delivery performance. The dashboard enables stakeholders to explore business performance through dynamic filters and visual reports.
---
# Project Workflow
### 1. Data Collection
* Downloaded the Olist Brazilian E-commerce dataset in CSV format.
* Organized multiple related datasets, including customers, orders, order items, products, sellers, payments, reviews, and geolocation.

### 2. Automated Data Ingestion

* Built a Python ETL script using Pandas and SQLAlchemy.
* Automatically imported all CSV files into PostgreSQL.
* Designed the pipeline so that rerunning the script refreshes the database automatically.
* Generated execution logs to monitor the ingestion process and capture errors.

### 3. Database Management

* Stored all datasets in PostgreSQL.
* Verified data integrity after import.
* Managed relationships between multiple tables.

### 4. SQL Business Analysis

Business questions answered include:

* Total Revenue
* Monthly Revenue Trend
* Revenue by Year
* Average Order Value (AOV)
* Top Selling Product Categories
* Best Selling Products
* Revenue by State
* Revenue by City
* Peak Sales Months
* Customer Purchase Trends

### Initial Business Insights

| Business Question        | Result            |
| ------------------------ | ----------------- |
| Total Revenue            | **15,422,461**    |
| Average Order Value      | **159**           |
| Highest Revenue Category | Health & Beauty   |
| Best Selling Category    | Bed, Bath & Table |
| Highest Revenue State    | São Paulo (SP)    |
| Peak Sales Month         | May               |

### 5. Summary Table Creation

* Joined multiple normalized tables using SQL.
* Created a business-friendly summary dataset.
* Imported the summary dataset back into PostgreSQL as a new analytical table.
* Simplified downstream analysis by reducing complex joins.

### 6. Data Cleaning with Python

Performed data preprocessing on the analytical dataset:

* Removed duplicate records
* Handled missing values
* Replaced null values where appropriate
* Corrected inconsistent data
* Validated data types
* Prepared the final dataset for visualization

### 7. Exploratory Data Analysis (EDA)

The cleaned dataset was analyzed to identify business trends, including:

* Delivery status by year
* Monthly revenue trend
* Yearly revenue trend
* Monthly order trend
* Revenue by state
* Revenue by city
* Top-selling product categories
* Product categories with the highest late deliveries
* Actual revenue analysis
* Customer purchasing patterns

### 8. Dashboard Development

An interactive Tableau dashboard was created featuring:

* Total Revenue
* Total Orders
* Average Order Value
* Monthly Revenue Trend
* Revenue by Year
* Monthly Order Trend
* Revenue by State
* Revenue by City
* Top Product Categories
* Delivery Performance
* Late Deliveries by Product Category
* Interactive filters for year, month, state, and product category

---

# Technology Stack

* Python
* Pandas
* SQLAlchemy
* PostgreSQL
* SQL
* Tableau
* Jupyter Notebook
* Git & GitHub

---

# Project Highlights

* Automated ETL pipeline using Python
* Dynamic PostgreSQL database updates
* Logging system for ETL monitoring
* SQL-based business analysis
* Analytical summary table creation
* Data cleaning and preprocessing with Python
* Interactive Tableau dashboard
* End-to-end analytics workflow from raw data to business insights
