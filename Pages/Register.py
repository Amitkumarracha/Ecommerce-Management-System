import streamlit as st
from passlib.hash import sha256_crypt
import mysql.connector as sql


def register():
    # Connection parameters
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'sit123'  # Replace with your actual password
    db_name = 'ecommerce_m_s'

    # Establish a connection
    connection = sql.connect(
        host=db_host,
        user=db_user,
        passwd=db_password,
        db=db_name
    )
    cursor = connection.cursor()
    st.subheader("Register")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    role = st.selectbox("Role", ("Customer", "Seller"))

    if st.button("Register"):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            st.error("User already exists. Please log in.")
        else:
            hashed_password = sha256_crypt.hash(password)
            cursor.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)",
                           (name, email, hashed_password, role))
            connection.commit()

            st.success("Registration successful. You can now log in.")

        cursor.close()


# Function for user login
def login():
    # Connection parameters
    db_host = 'localhost'

    db_user = 'root'
    db_password = 'sit123'  # Replace with your actual password
    db_name = 'ecommerce_m_s'

    # Establish a connection
    connection = sql.connect(
        host=db_host,

        user=db_user,
        passwd=db_password,
        db=db_name
    )
    cursor = connection.cursor()
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
        user = cursor.fetchone()

        if user:
            hashed_password = user[3]  # Assuming 'password' is the fourth column
            if sha256_crypt.verify(password, hashed_password):
                st.success("Login successful")
                st.write(f"Welcome to ShopEase , Mr/Mrs {user[1]}  !")
                st.write(f"Your {user[4]} Id is {user[0]}")

                st.session_state["Name"] = user[1]
                st.session_state["Login"] = user[4]
                st.session_state["Id"] = user[0]

                return user  # Return the user record
            else:
                st.error("Invalid login. Please check your credentials.")
        else:
            st.error("User not found. Please register first.")
    return None


with st.sidebar:
    selected_option = st.radio("Select an Option", ["Register", "Login"])

if selected_option == "Register":
    register()
else:
    user = login()