import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

sns.set_theme(style="whitegrid")

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page:",
    ["Welcome", "Univariate Analysis", "Bivariate Analysis", "Multivariate Analysis", "Insights"]
)

# ---------------- WELCOME ----------------
if page == "Welcome":
    st.title("Welcome To Streamlit Dashboard For EDA🎉")
    st.write("Upload a dataset and explore insights easily.")

# ---------------- FILE UPLOAD ----------------
st.sidebar.title("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

data = None

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.sidebar.success("Dataset Loaded ✅")

    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    if st.checkbox("Remove missing values"):
        data = data.dropna()
else:
    if page != "Welcome":
        st.warning("Please upload a dataset first")
        st.stop()

# ---------------- DEFINE COLUMNS ----------------
if data is not None:
    numeric_columns = data.select_dtypes(include="number").columns.tolist()
    categorical_columns = data.select_dtypes(include="object").columns.tolist()

# ---------------- UNIVARIATE ----------------
if page == "Univariate Analysis":
    st.title("Univariate Analysis")

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Histogram
    col = st.selectbox("Select numeric column", numeric_columns)
    sns.histplot(data[col], kde=True, ax=axes[0, 0])

    # Countplot
    if categorical_columns:
        cat = st.selectbox("Select categorical column", categorical_columns)
        sns.countplot(data=data, x=cat, ax=axes[0, 1])

    # Boxplot
    sns.boxplot(data=data, x=col, ax=axes[1, 0])

    # Pie chart
    if categorical_columns:
        pie = st.selectbox("Pie column", categorical_columns, key="pie")
        data[pie].value_counts().head(5).plot.pie(autopct="%1.1f%%", ax=axes[1, 1])

    plt.tight_layout()
    st.pyplot(fig)

# ---------------- BIVARIATE ----------------
elif page == "Bivariate Analysis":
    st.title("Bivariate Analysis")

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    x = st.selectbox("X column", numeric_columns)
    y = st.selectbox("Y column", numeric_columns, index=1 if len(numeric_columns)>1 else 0)

    sns.lineplot(data=data, x=x, y=y, ax=axes[0, 0])
    sns.scatterplot(data=data, x=x, y=y, ax=axes[0, 1])

    if categorical_columns:
        cat = st.selectbox("Categorical column", categorical_columns)
        sns.barplot(data=data, x=cat, y=y, ax=axes[1, 0])
        sns.boxplot(data=data, x=cat, y=y, ax=axes[1, 1])

    plt.tight_layout()
    st.pyplot(fig)

# ---------------- MULTIVARIATE ----------------
elif page == "Multivariate Analysis":
    st.title("Multivariate Analysis")

    # Pairplot
    st.subheader("Pairplot")
    cols = st.multiselect("Select columns", numeric_columns, default=numeric_columns[:2])

    if cols:
        sample = data[cols].sample(min(300, len(data)))
        st.pyplot(sns.pairplot(sample))

    # Heatmap
    st.subheader("Heatmap")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(data[numeric_columns].corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# ---------------- INSIGHTS ----------------
elif page == "Insights":
    st.title("Insights 📊")

    col = st.selectbox("Select column", data.columns)

    if col in numeric_columns:
        st.subheader("Numeric Insights")

        st.write("Mean:", round(data[col].mean(), 2))
        st.write("Median:", round(data[col].median(), 2))
        st.write("Max:", data[col].max())
        st.write("Min:", data[col].min())
        st.write("Std Dev:", round(data[col].std(), 2))

    elif col in categorical_columns:
        st.subheader("Categorical Insights")
        st.write(data[col].value_counts().head())

    else:
        st.warning("Unsupported column type")