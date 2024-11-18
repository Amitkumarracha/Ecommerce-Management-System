import streamlit as st

# Initialize session state
if "Name" not in st.session_state:
    st.session_state["Name"] = ""
if "Login" not in st.session_state:
    st.session_state["Login"] = ""
if "Id" not in st.session_state:
    st.session_state["Id"] = ""

# Set a title for your site
st.title("🛍️ ShopEase - E-commerce Management System")

# Inspirational Story Section
st.markdown(
    """
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);'>
        <h4 style='color: #ff5733;'>Our Inspiring Journey</h4>
        <ul style='color: #555;'>
            <li>In the heart of the digital world, three dedicated developers—Amitkumar Racha, Bhoomika Kapde, and Aryan Revankar—shared a vision to transform the online shopping experience.</li>
            <li>Driven by the challenges faced by small businesses in managing inventory, tracking sales, and handling customer data, they envisioned an all-in-one platform that could simplify e-commerce management.</li>
            <li>They spent months designing and refining their ideas, eventually creating ShopEase, a robust and user-friendly e-commerce management system.</li>
            <li>Today, they are thrilled to empower business owners to manage their stores efficiently, allowing them to focus on growth and customer satisfaction.</li>
            <li>Join us as we make online retail management smarter, simpler, and more effective!</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)

# LinkedIn Profiles Section
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px;'>
        <h4 style='color: #ff5733;'>Connect with Us on LinkedIn</h4>
        <p>Follow our team for updates and insights:</p>
        <a href="https://www.linkedin.com/in/amitkumar-racha-2003akr" target="_blank" style="color: #ff5733;">Amitkumar Racha</a> | 
        <a href="https://www.linkedin.com/in/bhoomika-kapde-478731285" target="_blank" style="color: #ff5733;">Bhoomika Kapde</a> | 
        <a href="https://www.linkedin.com/in/aryan-revankar-337957243" target="_blank" style="color: #ff5733;">Aryan Revankar</a>
    </div>
    """, unsafe_allow_html=True
)

# Team Photos Section using st.image()
st.markdown(
    """
    <div style='text-align: center; margin-top: 40px;'>
        <h4 style='color: #ff5733;'>Meet Our Team</h4>
    </div>
    """, unsafe_allow_html=True
)

# Display team photos with st.image()
col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/amit.jpg", caption="Amitkumar Racha", width=200)

with col2:
    st.image("images/bhoomika.jpg", caption="Bhoomika Kapde", width=200)

with col3:
    st.image("images/aryan.jpg", caption="Aryan Revankar", width=200)

# Optional Footer
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px;'>
        <p style='color: #555;'>ShopEase - E-commerce Management System © 2024</p>
    </div>
    """, unsafe_allow_html=True
)
