import streamlit as st

st.title("Contact Me", text_alignment="center")

st.info("Whether you're an employer looking for a dedicated professional, a business with a project in mind, or simply someone who wants to collaborate — I'd love to hear from you. " \
"No request is too big or too small. Fill out the contact form below or you can eamil me at eguterobson@yahoo.co.uk and I'll get back to you as soon as possible. Let's make something great together.")

st.markdown(
    """
        <form action="https://formsubmit.co/eguterobson@yahoo.co.uk" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="name" required>
            <input type="email" name="email" placeholder="email" required>
            <input type="message" name="message" placeholder="message" required>
            <button type="submit">Send</button>
        </form>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=DM+Serif+Display&display=swap');

form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  width: 100%;
  min-height: 520px;
  background: #3a3a3a;
  border: 1px solid #555555;
  border-radius: 12px;
  padding: 3rem 2.5rem;
  box-shadow: 0 4px 24px rgba(0,0,0,0.3);
  font-family: 'DM Sans', sans-serif;
  margin: 0 auto;
}

form input[type="text"],
form input[type="email"],
form input[type="message"] {
  width: 100%;
  padding: 0.9rem 1rem;
  border: 1px solid #666666;
  border-radius: 6px;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.95rem;
  font-weight: 300;
  color: #ffffff;
  background: #4a4a4a;
  transition: border-color 0.15s, box-shadow 0.15s, background 0.15s;
  outline: none;
  appearance: none;
}

form input::placeholder {
  color: #ffffff;
}

form input[type="text"]:focus,
form input[type="email"]:focus,
form input[type="message"]:focus {
  border-color: #4f46e5;
  background: #555555;
  box-shadow: 0 0 0 3px rgba(79,70,229,0.3);
}

form button[type="submit"] {
  padding: 1rem 1.5rem;
  background: #4f46e5;
  color: #ffffff;
  font-family: 'DM Sans', sans-serif;
  font-size: 1rem;
  font-weight: 500;
  letter-spacing: 0.03em;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.15s, transform 0.1s;
  width: 100%;
  margin-top: auto;
}

form button[type="submit"]:hover {
  background: #4338ca;
}

form button[type="submit"]:active {
  transform: translateY(1px);
}
</style>
""", unsafe_allow_html=True)