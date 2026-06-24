import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from supabase import create_client
import bcrypt
from datetime import datetime

from dotenv import load_dotenv
import os
os.environ.pop("SSL_CERT_FILE", None)

load_dotenv()


# Streamlit page configuration-----------------------------------------

st.set_page_config(
    layout="wide"
)


#-----------------------------------------------------------------------


# define state-------------------------------------------------

if "isLoggedIn" not in st.session_state:
    st.session_state.isLoggedIn = False

if "user_details" not in st.session_state:
    st.session_state.user_details = {}



#--------------------------------------------------------------



# super base config, create_client-----------------------------


supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase = create_client(supabase_url, supabase_key)


#---------------------------------------------------------------


# Check if user is already signed in_____________________________

cookies = EncryptedCookieManager(
    prefix="main_",
    password=os.getenv("COOKIE_PASS")
)

if not cookies.ready():
    st.stop()

# session restore

def restore_session():
    user_id = cookies.get("user_id")

    if user_id:
        try:
            # Re-fetch the user from your DB using the stored user_id
            user_data = supabase.table("users").select("*").eq("id", user_id).execute()

            if user_data.data:
                st.session_state.isLoggedIn = True
                st.session_state.user_details = user_data.data[0]
                st.session_state.auth_container = "Signedin"
        except Exception as e:
            # Clear bad cookie
            cookies["user_id"] = ""
            cookies.save()

# Run restore on every page load (before UI renders)
if not st.session_state.isLoggedIn:
    restore_session()

# ________________________________________________________________





# Hash Password ------------------------------------------------

def hash_pass(unhashed_pass: str) -> str:
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(unhashed_pass.encode("utf-8"), salt)
    return hashed_pass.decode("utf-8")


#---------------------------------------------------------------


# Authenticate Password ----------------------------------------

def check_pass(unhashed_pass: str, hashed_pass: str) -> bool:
    return bcrypt.checkpw(
        unhashed_pass.encode("utf-8"),
        hashed_pass.encode("utf-8")
    )

#---------------------------------------------------------------


# Register new user---------------------------------------------

def register_user(firstname: str, lastname: str, username: str, email: str, password: str):
    # check if the user email already exist
    checking_email = supabase.table("users").select("email").eq("email", email).execute()

    # check if the user name already exist
    checking_username = supabase.table("users").select("username").eq("username", username).execute()

    print(checking_email)
    print(checking_username)

    if checking_email.data:
        return st.error("This email already exists")
    
    if checking_username.data:
        return st.error("This username already exists")
    
    hashed_password = hash_pass(password)

    # save the user in the database
    supabase.table("users").insert({
         "firstname": firstname,
         "lastname": lastname,
         "username": username,
         "email": email,
         "password": hashed_password
     }).execute()
    
    return(st.success("User details added successfully") )


def log_in(username: str, plain_password: str):
    check_user = supabase.table("users").select("*").eq("username", username).execute()
    if not check_user.data:
        return st.error("Username not found")
    
    hashed_pass = check_user.data[0]['password']

    if check_pass(plain_password, hashed_pass):
        st.session_state.auth_container = "Signedin"
        st.session_state.isLoggedIn = True
        st.session_state.user_details = check_user.data[0]

        # ✅ Persist user_id in cookie
        cookies["user_id"] = str(check_user.data[0]["id"])
        cookies.save()

        st.rerun()
        return st.success("Login successful")
    
    return st.error("Login Unsuccessful")


def log_out():
    st.session_state.isLoggedIn = False
    st.session_state.user_details = {}
    st.session_state.auth_container = ""

    # ✅ Clear cookie
    cookies["user_id"] = ""
    cookies.save()
    st.rerun()

#---------------------------------------------------------------





# saving the income_expense data in the database----------------------------------

def income_expenses(
  user_id: str,
  salary: float,
  rent: float,
  electric_bills: float,
  gas_bills: float,
  network_bills: float,
  car_insurance: float,
  road_tax: float,
  public_transport: float,
  savings: float,
  food: float,
  clothing: float,
  recreational_activities: float,
  date_time: datetime
                    ):
    saving_data =   supabase.table("income_expenses").insert(
                    {
                    "user_id": user_id,
                    "salary": salary,
                    "rent": rent,
                    "electric_bills": electric_bills,
                    "gas_bills": gas_bills,
                    "network_bills": network_bills,
                    "car_insurance": car_insurance,
                    "road_tax": road_tax,
                    "public_transport": public_transport,
                    "savings": savings,
                    "food": food,
                    "clothing": clothing,
                    "recreational_activities": recreational_activities,
                    "date_time": date_time.isoformat()
                    }
                ).execute()
    if saving_data:
        saving_data
        print(saving_data)
        return st.success("Data saved successfully")









#-------------------------------------------------------------------------------------












# Streamlit UI ---------------------------------------------------------------------------------------------------
st.title("Income Expense Tracker", text_alignment="center")

st.info("For this exercise, you'll be required to be sign in order for the components to work.")

st.info("📊 This app supports multiple users — feel free to sign up with any credentials and add as much data as you like. All passwords are stored in an encrypted format, so your credentials are secure.")

st.success(f"""🔍 To see the app at its best, log in with the demo account below — the data was AI-generated purely for demonstration purposes:

**Username:** {os.getenv("EX_USERNAME")} 


**Password:** {os.getenv("EX_PASS")}
""")

st.caption("⚠️ For testing, feel free to create an account with random credentials — no personal information required.")

if "auth_container" not in st.session_state:
    st.session_state.auth_container = ""


col_empty, col1_signup, col2_signin = st.columns([8, 1, 1])

# setting up singin and login buttons ---------------------

with col1_signup:
    if st.button("Signup", key="signup_button", width="stretch"):
        st.session_state.auth_container = "Signup"

with col2_signin:
    if st.button("Signin", key="signin_button",  width="stretch"):
        st.session_state.auth_container = "Signin"

def auth_sel():
    state = st.session_state.auth_container

    if state == "Signup":
        with st.form("signup_form"):
            firstname = st.text_input("Firstname")
            lastname = st.text_input("Lastname")
            username = st.text_input("Username")
            email = st.text_input("Email")
            password = st.text_input("Password")
            signup_submitted = st.form_submit_button("Submit", key="form_sub_butt1")

            if signup_submitted:
                register_user(firstname, lastname, username, email, password)
                st.session_state.auth_container = "Signin"
                print('form submitted')
                st.rerun()
                pass

    if state == "Signin":
        st.session_state.auth_container = "Signin"
        with st.form("signup_form"):
            username = st.text_input("Username")
            password = st.text_input("Password")
            signin_submitted = st.form_submit_button("Submit", key="form_sub_butt")
            
            if signin_submitted:
                log_in(username, password)
                print("sign in form submitted")
                pass

    if state == "Signedin":
        st.info(f"Hello {st.session_state.user_details['firstname']}, you are logged in")
        if st.button("Logout"):
            log_out()

auth_sel()
#-----------------------------------------------------------------------------------------------------------------

# Expense Tracking Form------------------------------------------------------------

with st.expander("Income and Expense Tracking Form"):
    if st.session_state.isLoggedIn == True:
        user_id = st.session_state.user_details["id"]
        with st.form("Fill in the blank"):
            salary = st.number_input("Salary", key="salary")
            rent = st.number_input("Rents", key="rents")
            electric_bills = st.number_input("Electric bills", key="electric_bills")
            gas_bills = st.number_input("Gas bills", key="gas_bills")
            network_bills = st.number_input("Network bills", key="network_bills")
            car_insurance = st.number_input("Car insurance", key="car_insurance")
            road_tax = st.number_input("Road tax", key="road_tax")
            public_transport = st.number_input("Public transport", key="public_transport")
            savings = st.number_input("Savings", key="savings")
            food = st.number_input("Food", key="food")
            clothing = st.number_input("Clothing", key="clothing")
            recreational_activities = st.number_input("Recreational activities", key="recreational_activities")
            date_time = st.datetime_input("Date", key="date")

            if st.form_submit_button("Submit"):
                income_expenses(
                    user_id,
                    salary,
                    rent,
                    electric_bills,
                    gas_bills,
                    network_bills,
                    car_insurance,
                    road_tax,
                    public_transport,
                    savings,
                    food,
                    clothing,
                    recreational_activities,
                    date_time
                )



    else:
        st.info("You must be signed in to use this form")
        




#----------------------------------------------------------------------------------


#Data visualisation plot -------------------------------------------------------

with st.expander("Data visualisation plots"):
    # st.write("plotting...")
    # st.session_state.user_details["id"]

    try:
        # step 1: filter to Get the specific users data from the database
        user_data = supabase.table("income_expenses").select("*").eq("user_id", user_id).execute()
        # user_data
        # print(user_data)
    except Exception as err:
        st.warning(f"Signin to activate some sections {err}")
        st.stop()


    # convert the data into a pandas dataframe
    df = pd.DataFrame(user_data.data)
    if df.empty:
        st.info("No data found. Add an entry to get started.")
        st.stop()

    df['date_time'] = pd.to_datetime(df['date_time'], format='mixed')

    expenditure = [ "rent",
                    "electric_bills",
                    "gas_bills",
                    "network_bills",
                    "car_insurance",
                    "road_tax",
                    "public_transport",
                    "food",
                    "clothing",
                    "recreational_activities"]
    df['balance'] = df["salary"] - df[expenditure].sum(axis=1)
    df['year_month'] = df['date_time'].dt.to_period('M')

    # df

    df.info()

    cols_excluded = {'entry_id', 'user_id', 'date_time', 'balance'}

    df_long = df.melt(
    id_vars=['entry_id', 'user_id', 'date_time', 'year_month'],   # columns to keep as identifiers
    value_vars=[col for col in df.columns if col not in cols_excluded],
    var_name='category',
    value_name='amount'
)
    # df_long

    get_dates = list(df["date_time"].dt.year.unique())
    get_dates = sorted(get_dates)

    colsel1, colsel2 = st.columns(2)

    months_dict = {
            'January':   1,
            'February':  2,
            'March':     3,
            'April':     4,
            'May':       5,
            'June':      6,
            'July':      7,
            'August':    8,
            'September': 9,
            'October':   10,
            'November':  11,
            'December':  12
        }
    try:
        with colsel1:
            sel_year = st.multiselect("year", get_dates, key="year_sel")
            # sel_year

        with colsel2:
            sel_month = st.multiselect("month", months_dict.keys(), key="month_sel")
            # sel_month
            ex = months_dict[sel_month[0]]
            # ex
            print(ex)
            df_long.info()
    except Exception as err:
        st.warning(f"choose a year(s) and month(s)")
        st.stop()

    # Filter out the data based on the users selection:

    if (len(sel_year) == 1)&(len(sel_month) == 1):
        int_yr = int(sel_year[0])
        int_month = int(months_dict[sel_month[0]])
        filt_date = pd.Period(f"{int_yr}-{int_month:02d}", freq='M')
        # filt_date

        filt_df_long = df_long[df_long['year_month'] == filt_date]
        
        # filt_df_long

    elif (len(sel_year) > 1)&(len(sel_month) > 1):
        st_dt_yr = int(min(sel_year))
        st_dt_mt = int(min([months_dict[date] for date in months_dict]))

        start_dt = pd.Period(f"{st_dt_yr}-{st_dt_mt:02d}", freq='M')

        end_dt_yr = int(max(sel_year))
        end_dt_mt = int(max([months_dict[date] for date in months_dict]))

        end_dt = pd.Period(f"{end_dt_yr}-{end_dt_mt:02d}", freq='M')

        filt_df_long = df_long[(df_long['year_month'] >= start_dt) & (df_long['year_month'] <= end_dt)]
        
        # filt_df_long

    elif (len(sel_year) > 1)&(len(sel_month) == 1):
        st_dt_yr = int(min(sel_year))
        end_dt_yr = int(max(sel_year))
        int_month = int(months_dict[sel_month[0]])

        st_dt = pd.Period(f"{st_dt_yr}-{int_month:02d}", freq='M')
        end_dt = pd.Period(f"{end_dt_yr}-{int_month:02d}", freq='M')

        filt_df_long = df_long[(df['year_month'] == st_dt) | (df['year_month'] == end_dt)]



    elif (len(sel_year) == 1)&(len(sel_month) > 1):
        int_yr = int(sel_year[0])
        num_mth_list = [months_dict[word_mnth] for word_mnth in  sel_month]
        periods = [pd.Period(f"{int_yr}-{month:02d}", freq='M') for month in num_mth_list]

        filt_df_long = df_long[df_long['year_month'].isin(periods)]
        
        # filt_df_long
    
    



    pie_df = filt_df_long.loc[filt_df_long['category'] != "salary"]

    st.subheader("Share of expenditure", text_alignment="center")
    fig_pie = px.pie(
        pie_df,
        values="amount",
        names="category",
        color_discrete_sequence=px.colors.qualitative.Pastel,
        hole=0.3,
        width=700,
        height=700,
    )
    st.plotly_chart(fig_pie)

    
    pvt_filt = filt_df_long.pivot_table(
        index="category",
        values="amount",
        aggfunc="sum"
    ).reset_index()
    pvt_show = pvt_filt
    pvt_filt.columns = ["category", "total"]
    
    # pvt_filt


    
    # Define your income and expense categories
    income_cats = ['salary']
    expense_cats = ['rent', 'electric_bills', 'gas_bills', 'network_bills', 
                    'car_insurance', 'road_tax', 'public_transport', 
                    'savings', 'food', 'clothing', 'recreational_activities']

    # Sort df so salary comes first, then expenses
    cat_order = income_cats + expense_cats
    pvt_filt = pvt_filt.set_index('category').loc[cat_order].reset_index()
    

    # Build measure and y values dynamically
    measure = []
    y_values = []

    for cat in pvt_filt['category']:
        amount = pvt_filt.loc[pvt_filt['category'] == cat, 'total'].values[0]
        if cat in income_cats:
            measure.append('absolute')
            y_values.append(amount)
        elif cat in expense_cats:
            measure.append('relative')
            y_values.append(-amount)

    # Calculate the actual balance
    balance = sum(y_values)

    # Add balance as total
    measure.append('total')
    y_values.append(0)  # plotly still needs 0 here to draw the total bar correctly

    categories = list(pvt_filt['category']) + ['balance']

    # Build text labels - use actual balance for the last bar
    text_labels = [f'£{v:,.2f}' for v in y_values[:-1]] + [f'£{balance:,.2f}']

    # Plot
    fig = go.Figure(go.Waterfall(
        orientation='v',
        measure=measure,
        x=categories,
        y=y_values,
        textposition='outside',
        text=text_labels,
        decreasing={"marker": {"color": "red"}},
        increasing={"marker": {"color": "green"}},
        totals={"marker": {"color": "blue"}}
    ))

    fig.update_layout(
        title='Income & Expenditure Waterfall',
        xaxis_tickangle=-45
        )

    st.plotly_chart(fig)

    pvt_show
























#-----------------------------------------------------------------------------------