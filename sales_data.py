import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("retail_sales.csv", parse_dates=["sale_date"])
    return df

data = load_data()

# Sidebar Filters
st.sidebar.header("Filter Data")
category_filter = st.sidebar.multiselect(
    "Select Category", options=data["category"].unique(), default=data["category"].unique()
)

# Filtered data
filtered_data = data[data["category"].isin(category_filter)]

st.title("🛒 Retail Sales Dashboard")

# KPI Section
total_units = filtered_data["units_sold"].sum()
total_products = filtered_data["product_id"].nunique()
categories_count = filtered_data["category"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Units Sold", f"{total_units:,}")
col2.metric("Total Products", total_products)
col3.metric("Categories", categories_count)

st.markdown("---")

# Line Chart - Sales Over Time
st.subheader("📈 Sales Trend Over Time")
sales_trend = filtered_data.groupby("sale_date")["units_sold"].sum().reset_index()
fig_line = px.line(sales_trend, x="sale_date", y="units_sold", markers=True)
st.plotly_chart(fig_line, use_container_width=True)

# Bar Chart - Units Sold by Category
st.subheader("📊 Units Sold by Category")
bar_data = filtered_data.groupby("category")["units_sold"].sum().reset_index()
fig_bar = px.bar(bar_data, x="category", y="units_sold", color="category")
st.plotly_chart(fig_bar, use_container_width=True)

# Pie Chart - Category Share
st.subheader("🥧 Category Share of Units Sold")
fig_pie = px.pie(bar_data, names="category", values="units_sold", hole=0.4)
st.plotly_chart(fig_pie, use_container_width=True)

# Table - Detailed View
st.subheader("📋 Product-wise Sales")
st.dataframe(filtered_data.sort_values(by="units_sold", ascending=False))

