# note to run streamlit use the command in terminal: streamlit run DataVisualization/streamlit_tmp.py

import streamlit as st
import plotly.express as px

st.title("Iris Dataset Visualization")
df = px.data.iris()
st.dataframe(df.head())

# # multiselect
# selected_species = st.multiselect(
#     "Select Species:",
#     options=df['species'].unique(),
#     default=df['species'].unique().tolist()
# )

col1, col2 = st.columns(2)

with col1:
    selected_species = st.multiselect(
        "Select Species:",
        options=df['species'].unique(),
        default=df['species'].unique().tolist()
    )

with col2:
    data_amount = st.slider("Number of Data Points", min_value=10, max_value=len(df), value=50)


filtered_df = df[df['species'].isin(selected_species)]
filtered_df = filtered_df.head(data_amount)

st.scatter_chart(df, x='sepal_width', y='sepal_length', color='species')

