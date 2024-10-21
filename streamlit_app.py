import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Data App Assignment, on Oct 7th")

df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)

 # Multi-selct
selected_category = st.selectbox("Select Category", df['Category'].unique())
st.write("You selected:", selected_category)
filtered_df_new = df[df['Category'] == selected_category]

# Select Subcategory
selected_subcat = st.multiselect("Select Subcategory", filtered_df_new['Sub_Category'].unique())
st.write("You selected:", selected_subcat)
filtered_df_data = filtered_df_new[filtered_df_new['Sub_Category'].isin(selected_subcat)]

# Line Chart
st.line_chart(filtered_df_data, x='Order_Date', y="Sales")

 # Calc values
total_sales = filtered_df_data['Sales'].sum()
total_profit = filtered_df_data['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100

# Three Metrics
st.markdown(f"**Total Sales:** ${total_sales:.2f}")
st.markdown(f"**Total Profit:** ${total_profit:.2f}")
st.markdown(f"**Overall Profit Margin:** {profit_margin:.2f}%")

 # Profit margin
overall_avg_profit_margin = (df['Profit'].sum() / df['Sales'].sum()) * 100
delta_profit_margin = profit_margin - overall_avg_profit_margin
st.markdown(f"**Overall Profit Margin:** {profit_margin:.2f}% (Difference from overall average: {delta_profit_margin:.2f}%)")

#Line chart
plt.figure(figsize=(8, 4))
for item in selected_subcat:
    item_data = filtered_df_data[filtered_df_data['Item'] == item]
    plt.plot(item_data['Date'], item_data['Sales'], label=item)
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Over Time')
plt.legend()
st.pyplot()
