import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import time


st.set_page_config(
    page_icon="📊",
    layout="wide"
)

st.markdown(
            """
            <div class="title_container" 
            style="
            padding-bottom: 10px;
            ">
            <h1 style="
                text-align: center;
                font-size: 38px;
                font-weight: bold;
                "
            >
                E-commerce Customer Satisfaction Analysis For The Month of August 2023
            </h1>
            </div>
            """,
            unsafe_allow_html=True
            )

# Cleaning the data by converting the columns to all lower case and replacing spaces with underscores

df = pd.read_csv("datasets\Customer_support_data.csv.zip")

df.columns = (df.columns.str.lower()
              .str.replace(r"[ -]", "_", regex=True)
              )

# we create a copy of the dataframe to work with and preserve the original data for reference
df_copy = df.copy()

nu_duplicated = df_copy.duplicated().sum()

if nu_duplicated > 0:
    df_cleaned = df_copy.drop_duplicates(inplace=True)

card_col1, card_col2, card_col3 = st.columns(3);

#center the text in the metric cards
st.markdown(
    """
    <style>
    /* Target the metric container */
    [data-testid="stMetric"] {
        text-align: center;
        border: 1px solid #ddd;
        border-radius: 10px;
    }

    [data-testid="stMetricLabel"] > div > p {
        font-size: 30px !important;
        text-align: center;
        width: 100%;
        font-weight: bold;
    }

    /* Center the label (the title) */
    [data-testid="stMetricLabel"] {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Center the value and delta */
    [data-testid="stMetricValue"] {
        text-align: center;
        font-size: 70px;
        font-weight: bold;
    }
    
    /* Center the delta arrow and text */
    [data-testid="stMetricDelta"] > div {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

nu_complaints = len(df_copy.unique_id)

# Data Metrics section -------------------------------------


card_col1.metric("Total complaints", f"{nu_complaints:,}")

# convert the dates from a string to datetime format
df_copy['issue_reported_at'] = pd.to_datetime(df_copy['issue_reported_at'], dayfirst=True, errors='coerce')
df_copy['issue_responded'] = pd.to_datetime(df_copy['issue_responded'], dayfirst=True, errors='coerce')

# create a new columns to calculate the response time in hours:
df_copy['response_time_hours'] = (df_copy['issue_responded'] - df_copy['issue_reported_at']).dt.total_seconds() / 3600

# Add a new card metric
av_response_time = df_copy['response_time_hours'].mean()
card_col2.metric("Average response time(hours)", f"{av_response_time:.2f}")

# Average customer satisfaction score
av_csat_score = df_copy['csat_score'].mean()
card_col3.metric("Average CSAT score", f"{av_csat_score:.2f}")



# Data Metrics section -------------------------------------



# row 2 -----------------------------------------------------------------------



# create a new column to categorise the complaints into different categories, and rank the sub complaints by frequency
pie_col1, pie_col2 = st.columns([1, 2])


#share of complaints category by chanel
fil_dat1 = df_copy.channel_name.value_counts().reset_index(name="count")
fig1 = px.pie(
    fil_dat1,
    values="count",
    names="channel_name",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    hole=0.4
)

# customize the borders of the containers that hold the charts using CSS
st.markdown("""
    <style>
    /* This targets the container with a border */
    [data-testid="stElementContainer"] > div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 50px solid #4CAF50 !important; /* Thickness and Color */
        border-radius: 10px !important;       /* Roundness */
        padding: 20px;                         /* Spacing inside */
    }
    </style>
    """, 
    unsafe_allow_html=True
    )

with pie_col1:
    with st.container(border=True, height=650):
        st.markdown(
            """
              <h3 style="text-align: center;">
                Share of complaints by channel
              </h3>
            """,
            unsafe_allow_html=True
        )
        st.plotly_chart(fig1, use_container_width=True)

# share of complaints category by sub category
filt_dat2 = df_copy.sub_category.value_counts().reset_index(name="count").sort_values(by="count", ascending=False)
filt_dat2 = filt_dat2.head(10)

filt_dat2.sort_values(by="count", ascending=True, inplace=True)

fig2 = px.bar(
    filt_dat2,
    x="count",
    y="sub_category",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    orientation="h"
)


with pie_col2:
    with st.container(border=True, height=650):
        st.markdown(
            """
              <h3 style="text-align: center;">
                Top 10 complaints by sub-categorries
              </h3>
            """,
            unsafe_allow_html=True
        )
        st.plotly_chart(fig2, use_container_width=True)

# shifts period with the most complaints
shift_prds = df_copy.agent_shift.value_counts().reset_index(name="count")



# row 2 -----------------------------------------------------------------------


# row 3 -----------------------------------------------------------------------

row3_col1, row3_col2 = st.columns([1, 2])

with row3_col1:
    with st.container(border=True, height=650):
        st.markdown(
            """
            <h3 style="text-align: center;">
                Shift receiving the most complaints?
            </h3>

            """,
            unsafe_allow_html=True
        )
        fig3 = px.pie(
            shift_prds,
            values="count",
            names="agent_shift",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            hole=0.4
        )
        st.plotly_chart(fig3, use_container_width=True)

with row3_col2:
    with st.container(border=True, height=650):
        st.markdown(
            """
            <h3 style="text-align: center;">
                Data source
            </h3>
            """,
            unsafe_allow_html=True
        )
        df_copy


# row 3 -----------------------------------------------------------------------
