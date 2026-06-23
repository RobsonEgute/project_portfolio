import streamlit as st
import os
import ssl
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()


# Streamlit page congig --------------------------------------

st.set_page_config(
    layout="wide",
    page_title="AI chatbot",
    page_icon=":'"
)

#--------------------------------------------------------------

PORTFOLIO_CONTEXT = """

You are a helpful assistant for Robson's developer portfolio.
Answer questions about their projects, skills, and experience based only on
the information below. If you don't know something, say so honestly and
suggest the visitor get in touch directly at eguterobson@yahoo.co.uk.

---

NAME: Robson Egute
TITLE: Full-Stack Python and Javascript Developer | Data Analyst | Sustainability Analyst
LOCATION: West Midlands England, United Kingdom
CONTACT: eguterobson@yahoo.co.uk | https://www.linkedin.com/in/robson-egute-7464a7383/ | https://github.com/RobsonEgute
 
BIO:
I am a passinate data nerd, with an M.sc in sustainability and environmental management from Coventry University UK.
Whatever the project i undertake, i keep sustainability and efficiency at my core. 
My drive is to be a net positive contributor to protect and conserve our environment and just make the world a better place.
I bring key skills in programming, academics and peoples skills to get the job done fast.
 
SKILLS:
- Languages: Python, Javascript, SQL, Git-Bash, HTML, CSS
- Python Frameworks: Numpy, Pandas, Plotly, Matplotlib, Seaborn, Streamlit, Supabase, Bcrypt, 
- Javascript Frameworks: React.js, Redux.js, Bootstrap.js, Next.js, Express.js, D3.js
- Tools: PostgreSQL, MYSQL, Git-HUB, Vscode, Microsoft Excel, Libreoffice Calc, Jupyter Notebooks, Microsoft word, Microsoft Powerpoint, MongoDB  
 
PROJECTS:
 
1. Ecommerce Customer Satisfaction Analysis:
   - Description: 
        The E-commerce Customer Satisfaction Analysis Dashboard is a business intelligence and customer service analytics solution developed using Python, Streamlit, Pandas, NumPy, and Plotly. 
        The primary objective of the project is to help customer support managers, operations teams, quality assurance specialists, and business stakeholders gain a deeper understanding of customer service performance and customer satisfaction levels within an e-commerce environment. 
        The dashboard processes customer support records from August 2023 and transforms raw transactional data into meaningful insights that can be used to evaluate service quality, identify recurring customer issues, and support data-driven decision-making. 
        To ensure data quality and reliability, the application performs several preprocessing operations including column standardization, duplicate detection, date-time conversion, and response-time calculations before generating analytical outputs.

        The dashboard provides a collection of key performance indicators that allow users to quickly assess the overall effectiveness of customer support operations. 
        These metrics include the total number of customer complaints received, the average response time taken by support agents to address reported issues, and the average Customer Satisfaction (CSAT) score achieved across all interactions. 
        These indicators serve as high-level measures of operational efficiency and customer experience. By monitoring these metrics, organizations can identify whether support teams are meeting expected service standards, determine how quickly customer concerns are being resolved, and evaluate how customers perceive the quality of support provided. 
        This information enables managers to track performance trends, establish benchmarks, and implement targeted improvements to enhance customer satisfaction and loyalty.

        To provide deeper analytical insights, the dashboard incorporates several interactive visualizations that examine customer support activities from multiple perspectives. 
        The Complaint Channel Distribution Pie Chart analyzes the proportion of complaints received through different communication channels, helping organizations understand customer preferences and allocate support resources more effectively across channels. 
        The Top 10 Complaint Sub-Categories Bar Chart identifies and ranks the most frequently reported issues, allowing management teams to pinpoint recurring pain points, prioritize corrective actions, and address the root causes of customer dissatisfaction. 
        Additionally, the Agent Shift Distribution Pie Chart evaluates how complaint volumes are distributed across different work shifts, enabling organizations to assess staffing effectiveness, balance workloads, and optimize workforce scheduling. 
        Together, these visualizations transform large volumes of customer support data into actionable business intelligence, empowering stakeholders to improve operational efficiency, reduce response times, enhance service quality, and deliver a superior customer experience.

   - Tech stack: Python, Streamlit, Pandas, NumPy, Plotly, HTML, CSS, Data Analysis, Data Visualization, Dashboard Development, Business Intelligence Analytics.
   
   - Highlights: 
        Built a fully interactive E-commerce Customer Satisfaction Analysis Dashboard to transform raw customer support data into actionable business insights for customer support managers, operations teams, and business stakeholders.
        Implemented comprehensive data cleaning and preprocessing workflows, including duplicate detection, column standardization, date-time conversion, and response-time calculations to ensure accurate and reliable analysis.
        Developed real-time KPI monitoring cards displaying critical customer service metrics such as total complaints, average response time, and average Customer Satisfaction (CSAT) score, enabling quick assessment of support performance.
        Designed an interactive Complaint Channel Distribution Analysis that visualizes the proportion of complaints received through different communication channels, helping organizations understand customer behavior and optimize channel-specific support strategies.
        Created a Top 10 Complaint Sub-Categories Analysis to identify the most frequently reported customer issues, allowing stakeholders to detect recurring problems, prioritize corrective actions, and improve overall service quality.
        Implemented an Agent Shift Workload Analysis that evaluates complaint volumes across different support shifts, helping managers optimize staffing levels, balance workloads, and improve operational efficiency.
        Built responsive and visually engaging interactive Plotly visualizations including pie charts and bar charts, allowing users to explore data patterns and trends more effectively.
        Applied business intelligence and customer analytics techniques to uncover service bottlenecks, measure support team effectiveness, and identify opportunities for process improvement.
        Enhanced user experience through custom HTML and CSS styling, creating professional KPI cards, dashboard layouts, and chart containers that improve readability and accessibility.
        Enabled data-driven decision-making by providing stakeholders with a centralized analytics platform capable of monitoring customer service performance, reducing response times, improving resource allocation, and increasing customer satisfaction.
        Key Business Value

        The dashboard helps organizations answer critical questions such as:

        Which customer support channels receive the highest volume of complaints?
        What are the most common customer issues affecting satisfaction?
        How quickly are support teams responding to customer concerns?
        Which support shifts handle the most complaints?
        What factors may be contributing to lower customer satisfaction scores?
        Where should management focus resources to improve customer experience and operational performance?
   
   - Link: [GitHub / live URL]
 
2. Electricity Generation & Supply in the UK (1920–2024) Dashboard
Project Overview

The Electricity Generation & Supply in the UK (1920–2024) Dashboard is a comprehensive data analytics and business intelligence application developed to explore, analyze, and visualize more than one hundred years of electricity generation and supply data in the United Kingdom. Built using Python and Streamlit, the project transforms historical electricity records from a complex Excel workbook into an interactive analytical platform that enables users to investigate long-term trends in energy production, fuel usage, electricity supply, and the evolution of the UK's energy infrastructure.

The primary objective of the project is to provide a centralized environment where users can explore how the UK's electricity sector has changed over time. By analyzing historical generation data from different energy sources such as coal, oil, natural gas, nuclear power, renewable energy, pumped storage, and other fuels, the dashboard helps users understand the major transitions that have shaped the modern electricity market. The project converts raw datasets into meaningful insights that support strategic planning, historical research, sustainability assessments, and energy policy analysis.

Unlike traditional static reports, the dashboard enables users to dynamically filter and explore data across different time periods, making it possible to compare historical eras, investigate specific decades, and identify long-term trends in electricity generation and supply. This approach transforms historical energy records into actionable information that can be used for research, education, and decision-making.

Target Audience

The dashboard is designed for a wide range of users who require a deeper understanding of electricity generation and energy supply trends. Government agencies and policy makers can use the platform to evaluate the effectiveness of historical energy policies and understand how different energy sources have contributed to the country's electricity supply over time. Researchers and academics can leverage the dashboard to study long-term changes in energy production and examine the impact of technological, economic, and environmental developments on the UK's electricity sector.

Utility companies and energy providers can use the insights generated by the dashboard to better understand historical generation patterns and identify lessons that may influence future energy planning. Sustainability analysts and environmental consultants can evaluate the transition from carbon-intensive fuels such as coal and oil toward lower-carbon alternatives such as nuclear power and renewable energy. Students and aspiring data analysts can also use the project as a learning resource to understand data cleaning, exploratory data analysis, business intelligence, and dashboard development.

The platform serves as both an educational resource and a decision-support system, enabling users to analyze complex energy datasets without requiring advanced technical expertise.

Data Acquisition and Data Sources

The project uses historical electricity generation and supply data stored within an Excel workbook containing multiple sheets. These sheets contain information about electricity generation by source, historical estimates of electricity production, and electricity supplied to consumers over an extended time period spanning from 1920 to 2024.

Because the original datasets are structured primarily for reporting purposes rather than analytical processing, significant data preparation is required before meaningful analysis can take place. The dashboard extracts the relevant worksheets, identifies the appropriate header rows, and restructures the datasets into a format suitable for analysis and visualization.

This process ensures that the information can be efficiently queried, filtered, aggregated, and displayed while maintaining the integrity of the original data.

Data Cleaning and Transformation

One of the most important components of the project is the data cleaning and transformation process. Historical datasets often contain formatting inconsistencies, metadata rows, merged cells, and non-standard column structures that make direct analysis difficult. The dashboard addresses these challenges through a series of preprocessing operations designed to improve data quality and consistency.

The first step involves extracting the correct header row from the dataset and assigning it as the official column structure. Column names are then standardized by converting all characters to lowercase and replacing spaces with underscores. This ensures consistency throughout the application and simplifies future data manipulation tasks.

The project removes unnecessary rows that contain metadata rather than actual observations. It also converts year values into a format suitable for time-series analysis and transforms numerical fields into appropriate numeric data types. These conversions are essential because calculations, aggregations, and visualizations cannot be performed accurately when values are stored as text.

Through these transformations, the dashboard converts a raw historical dataset into a structured analytical dataset that can support complex exploration and reporting activities.

Interactive Filtering System

To enhance usability, the dashboard incorporates an interactive filtering system that allows users to select specific years or ranges of years for analysis. This functionality provides flexibility and enables users to focus on particular periods of interest rather than being restricted to the entire historical dataset.

For example, a user may wish to analyze the dominance of coal during the early twentieth century, examine the growth of natural gas during the late twentieth century, or study the rapid expansion of renewable energy sources during the twenty-first century. By selecting specific years, users can create customized views that reveal patterns and trends relevant to their research objectives.

The filtering mechanism also improves performance and readability by limiting calculations and visualizations to the selected timeframe, ensuring that users receive focused and meaningful insights.

Key Performance Indicators (KPIs)

The dashboard includes a collection of key performance indicators that provide a high-level overview of electricity generation across different energy sources. These metrics summarize large volumes of historical data into concise values that can be interpreted quickly by decision-makers and analysts.

The Total Generation metric represents the cumulative electricity generated during the selected period. Additional metrics provide generation totals for specific energy sources, including coal, oil, natural gas, nuclear power, renewable energy, coke and breeze, pumped storage, and other fuels.

These indicators enable users to compare the relative contributions of different energy sources and understand how the composition of the UK's electricity system has evolved over time. The metrics also help identify dominant fuels during particular periods and reveal broader trends in energy production.

By presenting key information in a concise format, the KPI section acts as a summary layer that supports rapid decision-making and trend identification.

Electricity Generation Share Analysis

One of the central analytical components of the dashboard is the electricity generation share analysis. This section examines how much each energy source contributes to overall electricity generation during the selected time period.

The analysis begins by identifying all variables associated with generation shares and converting them into numerical values suitable for aggregation. The dashboard then calculates the total contribution of each energy source and compares these contributions against the overall electricity generation portfolio.

This analysis enables users to understand the changing balance between fossil fuels, nuclear energy, and renewable technologies. It provides valuable insight into how the UK energy mix has evolved and highlights major shifts in energy policy, technological innovation, and market dynamics.

The results can be used to evaluate historical dependence on specific fuel types, assess diversification efforts, and study the transition toward cleaner energy sources.

Electricity Generation and Supply Trend Analysis

A major feature of the dashboard is the analysis of electricity generation and electricity supply over time. This component investigates the relationship between electricity produced by generators and electricity ultimately supplied to consumers.

The dashboard first extracts and cleans the relevant dataset before calculating a new variable representing the difference between electricity generated and electricity supplied. This difference serves as an indicator of system efficiency and provides insight into potential transmission losses, operational inefficiencies, and other factors affecting electricity delivery.

By examining generation and supply simultaneously, users can gain a deeper understanding of how effectively electricity production is converted into usable energy. Long-term trends can reveal periods of rapid industrial growth, changes in electricity demand, infrastructure expansion, and improvements in system performance.

This analysis is particularly valuable for energy planners, researchers, and policy makers seeking to understand the historical development of the UK electricity network.

Comparative Dataset Validation

An additional feature of the dashboard is the inclusion of both raw and cleaned versions of the datasets used throughout the analysis. This functionality provides transparency and demonstrates the complete data preparation workflow.

Users can compare the original datasets against their cleaned counterparts to understand how data transformation improves analytical quality. This side-by-side comparison highlights the importance of data preprocessing and illustrates the practical challenges associated with working with real-world datasets.

The feature is particularly useful for educational purposes because it allows students and analysts to observe how raw information is transformed into structured data suitable for reporting and visualization.

Business Value and Impact

The dashboard delivers significant value by transforming complex historical electricity records into a user-friendly analytical environment. Rather than manually reviewing large spreadsheets and historical reports, users can interactively explore trends, compare energy sources, and investigate changes in electricity production over time.

The insights generated by the dashboard support evidence-based decision-making in areas such as energy policy, infrastructure planning, sustainability strategy, and academic research. The platform helps stakeholders identify long-term trends, evaluate historical energy transitions, and better understand the factors that have shaped the modern UK electricity system.

By combining historical analysis, data cleaning, performance metrics, and interactive exploration, the project demonstrates how business intelligence tools can convert large datasets into actionable knowledge that supports strategic planning and informed decision-making.

Technology Stack
Programming Language
Python
Data Processing and Analysis
Pandas
NumPy
Data Visualization
Plotly Express
Dashboard Development
Streamlit
Data Source
Microsoft Excel (.xlsx)
Analytical Techniques
Data Cleaning
Data Transformation
Exploratory Data Analysis (EDA)
Time-Series Analysis
Business Intelligence Reporting
Energy Analytics
Historical Trend Analysis
Project Highlights

The project successfully processes and analyzes more than one hundred years of UK electricity generation and supply data, demonstrating the ability to work with large-scale historical datasets. It implements advanced data cleaning and transformation techniques to convert complex spreadsheet data into structured analytical datasets suitable for exploration and reporting.

The dashboard provides dynamic year-based filtering, allowing users to investigate specific historical periods and compare energy trends across different decades. It calculates key performance indicators for multiple energy sources and generates insights into the changing composition of the UK's electricity generation portfolio.

The project also performs comparative analysis between electricity generated and electricity supplied, enabling users to evaluate long-term system efficiency and understand the relationship between production and consumption. By integrating historical analysis, business intelligence methodologies, and interactive dashboard development, the solution demonstrates strong capabilities in data engineering, analytics, visualization, and decision-support system design.

Overall, the project showcases practical expertise in transforming complex real-world datasets into a comprehensive analytical platform that supports research, strategic planning, sustainability analysis, and energy-sector decision-making.
 

3. Personal Income & Expense Tracker Dashboard
Project Overview

The Personal Income & Expense Tracker Dashboard is a full-stack financial management and analytics application developed using Python, Streamlit, Supabase, Pandas, Plotly, and Bcrypt. The primary purpose of the project is to provide individuals with a secure and interactive platform for recording, storing, managing, and analyzing their personal income and expenditure data over time. Unlike traditional spreadsheet-based budgeting systems that require manual calculations and offer limited analytical capabilities, this application combines financial data collection, user authentication, cloud database storage, and interactive visualizations into a single centralized solution.

The system enables users to create secure accounts, log in to a personalized dashboard, record monthly income and expense information, and instantly generate visual insights into their spending habits. By integrating user authentication with a cloud-hosted database, each user's financial records remain isolated and accessible only to the account owner. The application transforms raw financial transactions into meaningful analytics that help users understand how their money is being allocated across various spending categories.

The project was designed to address common personal finance challenges such as budget tracking, expenditure monitoring, savings management, and financial planning. Through the combination of secure data storage and interactive visual analytics, the dashboard allows users to move beyond simple record keeping and gain actionable insights into their financial behavior. This supports better decision-making, improved budgeting practices, and greater financial awareness.

Target Audience

This application is designed for individuals who want to gain greater control over their personal finances and make more informed financial decisions. It is particularly useful for students, working professionals, families, freelancers, and self-employed individuals who need a structured method of monitoring income, expenses, and savings over time.

Students can use the application to manage limited budgets and understand how their spending habits affect their overall financial position. Working professionals can track monthly expenditures, evaluate spending trends, and identify opportunities to improve savings. Freelancers and self-employed individuals can use the platform to monitor irregular income streams and better understand the relationship between earnings and expenditures.

The dashboard is also valuable for anyone seeking to develop stronger budgeting habits. By providing detailed visual representations of spending patterns, the system enables users to identify areas of overspending, evaluate discretionary expenses, and create more sustainable financial plans.

Project Objectives

The primary objective of the project is to provide users with a secure and user-friendly platform for recording financial information and generating meaningful financial insights. The application aims to eliminate the need for manual calculations by automatically processing user-entered data and generating analytical outputs.

Another major objective is to promote financial awareness by helping users understand where their money is being spent and how different expense categories contribute to their overall financial position. By visualizing spending patterns and remaining balances, the system supports more effective financial planning and budgeting.

A further objective is to demonstrate the integration of modern web application development technologies, cloud databases, authentication systems, and business intelligence techniques within a single project.

Application Architecture

The project follows a full-stack architecture that combines a front-end user interface, a backend database service, authentication logic, and analytical processing components.

The front-end is built using Streamlit and serves as the primary interface through which users interact with the system. Users can register accounts, log in, enter financial data, and view visualizations without requiring any technical expertise.

The backend relies on Supabase, which acts as the cloud database responsible for storing user profiles and financial records. Supabase enables persistent data storage, ensuring that information remains available across sessions.

Authentication functionality is implemented using Bcrypt password hashing and encrypted cookies. Passwords are never stored in plain text, significantly improving security. Session management is achieved through encrypted cookies that allow users to remain authenticated between visits.

Pandas performs data processing and transformation tasks, while Plotly is responsible for generating interactive financial visualizations.

User Authentication System

One of the most sophisticated components of the application is the authentication system. The project implements a complete user registration, login, logout, and session restoration workflow.

When a new user registers, the system first verifies that both the email address and username are unique. This prevents duplicate accounts and ensures data integrity. If the information passes validation, the password is encrypted using the Bcrypt hashing algorithm before being stored in the database.

This security mechanism is critical because passwords are never saved in plain text. Even if unauthorized access to the database were to occur, the original passwords would remain protected through cryptographic hashing.

During login, the application retrieves the user's stored password hash and compares it against the entered password using secure hash verification. If authentication succeeds, the user is granted access to the application and a secure session is created.

The project also implements session persistence through encrypted cookies. This means that users remain logged in even after refreshing the browser or returning to the application later. Each session is automatically restored by retrieving the user's unique identifier from the encrypted cookie and validating it against the database.

This feature significantly improves user experience while maintaining a high level of security.

User Registration Process

The registration workflow serves as the entry point for new users.

The process begins when a user enters their first name, last name, username, email address, and password. The application validates the supplied information by checking whether the username or email address already exists in the database.

If a duplicate account is detected, an appropriate error message is displayed to prevent conflicts. If validation succeeds, the password is securely hashed and the user record is inserted into the Supabase database.

This process ensures that every user has a unique identity within the system and that account information is securely stored.

User Login and Session Management

The login process enables users to securely access their financial records.

After entering their credentials, the application retrieves the associated account information and verifies the supplied password. Upon successful authentication, user information is stored in the application state and a secure cookie is generated.

The cookie stores the user's unique identifier, allowing the application to automatically restore the session during future visits. This eliminates the need for repeated logins and creates a seamless user experience.

The logout process reverses this workflow by clearing session data and deleting the authentication cookie.

Income and Expense Data Collection

The core functionality of the application revolves around collecting financial information from users.

A dedicated financial entry form allows users to record a wide variety of income and expenditure categories. These include salary, rent, electricity bills, gas bills, network expenses, car insurance, road tax, public transportation costs, savings contributions, food expenses, clothing purchases, and recreational spending.

Each record is timestamped with a specific date, enabling historical tracking and time-based analysis.

Once submitted, the data is stored within the cloud database and linked directly to the authenticated user's account. This relationship ensures complete data separation between users and guarantees privacy.

The structured nature of the form allows users to consistently categorize expenditures, which significantly improves the quality and usefulness of subsequent analysis.

Financial Data Processing

After retrieving financial records from the database, the application performs extensive data processing and transformation.

The first step involves converting raw database records into a Pandas DataFrame. Date values are transformed into datetime objects to enable time-series analysis and filtering.

The application then calculates a balance value for every financial record. This balance is determined by subtracting the total expenditure categories from the user's salary. This calculation provides an immediate indication of whether income exceeds expenditure.

To facilitate visual analysis, the data is reshaped from a wide format into a long format using data melting techniques. This transformation creates a standardized structure that allows multiple expense categories to be analyzed simultaneously.

Additional date fields are generated to support monthly and yearly filtering.

These preprocessing steps form the analytical foundation of the dashboard and enable all subsequent visualizations.

Interactive Filtering System

The dashboard includes an advanced filtering mechanism that allows users to analyze financial data across different time periods.

Users can select one or more years and one or more months using interactive controls. Based on these selections, the application dynamically filters the dataset and generates visualizations specific to the chosen timeframe.

The filtering logic supports multiple scenarios, including single-month analysis, multi-month analysis, single-year analysis, and multi-year comparisons.

This flexibility enables users to investigate spending patterns over short periods or examine long-term financial trends.

Expenditure Distribution Analysis

One of the primary analytical components of the dashboard is the expenditure distribution analysis.

This analysis examines how total spending is distributed across different expense categories during the selected period. Salary data is intentionally excluded to focus solely on expenditure behavior.

The visualization aggregates all spending categories and calculates their relative contribution to total expenses.

This analysis helps users answer important financial questions such as:

Which category consumes the largest portion of monthly income?
Are utility bills becoming a significant expense?
How much is being spent on discretionary activities?
Which categories offer the greatest opportunities for cost reduction?

The resulting insights help users identify spending habits and make more informed budgeting decisions.

Income and Expenditure Waterfall Analysis

One of the most powerful features of the application is the waterfall analysis.

Unlike traditional charts that simply display totals, a waterfall analysis demonstrates how each financial category contributes to the final balance.

The process begins with total salary income. Each expense category is then sequentially deducted from that income. Finally, the remaining balance is calculated and displayed.

This approach provides a complete financial story, allowing users to see exactly how their income is consumed by different expenditures.

The waterfall analysis answers several important questions:

How much money remains after all expenses?
Which expenses have the greatest impact on financial health?
Are savings contributions sustainable?
Which spending categories should be reduced to improve the final balance?

This makes the visualization particularly valuable for budgeting and financial planning.

Financial Performance Monitoring

The dashboard functions as a personal financial monitoring system by continuously calculating and evaluating user balances.

By comparing income against expenditures, users can determine whether they are operating within their means or overspending. The calculated balance serves as a key performance indicator of financial health.

Positive balances indicate surplus income available for savings or investment, while negative balances highlight potential financial risks.

This capability transforms the application from a simple expense tracker into a practical financial decision-support system.

Database Integration

A major technical achievement of the project is its integration with Supabase.

Rather than storing information locally, all user and financial records are maintained in a cloud-hosted relational database. This enables persistent storage, multi-user support, and secure data access.

The application performs various database operations, including:

User registration
User authentication
Session restoration
Financial record insertion
User-specific data retrieval

This architecture demonstrates full-stack development capabilities and significantly increases the scalability of the solution.

Security Features

Security is a critical aspect of the application.

The project incorporates several security mechanisms including password hashing, encrypted session cookies, authenticated database queries, and user-specific data isolation.

Passwords are encrypted using Bcrypt before being stored in the database. Session data is secured through encrypted cookies, reducing the risk of unauthorized access.

Additionally, all financial data is linked to specific user identifiers, ensuring that users can only access their own records.

These measures create a secure environment suitable for handling sensitive personal financial information.

Technology Stack
Programming Language
Python
Front-End Framework
Streamlit
Database Platform
Supabase
Data Processing and Analysis
Pandas
NumPy
Data Visualization
Plotly Express
Plotly Graph Objects
Authentication & Security
Bcrypt
Encrypted Cookie Manager
Environment Configuration
Python Dotenv
Data Storage
Cloud-Based Relational Database
Analytical Techniques
Personal Finance Analytics
Budget Analysis
Expenditure Tracking
Time-Series Analysis
Data Transformation
Financial Performance Monitoring
Project Highlights

The project successfully combines full-stack web development, cloud database integration, secure user authentication, and business intelligence analytics within a single application. It implements a complete user management system featuring registration, login, logout, encrypted password storage, session persistence, and cookie-based authentication.

The application enables users to record and manage detailed financial information across multiple expenditure categories while maintaining complete data privacy through user-specific database relationships. Advanced data transformation techniques convert raw financial records into analytical datasets that support dynamic filtering and interactive exploration.

The project includes comprehensive expenditure analysis, balance calculations, and waterfall-based financial breakdowns that help users understand how income is allocated across various spending categories. By integrating cloud storage, authentication, financial tracking, and visual analytics, the dashboard demonstrates practical expertise in full-stack development, database management, cybersecurity principles, business intelligence, financial analytics, and user-centered application design.

Overall, the Personal Income & Expense Tracker Dashboard serves as a comprehensive personal finance management solution that empowers users to monitor spending behavior, improve budgeting practices, strengthen financial decision-making, and develop long-term financial awareness through data-driven insights.
 
EXPERIENCE:
- Operations Data Analyst at Romenda Ltd (2024 - Present)
- Digital Ecommerce Entrepreneur at Ebay (2022 – 2025])
- Environmental Impact Assessment(EIA) Officer at Ministry of Environment Cameroon (2019-2020)
- Community Engagement Officer at University of Buea Cameroon (2014 - 2018)
 
EDUCATION:
- Msc in Sustainability and Environmental Management, Coventry University (2020-2022)
- Bsc in Environmental Science, University of Buea (2014-2018)

Licenses and certifications:
-   CITB Health safety and environment For Managers and Professionals
    Construction Skills Certification Scheme (CSCS)
    Issued Sep 2025 · Expires Sep 2030
    Credential ID 15305206
 
-   Data Visualization
    freeCodeCamp
    Issued Oct 2023

-   Front End Development Libraries
    freeCodeCamp
    Issued May 2023

-   Responsive Web Design
    freeCodeCamp
    Issued Dec 2022

    Full UK Driving License: Yes
                
    Access to a personal vehicle: Yes
                
    Visa Sponsorship required: No


### Get to Know Me

Hello, and thank you for stopping by!

I'm a passionate data enthusiast (or as I like to say, a proud data nerd) based in England, United Kingdom, with over three years of experience collecting, cleaning, analyzing, and interpreting data to uncover meaningful insights and support better decision-making. I genuinely enjoy working with data and discovering the stories hidden beneath numbers, patterns, and trends. For me, data is more than just figures on a screen—it's a powerful tool that helps organizations understand where they are today and where they can improve tomorrow.

My academic journey began with a Master of Science (MSc) in Sustainability and Environmental Management, a broad multidisciplinary field focused on integrating sustainability, efficiency, environmental stewardship, and responsible decision-making across organizational processes, operations, and policies. Throughout my studies, I developed a strong understanding of how businesses and institutions can balance economic growth, operational performance, and environmental responsibility to create long-term value for both people and the planet.

However, during my postgraduate studies, I came to an important realization: having expertise in sustainability alone is not enough to drive meaningful change. Decisions that shape organizations, industries, and policies are often guided by data. To effectively influence sustainable decision-making, professionals must possess the technical skills to collect, track, analyze, and evaluate complex datasets. These skills are essential for identifying opportunities for improvement, measuring efficiency and performance, assessing risks, understanding costs versus returns, and uncovering trends that may otherwise go unnoticed. Data provides the evidence needed to justify sustainable initiatives and helps organizations choose systems and strategies that maximize value while preserving environmental integrity for current and future generations.

This realization sparked a deep curiosity and passion for data analytics and data science. I became determined to develop the technical expertise needed to bridge the gap between sustainability and data-driven decision-making. Since then, I have dedicated myself to learning and applying data analytics, statistical analysis, machine learning, and deep learning techniques to solve real-world problems and generate actionable insights.

Over the years, I have completed more than 100 professional, academic, and personal projects covering data analytics, business intelligence, dashboard development, data visualization, reporting, and predictive analytics. Many of these projects are showcased throughout this portfolio and on my GitHub profile, where I continuously share my work, learning journey, and technical growth. Each project represents an opportunity to sharpen my skills, tackle new challenges, and transform raw data into meaningful solutions.

I strongly believe that learning never stops, especially in the ever-evolving world of technology and data. As of today, I continue to invest significant time in expanding my knowledge, staying current with industry best practices, exploring emerging technologies, and learning new programming languages, frameworks, and analytical techniques. Continuous improvement is something I take seriously because I understand that today's innovation quickly becomes tomorrow's standard.

Beyond technical skills, I pride myself on being a hard-working, disciplined, and highly motivated individual. I enjoy thinking creatively, approaching problems from different perspectives, and finding solutions that others may overlook. I have excellent interpersonal skills, am a strong communicator, and consider active listening to be one of my greatest strengths. I am highly detail-oriented, naturally curious, and particularly skilled at identifying patterns, anomalies, and relationships within complex datasets. These qualities allow me to combine analytical thinking with practical problem-solving to deliver meaningful results.

Working with data is genuinely what I love doing. Whether I am building dashboards, developing analytical models, exploring trends, or learning a new technology, I find great satisfaction in turning information into insight. Looking ahead, my long-term goal is to continue growing within the fields of Data Science, Machine Learning, Deep Learning, and Artificial Intelligence, where I hope to leverage advanced analytical techniques to solve increasingly complex challenges and create innovative solutions with real-world impact.

Thank you for taking the time to learn a little more about me. I truly appreciate your interest and hope this portfolio gives you insight into both my technical capabilities and my passion for continuous growth.

As someone once said:

*"A picture can tell a thousand words, but a few words can change its story."*
— Sebastyne Young

If you'd like to connect, collaborate, discuss opportunities, or simply talk about data, sustainability, or technology, please feel free to get in touch.

**Email:** [eguterobson@yahoo.co.uk](mailto:eguterobson@yahoo.co.uk)

I look forward to hearing from you!


---
 
Keep answers concise and friendly. When mentioning a project, always include
its link if one is available. Encourage visitors to explore the other pages
of this portfolio for more detail.


"""

if "SSL_CERT_FILE" in os.environ and not os.path.exists(os.environ["SSL_CERT_FILE"]):
    del os.environ["SSL_CERT_FILE"]

# ── Anthropic client (reads ANTHROPIC_API_KEY from env / Streamlit secrets) ────
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
 
# ── Session state ──────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
 
# ── UI ─────────────────────────────────────────────────────────────────────────
st.title("💬 Chat with my Portfolio")
st.caption(
    "Ask me anything about myself, my projects, skills, or experience. "
    #"Powered by [Claude](https://www.anthropic.com)."
)
 
# Suggested openers — disappear once the conversation starts
if not st.session_state.messages:
    st.markdown("**Try asking:**")
    cols = st.columns(3)
    starters = [
        "What projects have you built?",
        "What's your tech stack?",
        "How can I contact you?",
    ]
    for col, prompt in zip(cols, starters):
        if col.button(prompt, use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.rerun()
 
st.divider()
 
# Render conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
 
# Chat input
if user_input := st.chat_input("Ask something…"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
 
# Generate a reply whenever the last message is from the user
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=1024,
                system=PORTFOLIO_CONTEXT,
                messages=st.session_state.messages,
            )
            reply = response.content[0].text
            st.markdown(reply)
 
    st.session_state.messages.append({"role": "assistant", "content": reply})
 
# Clear conversation button (sidebar)
with st.sidebar:
    st.markdown("### Options")
    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown(
        "This chatbot only knows what's in my portfolio. "
        "For anything else, [get in touch](mailto:your@email.com)."
    )