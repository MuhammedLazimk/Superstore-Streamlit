import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Superstore Dashboard",
    page_icon="📊",
    layout="wide"
)


@st.cache_data
def load_data():
    return pd.read_csv(
        r"C:\Users\mhdlz\OneDrive\Desktop\project_4.1\Data\superstore_clean.csv",
        parse_dates=["order_date", "ship_date"]
    )

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading file: {e}")
    st.stop()


st.title("📊 Superstore Dashboard")
st.markdown("Interactive dashboard for Superstore sales analysis")



with st.sidebar:

    st.header("Filters")

    selected_Regions = st.multiselect(
        "region",
        options=sorted(df["region"].unique()),
        default=sorted(df["region"].unique())
    )

    selected_years = st.multiselect(
        "Year",
        options=sorted(df["order_year"].unique()),
        default=sorted(df["order_year"].unique())
    )

    start_date = st.date_input(
        "Start Date",
        value=df["order_date"].min().date()
    )

    end_date = st.date_input(
        "End Date",
        value=df["order_date"].max().date()
    )



filtered = df[
    (df["region"].isin(selected_Regions)) &
    (df["order_year"].isin(selected_years))
]

filtered = filtered[
    filtered["order_date"].dt.date.between(
        start_date,
        end_date
    )
]



st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Sales",
        f"${filtered['sales'].sum():,.0f}"
    )

with col2:
    st.metric(
        "Total Profit",
        f"${filtered['profit'].sum():,.0f}"
    )

with col3:
    st.metric(
        "Average Discount",
        f"{filtered['discount'].mean():.1%}"
    )



col1, col2 = st.columns(2)

with col1:

    st.subheader("Sales by category")

    category_sales = (
        filtered.groupby("category")["sales"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(category_sales)

with col2:

    st.subheader("Profit by category")

    category_profit = (
        filtered.groupby("category")["profit"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(category_profit)


st.subheader("Monthly Sales Trend")

monthly_sales = (
    filtered.groupby(
        filtered["order_date"].dt.to_period("M")
    )["sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

st.line_chart(monthly_sales)



st.subheader("Filtered Data")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)



csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Filtered Data",
    data=csv,
    file_name="filtered_superstore.csv",
    mime="text/csv"
)



tab1, tab2, tab3 = st.tabs(
    ["📋 Overview", "📦 By Category", "🗺️ By Region"]
)


with tab1:
    st.subheader("Filtered Data Preview")

    st.dataframe(
        filtered.head(20),
        use_container_width=True,
        hide_index=True
    )
    st.subheader("Monthly Sales Trend")

monthly_sales = (
    filtered.set_index("order_date")
    .resample("ME")["sales"]
    .sum()
)

st.line_chart(monthly_sales)


with tab2:
    st.subheader("Sales by category")

    category_sales = (
        filtered.groupby("category")["sales"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(category_sales)
    st.subheader("Sub-Category Breakdown")

    subcategory_summary = (
        filtered.groupby("sub_category")
        .agg(
            Total_Sales=("sales", "sum"),
            Total_Profit=("profit", "sum")
        )
        .sort_values(
            by="Total_Sales",
            ascending=False
        )
    )

    st.dataframe(
        subcategory_summary.style.format("${:,.0f}"),
        use_container_width=True
    )

with tab3:

    st.subheader("Sales by region")

    Region_sales = (
        filtered.groupby("region")["sales"]
        .sum()
        .sort_values(ascending=False)
    )

    st.area_chart(Region_sales)

   



st.markdown("---")

row_count = len(filtered)

min_year = filtered["order_year"].min()
max_year = filtered["order_year"].max()

st.caption(
    f"Showing {row_count:,} rows • "
    f"{min_year}–{max_year} • "
    f"Built by Muhammed Lazim"
)