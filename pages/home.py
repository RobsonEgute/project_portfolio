import streamlit as st

st.title("Home page", text_alignment="center")

st.info("I build data-driven solutions that turn raw numbers into real insights. " \
"This portfolio showcases my work across data analytics and data science — from uncovering trends hidden in complex datasets to building predictive models that drive smarter decisions. " \
"Data is everywhere, but knowing what to do with it is a skill — and it's one I've spent years sharpening. " \
"Every project here is a testament to that: clean analysis, sharp visualisations, and models built with purpose, not just precision. " \
"I work across the full data pipeline — from gathering and cleaning messy, real-world data to delivering findings that are clear, actionable, and impossible to ignore. " \
"Whether you're a business looking to make better decisions, a team that needs someone to make sense of your data, or an employer searching for a data professional who brings both technical depth and strategic thinking — you're in the right place. " \
"Take a look at my work, and let's talk about what we can build together."
)

st.warning("💬 Want quick answers? Try the AI Chatbot — ask it anything about my projects, skills, or experience and get instant, specific answers without scrolling through the whole portfolio.")

col1r1, col2r1 = st.columns([1, 2])
with col1r1:
    st.subheader("Project 1")
    with st.container(border=True):
        st.write("Ecommerce Customer Satisfaction Analysis")

with col2r1:
    st.subheader("Description")
    with st.container(border=True):
        with st.expander("click for full descriotion"):
            st.markdown("""
                            # E-commerce Customer Satisfaction Dashboard

## Overview

This interactive dashboard provides a comprehensive breakdown of customer support activity for an e-commerce business during **August 2023**. Built for customer experience managers, support team leads, and operations analysts, it transforms raw complaint ticket data into actionable insight — surfacing where complaints originate, what customers are most unhappy about, and how efficiently the support team is responding.

The goal is to give decision-makers a clear, at-a-glance picture of support performance and complaint patterns, without having to dig through raw data.

---

## KPI Metrics

Three headline metrics sit at the top of the dashboard, giving an immediate pulse check on support health:

| Metric | Description |
|---|---|
| **Total Complaints** | Full count of support tickets logged during August 2023 — the volume baseline for everything that follows. |
| **Average Response Time (hours)** | Calculated by subtracting the issue report timestamp from the first response timestamp and converting to hours. A direct measure of team responsiveness and a key driver of customer satisfaction. |
| **Average CSAT Score** | Mean customer satisfaction score across all resolved tickets. The single most important outcome metric in the dashboard; all other charts exist to help explain it. |

---

## Charts

### 1. Share of Complaints by Channel — Donut Chart

Breaks down the proportion of complaints arriving through each support channel (e.g. chat, email, phone, social media).

**What it answers:** *Where are customers reaching out?* Understanding channel distribution helps support teams allocate staffing appropriately and identify whether certain channels are being over- or under-resourced relative to demand.

---

### 2. Top 10 Complaints by Sub-Category — Horizontal Bar Chart

A ranked horizontal bar chart showing the ten most frequent complaint sub-categories, sorted in ascending order for easy visual scanning.

**What it answers:** *What are customers most upset about?* Whether it's delivery delays, refund issues, or product defects, this chart pinpoints the highest-frequency pain points driving ticket volume — the highest-leverage areas for product or process improvement.

---

### 3. Shift Receiving the Most Complaints — Donut Chart

Distributes complaints across agent work shifts (e.g. morning, afternoon, night).

**What it answers:** *When do complaints peak?* This matters both for scheduling — ensuring adequate coverage during high-volume windows — and for quality monitoring, since certain shifts may consistently handle harder or more complex cases.

---

### 4. Raw Data Table

The full cleaned dataframe is exposed at the bottom of the dashboard, giving analysts the ability to drill into individual records, verify aggregates, or export data for further investigation. It functions as the audit layer of the dashboard.

---

## Tech Stack

| Layer | Tool |
|---|---|
| App framework | [Streamlit](https://streamlit.io/) |
| Data manipulation | [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) |
| Visualisation | [Plotly Express](https://plotly.com/python/plotly-express/) |
| Data format | CSV (zipped) |
| Styling | Custom CSS via `st.markdown()` + `unsafe_allow_html=True` |

---

## Dataset

The underlying data is sourced from Kaggle:

**[Customer Support Data](https://www.kaggle.com/datasets/akashbommidi/customer-support-data)** — by Akash Bommidi

The dataset contains e-commerce customer support ticket records including complaint categories, response timestamps, channel information, agent shift data, and CSAT scores.
                        
[PROJECT LINK](http://localhost:8501/ecom_customer_satisfaction_analysis)
                        """)
            

col1r2, col2r2 = st.columns([1, 2])
with col1r2:
    st.subheader("Project 2")
    with st.container(border=True):
        st.write("UK electricity generation/consumption analysis")

with col2r2:
    st.subheader("Description")
    with st.container(border=True):
        with st.expander("click for full description"):
            st.markdown("""
                            # Electricity Generation & Supply in the UK (1920–2024)

## Overview

This interactive dashboard explores over a century of electricity generation and supply data in the United Kingdom, covering the period from **1920 to 2024**. Built for energy analysts, policy researchers, and data enthusiasts, it transforms historical government energy records into clear visual narratives — tracking how the UK's electricity mix has evolved across coal, oil, gas, nuclear, and renewables over more than 100 years.

The dashboard answers a deceptively simple question: *how has the UK powered itself, and how has that changed?*

---

## KPI Metrics

Nine headline metrics provide an aggregated summary of electricity generation across all selected years, broken down by energy source. All figures are dynamically filtered by the year selector and formatted for readability (K, M, B).

| Metric | Description |
|---|---|
| **Total** | Combined electricity generation across all sources for the selected period. |
| **Coal** | Total estimated generation from coal — the dominant source through most of the 20th century. |
| **Oil** | Total generation from oil-fired power stations. |
| **Natural Gas** | Total generation from gas — which largely replaced coal from the 1990s onward. |
| **Nuclear** | Total nuclear generation since the first stations came online in the 1950s. |
| **Renewables** | Combined output from wind, wave, solar, and hydro sources. |
| **Coke & Breeze** | Generation from coke oven and blast furnace gases — an industrial-era legacy source. |
| **Pumped Storage** | Contribution from pumped hydro storage — used for grid balancing rather than net generation. |
| **Others** | All remaining fuel types not captured in the named categories. |

---

## Charts

### 1. Source of Electricity Generation by Share — Pie Chart

A pie chart showing the proportional contribution of each energy source (coal, oil, gas, nuclear, renewables, coke & breeze, pumped storage, and others) to total generation across the selected time window.

**What it answers:** *What has powered the UK?* This chart makes the energy transition visible — from a coal-dominated grid in the early 20th century, through the rise of gas and nuclear, to the growing share of renewables in recent decades. The year filter makes it possible to isolate and compare specific eras.

---

### 2. Electricity Generated vs. Net Electricity Supplied — Line Chart

A multi-series line chart tracking three variables over time from 1920 to 2024: total electricity generated by major power producers, net electricity supplied to the grid, and the calculated difference between the two.

**What it answers:** *How much electricity was produced, how much reached consumers, and what was lost?* The gap between generation and supply reflects transmission losses, station own-use, and pumped storage consumption. Tracking this over a century reveals both infrastructure improvements and the increasing complexity of the modern grid.

---

## Data Tables

Four raw data tables are exposed across two rows, showing both the uncleaned and cleaned versions of each dataset side by side:

- **Uncleaned vs. Cleaned — Estimated Historical Generation:** Shows the transformation from the raw Excel sheet (with merged header rows and inconsistent formatting) to the cleaned, analysis-ready dataframe.
- **Uncleaned vs. Cleaned — Electricity Generated and Supplied:** Same before/after comparison for the generation and supply dataset, demonstrating the column renaming, datetime conversion, and derived `Difference` column added during cleaning.

These tables serve as a transparency layer, making the data wrangling process visible and auditable.

---

## Filters

A year multiselect filter allows users to narrow all metrics and charts to a specific set of years — enabling direct comparisons between energy eras (e.g. pre-war vs. post-war, or pre- vs. post-renewables boom).

---

## Tech Stack

| Layer | Tool |
|---|---|
| App framework | [Streamlit](https://streamlit.io/) |
| Data manipulation | [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) |
| Visualisation | [Plotly Express](https://plotly.com/python/plotly-express/) |
| Data format | Excel (`.xlsx`, multi-sheet) |
| Styling | Custom CSS via `st.markdown()` + `unsafe_allow_html=True` |

---

## Dataset

The underlying data is sourced from the UK Government's Department for Energy Security and Net Zero:

**[Electricity since 1920 — DESNZ Historical Data](https://www.gov.uk/government/statistical-data-sets/historical-electricity-data)**

The dataset contains multi-sheet Excel records covering estimated historical generation by fuel source, share of generation, and gross electricity supplied by major power producers — spanning 1920 to 2024.

[PROJECT LINK](http://localhost:8501/electricity_generated&supplied_from_1920-2024)                        

                            """)



col1r3, col2r3 = st.columns([1, 2])
with col1r3:
    st.subheader("Project 3")
    with st.container(border=True):
        st.write("Income/Expense tracking and analysis app")

with col2r3:
    st.subheader("Description")
    with st.container(border=True):
        with st.expander("click for full descriotion"):
            st.markdown("""
                           # Income & Expense Tracker

## Overview

This full-stack personal finance application allows users to log, store, and visualise their monthly income and expenses in real time. Built with a secure authentication system and a cloud database backend, it gives individuals a structured way to track where their money goes — breaking spending down by category and surfacing their true monthly balance.

The app is designed for anyone who wants to move beyond spreadsheets and gain a clear, data-driven picture of their personal finances.

---

## Authentication System

The app implements a complete user authentication flow with persistent session management:

- **Sign Up** — New users register with a first name, last name, username, email, and password. The app checks for duplicate emails and usernames before registering, and all passwords are hashed using **bcrypt** before being stored in the database. Plain-text passwords are never saved.
- **Sign In** — Returning users authenticate with their username and password. The entered password is verified against the stored bcrypt hash.
- **Session Persistence** — Upon login, the user's ID is stored in an **encrypted browser cookie** via `streamlit-cookies-manager`. On every page load, the app checks for a valid cookie and restores the session automatically — no need to log in again after refreshing.
- **Log Out** — Clears both the session state and the encrypted cookie, fully terminating the session.

All authenticated data is scoped to the logged-in user — no user can access another user's records.

---

## Income & Expense Form

A collapsible form allows signed-in users to log a financial entry for a given date. Each entry captures:

| Field | Category |
|---|---|
| Salary | Income |
| Rent | Fixed expense |
| Electric bills | Fixed expense |
| Gas bills | Fixed expense |
| Network bills | Fixed expense |
| Car insurance | Fixed expense |
| Road tax | Fixed expense |
| Public transport | Variable expense |
| Savings | Allocation |
| Food | Variable expense |
| Clothing | Variable expense |
| Recreational activities | Variable expense |

Each submission is timestamped and saved to a user-specific record in the Supabase database. Users who are not signed in see a prompt to log in instead of the form.

---

## Charts

### 1. Share of Expenditure — Donut Pie Chart

A donut chart showing the proportional breakdown of spending across all expense categories for the selected time window (salary excluded).

**What it answers:** *Where is the money actually going?* This chart makes it immediately clear whether rent, food, or discretionary spending like clothing and recreation dominate the monthly outgoings — and by how much.

---

### 2. Income & Expenditure Waterfall Chart

A waterfall chart that starts with gross salary, subtracts each expense category one by one, and lands on the final calculated balance.

- Income bars are shown in **green**
- Expense bars are shown in **red**
- The final balance bar is shown in **blue**

Each bar is labelled with its exact value in GBP (£).

**What it answers:** *What is left at the end of the month, and what took the most?* The waterfall format makes it visually obvious how each category erodes the salary — and whether the user ends the month in surplus or deficit.

---

## Filters

Users can filter all visualisations by **year** and **month** using two multiselect dropdowns. The app handles four filtering scenarios:

- Single year + single month — shows that exact period
- Multiple years + multiple months — shows the full range between earliest and latest selection
- Multiple years + single month — compares the same month across different years
- Single year + multiple months — shows a range of months within one year

---

## Tech Stack

| Layer | Tool |
|---|---|
| App framework | [Streamlit](https://streamlit.io/) |
| Database | [Supabase](https://supabase.com/) (PostgreSQL) |
| Authentication | [bcrypt](https://pypi.org/project/bcrypt/) + [streamlit-cookies-manager](https://pypi.org/project/streamlit-cookies-manager/) |
| Data manipulation | [pandas](https://pandas.pydata.org/) |
| Visualisation | [Plotly Express](https://plotly.com/python/plotly-express/), [Plotly Graph Objects](https://plotly.com/python/graph-objects/) |
| Environment management | [python-dotenv](https://pypi.org/project/python-dotenv/) |
| Data format | Live database records (Supabase REST API) | 
                        
                        

                            """)
            

st.info("🐙 This portfolio is just the highlight reel. Head over to [MY GITHUB](https://github.com/RobsonEgute?tab=repositories) to explore the full collection — Power BI dashboards, JavaScript projects, and more Python work across Matplotlib, Seaborn, and beyond.")

st.warning("📥 Power BI projects will need to be downloaded from GitHub and opened in Power BI Desktop to view the full dashboard, as I don't currently have a Power BI online hosting account.")