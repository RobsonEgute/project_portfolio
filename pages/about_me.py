import streamlit as st
import base64
import os

st.set_page_config(
    page_title="About Me",
    page_icon="👤",
    layout="wide"
)


st.markdown("""
    <style>
        /* Background colour */
        .stApp {
            background-color: #1e1e2e;
        }

        /* Main text colour */
        html, body, [class*="css"] {
            color: #ffffff;
        }

        /* Sidebar background */
        [data-testid="stSidebar"] {
            background-color: #2e2e3e;
        }

        /* Sidebar text */
        [data-testid="stSidebar"] * {
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown(
    """
    <h1 style="text-align: center; ">
        About Me
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: black-grey;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def get_base64_image(image_path):
    if os.path.exists(image_path):
        print(f"Image found at: {image_path}")
        with open(image_path, "rb") as image_bin_file:
            return base64.b64encode(image_bin_file.read()).decode()
    return None

profile_image_path = "images/robson_egute.jpg"

profile_image_base64 = get_base64_image(profile_image_path)



st.markdown(
    f"""
    <div style="text-align: center;">
        <img 
            src="data:image/jpeg;base64,{profile_image_base64}"
            width="400px"
            style="
                border-radius: 50%;
                border: 3px solid grey;
                object-fit: cover;
                aspect-ratio: 1/1;
            "
        />
        <h3 class="h2_text" id="about_me_name">Hi, am Robson Egute!</h3>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
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
    """)

with col2:
    st.markdown("""
### Technical skills
- Python(Numpy, Pandas, Plotly, Matplotlib, Streamlit, Bcrypt, Seaborn)
- JavaScript(React, Redux, Bootstrap, Tailwind, Express)
- HTML
- CSS
- Git/Git-Hub
- SQL
- Database: Supabase, MongoDB, MYSQL, POSTGRESQL
- Microsoft Excel, Powerpoint, Word
- Microsoft PowerBI
- Libreoffice Calc
- Pivot tables
- VsCode
- Data cleaning
    
### Full UK Driving License: Yes
            
### Access to a personal vehicle: Yes
            
### Sponsorship required: No
                
## EDUCATION:
- Msc in Sustainability and Environmental Management, Coventry University (2020-2022)
- Bsc in Environmental Science, University of Buea (2014-2018)

## Licenses and certifications:
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
                
## EXPERIENCE:
- Operations Data Analyst at Romenda Ltd (2024 - Present)
- Digital Ecommerce Entrepreneur at Ebay (2022 – 2025])
- Environmental Impact Assessment(EIA) Officer at Ministry of Environment Cameroon (2019-2020)
- Community Engagement Officer at University of Buea Cameroon (2014 - 2018)
                
    """)
