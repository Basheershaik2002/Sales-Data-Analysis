# Sales-Data-Analysis

This is a fully interactive web-based dashboard developed using Streamlit, Plotly, and Pandas to analyze and visualize retail sales data. It helps users understand product performance across categories and over time through engaging charts and KPIs.

🔗 Live App: https://sales-viz-replicate.lovable.app/

### Features

Filter sales data in real time by product category.

Display key metrics like total units sold, average sales, and best-performing day.

Interactive visualizations including:

- Line chart for sales trend over time.

- Bar chart showing category-wise sales.

- Pie chart for sales distribution by category.

- Scrollable, searchable product-wise sales table.

### Tech Stack

Python (for backend logic)

Streamlit (for frontend dashboard)

Plotly (for dynamic charts)

Pandas (for data handling)

### Project Structure

sales_data.py: The main Streamlit app script.

retail_sales.csv: Sample dataset.

requirements.txt: List of dependencies.

README.md: Project documentation.

### Dataset Columns

product_id: Unique ID for each product.

product_name: Name of the product.

category: Product category like Electronics, Clothing, etc.

units_sold: Number of units sold per day.

sale_date: Date of sale.

### How to Run the Project Locally

Clone the repository to your machine.

Open your terminal and navigate to the project folder.

Run pip install -r requirements.txt to install required libraries.

Run the app with streamlit run sales_data.py.
