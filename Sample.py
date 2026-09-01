import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="My Streamlit App", page_icon="🚀")
print("Streamlit and supporting libraries imported.")

# Basic Streamlit app structure
st.title("Welcome to My Streamlit App")
st.write("This is a simple web app built with Streamlit.")
st.header("Quick Overview")
st.markdown("- Easy to build\n- Great for dashboards\n- Interactive and fast")

# Display a simple metric
st.metric(label="Status", value="Ready", delta="Live")

# Interactive widgets
name = st.text_input("What is your name?", "Streamlit User")
age = st.slider("Choose your age", 0, 100, 25)
if st.button("Say hello"):
    st.success(f"Hello {name}! You are {age} years old.")

# Sample data and chart
sample_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [120, 180, 150, 220, 260],
})

st.subheader("Sample Sales Data")
st.dataframe(sample_data)

fig, ax = plt.subplots()
ax.plot(sample_data["Month"], sample_data["Sales"], marker="o")
ax.set_title("Sales Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
st.pyplot(fig)
