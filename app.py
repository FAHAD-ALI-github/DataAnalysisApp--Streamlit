import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Set the title
st.title("📊 Data Analysis Application")
st.subheader("An interactive tool for quick, insightful data exploration and visualization")


# Dataset selection
dataset_options = ['iris', 'titanic', 'tips', 'diamonds']
selected_dataset = st.selectbox("Select a sample dataset", dataset_options)

# Load the selected dataset
if selected_dataset:
    df = sns.load_dataset(selected_dataset)

# Upload your own dataset
uploaded_file = st.file_uploader('Or upload a custom dataset', type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()

# Display dataset
st.markdown("---")
st.subheader("📋 Dataset Preview")
st.write(df)

# Check for null values
st.subheader("🔍 Null Values")
nulls = df.isnull().sum()
if nulls.sum() > 0:
    st.write(nulls[nulls > 0].sort_values(ascending=False))
else:
    st.write("✅ No null values found.")

# Summary statistics
st.subheader("📈 Summary Statistics")
st.write(df.describe())

# Pairplot section
st.markdown("---")
st.subheader("📉 Pairplot")

# Dropdown to select hue column
categorical_cols = df.select_dtypes(include='object').columns.tolist() + df.select_dtypes(include='category').columns.tolist()
if len(categorical_cols) > 0:
    hue_column = st.selectbox("Select a column for hue", categorical_cols)
    try:
        pairplot_fig = sns.pairplot(df, hue=hue_column)
        st.pyplot(plt.gcf())
        plt.clf()
    except Exception as e:
        st.warning(f"Unable to generate pairplot: {e}")
else:
    st.info("No categorical column found for hue. Skipping pairplot.")

# Heatmap section
st.markdown("---")
st.subheader("🔥 Correlation Heatmap")

numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

if len(numeric_columns) >= 2:
    corr_matrix = df[numeric_columns].corr()
    heatmap_fig = go.Figure(
        data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='Viridis'
        )
    )
    st.plotly_chart(heatmap_fig)
else:
    st.info("Not enough numerical columns for heatmap.")
