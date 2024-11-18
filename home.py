import streamlit as st
import mysql.connector as sql

st.set_page_config(page_title="E-Commerce Management System", layout="wide")


# Establish a connection
connection = sql.connect(
    host='localhost',
    user='root',
    password='sit123'
)


# Banner Image (Optional)
# Uncomment the line below if you have an image banner for the home page
# banner_image = Image.open("path/to/banner_image.jpg")
# st.image(banner_image, use_column_width=True)


st.session_state['connection'] = connection
# --- Page Setup ---

home_page = st.Page(
    page="./Pages/Home_Page.py",
    title="🏠 Welcome to E-Commerce Management System",
    default=True
)

about_page = st.Page(
    page="./Pages/About.py",
    title="👥 About Us - Our Story"
)

register_page = st.Page(
    page="./Pages/Register.py",
    title="📝 Register & Get Started"
)

actions_page = st.Page(
    page="./Pages/Action.py",
    title="Shop Ease Dashboard"
)


# --- Navigation ---

pg = st.navigation({
    "Home" : [home_page],
    "Login/Register" : [register_page],
    "Features":[actions_page],
    "Info": [about_page]
    })

pg.run()
