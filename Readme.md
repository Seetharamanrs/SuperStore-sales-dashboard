# SuperStore sales Dashboard 
This project provides an end-to-end data analysis pipeline for the popular Sample Superstore dataset. It combines data exploration, interactive visualization, customer segmentation, and time series forecasting using both Prophet and ARIMA models. A responsive Streamlit dashboard is built to help users interact with the data seamlessly.
- A Jupyter Notebook for data exploration and customer segmentation using machine learning.

- An interactive Streamlit dashboard to visualize sales, profits, and discounts dynamically.



## Overview

- Data Cleaning & EDA: Exploring sales trends, profit, and other metrics.
- Visualizations: Trend analysis, regional breakdowns, and category-based insights.
- Customer Segmentation: Using KMeans clustering to group customers based on sales behavior.
- Interactive Dashboard: Built with Streamlit to enable dynamic exploration via filters and charts.

## Streamlit Dashboard
- Interactive sidebar filters for Year, Region, and Category
- KPI cards showing Total Sales, Total Profit, and Average Discount
- Line chart showing Monthly Sales Trends
- Bar charts for Sales by Region and Profit by Category
- CSV download button for exporting the filtered dataset
- Default filter options are intentionally left empty to let users choose freely
- Data caching improves dashboard responsiveness sidebar filter changes reduced from `0.40s → 0.01s`

## Dataset Summary 
- **Total Samples:** 9994
- **Features:** 21
- No missing values found in dataset 
- Time span: 2014-2017

#### Visualizations
- Monthly Sales Trend (Line Chart)
- Region-wise Sales Distribution (Bar Chart)
- Profit by Category (Horizontal Bar Chart)
## ML Model
#### KMeans Clustering
- Segmentation based on Sales, Profit, Discount, Quantity
- PCA used for 2D visualization of customer clusters
#### Time series Forecasting
Prophet Model
- Grouped monthly sales and renamed columns for Prophet
- Split data into train/test
- Built a Prophet model and made predictions for the next 12 months
- Compared predicted values against actuals in a clean line plot
ARIMA Model
- Plotted ACF and PACF to determine optimal parameters
- Built and trained ARIMA on training data
- Forecasted future sales and compared them with test data
## Requirements

See `requirements.txt` to install dependencies:
## How to Run

```bash
pip install -r requirements.txt
```


# Why this projects add value 
- Combines EDA, ML, forecasting, and UI in a single project

- Uses Prophet and ARIMA for comparison — not just one model

- Uses clustering and PCA for real-world customer insights

- Interactive dashboard lets Stake holder can explore results instantly

- Cached data loading improves performance, proving optimization skills
### Possible Future Enhancements
- Add sub-category filtering in dashboard (currently not used by choice)
- Deploy dashboard online (e.g., Streamlit Cloud)
- Add a database backend for dynamic updates
- Include a model performance summary in the dashboard