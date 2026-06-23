import streamlit as st



st.set_page_config(
    layout="wide",
    page_title="Homepage",
    initial_sidebar_state="auto"
)

import streamlit as st

pg = st.navigation([
    st.Page("pages/home.py",        title="Home",         icon="🏠"),
    st.Page("pages/ai_chatbot.py",  title="Chat Bot",     icon="🤖"),
    st.Page("pages/about_me.py",    title="About Me",     icon="👤"),
    st.Page("pages/contact_me.py",  title="Get In Touch", icon="✉️"),
    st.Page("pages/ecom_customer_satisfaction_analysis.py",  title="Ecommerce customer satisfaction analysis", icon="📈"),
    st.Page("pages/electricity_generated&supplied_from_1920-2024.py",  title="Electricity generated/supplied UK", icon="📉"),
    st.Page("pages/income_expense_tracker.py",  title="Income/Expense app", icon="🧮"),
])


with st.sidebar:
    st.markdown("---")
    st.markdown("### Connect with me")
    st.markdown("""
        <a href="https://github.com/RobsonEgute?tab=repositories" target="_blank">🐙 GitHub</a><br>
        <a href="https://www.linkedin.com/in/robson-egute-7464a7383/" target="_blank">💼 LinkedIn</a><br>
    """, unsafe_allow_html=True)



pg.run()

