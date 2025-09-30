import streamlit as st 
import pandas as pd

st.title("Shopping Trends Dashboard")
data  = pd.read_csv('../data/shopping_trends_updated.csv')
st.header("Data Overview")
st.dataframe(data.sample(5))

# sidebar for filtering
st.sidebar.header("Filters")

with st.sidebar:
    age_filter = st.slider("Select Age Range", int(data['Age'].min()), int(data['Age'].max()), (18, 70))
    filtered_data = data[(data['Age'] >= age_filter[0]) & (data['Age'] <= age_filter[1])]

# Page links
st.sidebar.markdown("### Other Pages")
with st.sidebar:
    st.page_link("Shopping_Dashboard.py", label="Home", icon="🏠")
    st.page_link("pages\data_description.py", label="Data Description", icon="📄")

# graph list 
graph_list = st.selectbox(
    "Select a Graph Type",
    ("Gender Distribution", "Category Distribution", "Top 10 Items Purchased", "Highest Purchase Amount Payment Method", "Age Group with Highest Purchase Amount", "Promo Code Distribution")
)

if graph_list == "Gender Distribution":
    st.header("Gender Distribution")
    gender_counts = data['Gender'].value_counts()
    st.bar_chart(gender_counts)

elif graph_list == "Category Distribution":
    st.header("Category Distribution")
    category_counts = data['Category'].value_counts()
    st.bar_chart(category_counts)

elif graph_list == "Top 10 Items Purchased":
    st.header("Top 10 Items Purchased")
    top_items = data['Item Purchased'].value_counts().sort_values(ascending=False).head(10)
    st.bar_chart(top_items, horizontal=True)

elif graph_list == "Highest Purchase Amount Payment Method":
    st.header("Highest Purchase Amount Payment Method")
    highest_payment_amount = data.groupby('Payment Method')['Purchase Amount (USD)'].sum().sort_values(ascending=False)
    st.bar_chart(highest_payment_amount)

elif graph_list == "Age Group with Highest Purchase Amount":
    st.header("Age Group with Highest Purchase Amount")
    age_bins = [18, 25, 35, 45, 55, 65, 70]
    age_labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65-70']
    data['Age Group'] = pd.cut(data['Age'], bins=age_bins, labels=age_labels, right=True, include_lowest=True)
    highest_age_group_purchase = data.groupby('Age Group')['Purchase Amount (USD)'].sum().sort_values(ascending=False)
    st.bar_chart(highest_age_group_purchase)

elif graph_list == "Promo Code Distribution":
    st.header("Promo Code Distribution")
    promocode_used = data['Promo Code Used'].value_counts()
    st.bar_chart(promocode_used)





