# SuperStore sales Dashboard 
This project is an end-to-end interactive data visualization and analysis tool built using Python, Streamlit, Pandas, Seaborn, Matplotlib, and scikit-learn. It analyzes a fictional retail store's historical performance using the Sample Superstore dataset.
- A Jupyter Notebook for data exploration and customer segmentation using machine learning.

- An interactive Streamlit dashboard to visualize sales, profits, and discounts dynamically.



## Overview

- Data Cleaning & EDA: Exploring sales trends, profit, and other metrics.
- Visualizations: Trend analysis, regional breakdowns, and category-based insights.
- Customer Segmentation: Using KMeans clustering to group customers based on sales behavior.
- Interactive Dashboard: Built with Streamlit to enable dynamic exploration via filters and charts.

## Dataset Summary 
- **Total Samples:** 9994
- **Features:** 21
- No missing values found in dataset 
- Time span: 2014-2017
## Dashboard Features (Streamlit)
### Filters
- Year Selector: 2014, 2015, 2016, 2017
- Region Selector: South, West, Central, East

#### Key Performance Indicators (KPIs)
- Total Sales
- Total Profit
- Average Discount

#### Visualizations
- Monthly Sales Trend (Line Chart)
- Region-wise Sales Distribution (Bar Chart)
- Profit by Category (Horizontal Bar Chart)
## ML Model
#### KMeans Clustering
- Segmentation based on Sales, Profit, Discount, Quantity
- PCA used for 2D visualization of customer clusters
## Requirements

See `requirements.txt` to install dependencies:
## How to Run

```bash
pip install -r requirements.txt