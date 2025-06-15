# Superstore Sales Dashboard

This project is an interactive **dashboard** built using **Streamlit**, **Seaborn**, **Pandas**, and **Matplotlib** to visualize and analyze the sales performance of a fictional retail store using the **Sample Superstore** dataset.

---
 # Overview

- Created a web-based application using `Streamlit` in the file `app.py`.
- Loaded data from the `Sample - Superstore.xls` Excel file.
- Visualized various aspects of the dataset using `Seaborn`, `Pandas`, and `Matplotlib`.

---

## Dataset

- **Source**: Sample - Superstore.xls  
- **Contains**: Sales, Profit, Discount, Quantity, Product Info, Customer Info, Region, Category, Dates, etc.

---

##  Dashboard Features

 **Filters**
- **Year Selector**: 2014, 2015, 2016, 2017  
- **Region Selector**: South, West, Central, East

 **Key Performance Indicators (KPIs)**
-  Total Sales
-  Total Profit
- Average Discount

 **Visualizations**
- **Monthly Sales Trend**: A line chart showing sales over time (by Year-Month)
- **Region-wise Sales Distribution**: A bar chart comparing sales across regions
- **Profit by Category**: A horizontal bar chart displaying profit by product category

---

## How to Run the App


```bash
Python -m streamlit run app.py
