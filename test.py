import perspective_bi as px

# Add a title using markdown
title = px.markdown_text("""
# Sales Report
This report shows the sales performance by category for the last month.
""")

# Load and transform data
sales = px.DataSet('sales.csv')
monthly_sales = (
    sales.filter(date='last_month')
    .aggregate(group_by='category', metrics={'sales': 'sum'})
    .sort_values('sales', ascending=False)
)

# Create visualization
chart = px.bar(
    data=monthly_sales,
    x='category',
    y='sales',
    title='Sales by Category Last Month'
)

# Add some analysis using markdown
analysis = px.markdown_text("""
## Key Findings
- Category A has the highest sales
- Category B shows strong growth
- Category C needs attention
""")