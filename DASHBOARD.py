import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(7)
st.write('*CAR SALES RAW DATA*')

# DATA
brands = ['BMW','Audi','Porsche','Rimac','Range Rover','Lamborghini','Mercedes','Mclaren','Pagani','Nissan']
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
years = [2020,2021,2022,2023,2024,2025]
countries = ['Dubai','USA','Italy','China','Japan']

df = pd.DataFrame({
    'Brand':np.random.choice(brands,size=100),
    'Quantity Sold':np.random.randint(14,21,size=100),
    'Month':np.random.choice(months,size=100),
    'Year':np.random.choice(years,size=100),
    'Country':np.random.choice(countries,size=100)
})

st.dataframe(df)

# GRAPHS
graph_filter_by = st.selectbox('Filter by:',['Brand','Month','Year','Country'])
graph_selected = st.selectbox('Select graph:',['Bar Graph','Line Graph','Pie Chart','Scatter plot'])
quantity_sold_sum = df.groupby(graph_filter_by)['Quantity Sold'].sum().reset_index()
see_graph = st.button('See graph')

if see_graph:
    fig,ax = plt.subplots(figsize=(8,4))
    # ---------------- BAR GRAPH ----------------
    if graph_selected == "Bar Graph":
        bars = ax.bar(quantity_sold_sum[graph_filter_by], quantity_sold_sum['Quantity Sold'])
        ax.set_xlabel(graph_filter_by)
        ax.set_ylabel('Quantity Sold')
        ax.set_title(f'Total Quantity Sold by {graph_filter_by}')

        # Add data labels
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                str(height),
                ha='center',
                va='bottom'
            )

    # ---------------- LINE GRAPH ----------------
    elif graph_selected == "Line Graph":
        ax.plot(quantity_sold_sum[graph_filter_by], quantity_sold_sum['Quantity Sold'], marker='o')
        ax.set_xlabel(graph_filter_by)
        ax.set_ylabel('Quantity Sold')
        ax.set_title(f'Trend of Quantity Sold by {graph_filter_by}')

        # Add data labels
        for x, y in zip(quantity_sold_sum[graph_filter_by], quantity_sold_sum['Quantity Sold']):
            ax.text(x, y, str(y), ha='center', va='bottom')

    # ---------------- PIE CHART ----------------
    elif graph_selected == "Pie Chart":
        ax.pie(
            quantity_sold_sum['Quantity Sold'],
            labels=quantity_sold_sum[graph_filter_by],
            autopct='%1.1f%%'
        )
        ax.set_title(f'Distribution by {graph_filter_by}')

    # Only rotate X labels for charts that *have* an X-axis
    if graph_selected in ["Bar Graph", "Line Graph", "Scatter Plot"]:
        plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    st.pyplot(fig)
