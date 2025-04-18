import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('sales_data.db')

# --- First Query: Grouped Revenue and Quantity by Product ---
query1 = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""

df1 = pd.read_sql_query(query1, conn)
print("=== Sales Summary by Product ===")
print(df1)

# Plot bar chart of revenue by product
df1.plot(kind='bar', x='product', y='revenue', legend=False, title='Revenue by Product')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# --- Second Query: Total Revenue ---
query2 = """
SELECT SUM(quantity * price) AS total_revenue FROM sales
"""
df2 = pd.read_sql_query(query2, conn)
print("\n=== Total Revenue ===")
print(df2)

# Close the database connection
conn.close()
