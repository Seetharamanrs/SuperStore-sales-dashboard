import streamlit as st
import io
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px



st.set_page_config(page_title="Superstore Dashboard", layout="wide")
st.title("Superstore Sales Dashboard")

@st.cache_data
def load_data():
    current_dir = os.path.dirname(__file__)
    path = os.path.normpath(os.path.join(current_dir, '..', 'data', 'Sample - Superstore.xls'))
    df = pd.read_excel(path)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['YearMonth'] = df['Order Date'].dt.to_period('M').astype(str)
    return df
df =load_data()

st.sidebar.header("Filters")
years = sorted(df['Order Date'].dt.year.unique())
regions = df['Region'].unique()
year_filter = st.sidebar.selectbox("Select Year", years)
region_filter = st.sidebar.multiselect("Select Region", regions, default=[])
categories = df['Category'].unique()
category_filter = st.sidebar.multiselect("Select Category", categories, default=[])
filtered_df = df[
    (df['Order Date'].dt.year == year_filter) &
    (df['Region'].isin(region_filter) )&
    (df['Category'].isin(category_filter))
     
]
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
avg_discount = filtered_df['Discount'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric(" Total Profit", f"${total_profit:,.0f}")
col3.metric(" Avg. Discount", f"{avg_discount:.2%}")

# Monthly Sales Trend
monthly_sales = (
    filtered_df.groupby('YearMonth')['Sales']
    .sum()
    .reset_index()
)

def converted_csv(df):
    return df.to_csv(index=False).encode('utf-8')
csv_data = converted_csv(filtered_df)

st.download_button(
    label="Download Filtered Data as CSV",
    data=csv_data,
    file_name='filtered_superstore_data.csv',
    mime='text/csv',
)
st.subheader(" Monthly Sales Trend")
fig1, ax1 = plt.subplots(figsize=(10, 2))
sns.lineplot(data=monthly_sales, x='YearMonth', y='Sales', marker='o', ax=ax1)
plt.xticks(rotation=45)
plt.grid(True)
st.pyplot(fig1)
st.subheader(" Region-wise Sales Distribution")
region_sales = filtered_df.groupby('Region')['Sales'].sum().reset_index()
fig2 = px.bar(region_sales, x='Region', y='Sales', color='Sales', title='Sales by Region')
st.plotly_chart(fig2, use_container_width=True)

# Profit by Category
st.subheader(" Profit by Category")
category_profit = filtered_df.groupby('Category')['Profit'].sum().sort_values()
fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.barplot(x=category_profit.values, y=category_profit.index, palette='coolwarm', ax=ax3)
st.pyplot(fig3)






 