import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from a CSV file
data = pd.read_csv("E:\\Ahmed Fekry\\New folder (2)\\ecommerce (2).csv")
data[['Year','Month']] = data['Year-Month'].str.split('-', expand=True)
# Create a sidebar
st.sidebar.header("Invoice Data Options")

# Filter data by country (optional)
selected_country = st.sidebar.selectbox("Select a country", data["Country"].unique())
data_filtered = data[data["Country"] == selected_country]

# Display the data as a table
st.dataframe(data_filtered)

# Create a chart of total order value by country
fig = px.bar(data_filtered, x="Country", y="OrderValue",color='Major Category',barmode= 'group', title="Total Order Value by Country")
st.plotly_chart(fig)
selected_variable = "OrderValue"
fig2 = px.histogram(data, x=selected_variable, title=f"{selected_variable} Distribution")
st.plotly_chart(fig2)
fig3 = px.scatter(data, x="UnitPrice", y="OrderValue", title="Order Value vs Unit Price")
st.plotly_chart(fig3)

fig4 = px.bar(
    data, x="Country", y="OrderValue", color="Major Category", title="Order Value by Country and Major Category"
)
st.plotly_chart(fig4)
