import streamlit as st

# Session state for storing user data
st.session_state["Name"] = ""
st.session_state["Login"] = ""
st.session_state["Id"] = ""

# Header section with logo and title
col1, col4, col2, col3 = st.columns([1, 0.3, 5, 2])
with col1:
    print()

with col2:
    st.write(" ")
    st.write(" ")
    st.title("🛍️ ShopEase - E-commerce Management System")  # Adjust this title to fit your eCommerce brand
    st.subheader("Your destination for a seamless shopping experience")

st.text(" ")
st.text("")

# Introduction to the website
st.write(
)

#st.write(
 #   "Shop with us and discover the convenience and joy of finding everything you need in one place. "
  #  "With personalized recommendations, secure payments, and efficient delivery, ShopEase is here to redefine the way you shop online."
#)

# Introduction Section
st.markdown(
    """
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);'>
        <h5 style='color: #333;'>Welcome to ShopEase - E-Commerce Management System!</h5>
        <p style='color: #555;'>Effortlessly manage your product inventory, track sales, and fulfill customer orders. 
        Our platform streamlines e-commerce management, empowering you to grow your business and provide exceptional service to your customers.</p>
    </div>
    """, unsafe_allow_html=True
)

st.write("---")

# Section explaining why customers should choose this site
col1, _, col2 = st.columns([5, 0.3, 3])
with col1:
    st.header("Why Shop with Us?")
    st.write(
        "Shopping with ShopEase is all about comfort, quality, and convenience. Here are the key reasons why we're your go-to shopping platform:"
    )
    st.markdown("1. Wide Product Selection")
    st.markdown("2. Unmatched Quality and Prices")
    st.markdown("3. Secure Payment Options")
    st.markdown("4. Fast and Reliable Delivery")
    st.markdown("5. Exceptional Customer Service")

    st.write("---")

with col2:
    st.write(" ")
    st.write(" ")
    st.image("./images/delllaptop.jpg", width=300)  # Image representing customer benefits

# Section highlighting competitive advantage
st.header("Our Advantage")
col3, col1 = st.columns(2)
with col3:
    st.write(" ")
    st.write(" ")
    st.image("./images/images.jpg")  # Image highlighting competitive advantage

with col1:
    st.header("Why We're Ahead")
    st.write(
        "To offer you the best, we've analyzed other eCommerce platforms and ensured that ShopEase excels in the areas that matter most to you."
    )
    st.subheader("Competitor X")
    st.write("Pros: Well-known brand, good selection.")
    st.write("Cons: Higher prices, limited customer support.")
    st.subheader("Competitor Y")
    st.write("Pros: Competitive pricing, wide range of products.")
    st.write("Cons: Slow delivery, limited payment options.")
    st.subheader("ShopEase")
    st.write(
        "Pros: Extensive product variety, fast delivery, secure payments, personalized recommendations, and 24/7 customer support."
    )
    st.write("Cons: None!")

st.write("---")

# Key features of the platform
st.header("Key Features")
st.write("Discover the amazing features that make ShopEase the ultimate shopping platform:")
st.write("- Easy Browsing and Product Search")
st.write("- Personalized Product Recommendations")
st.write("- Secure Payment Options")
st.write("- Fast, Reliable Delivery")
st.write("- 24/7 Customer Support")

st.write(
    "We've also added a chatbot to assist you with any questions and help you find the products you need quickly and easily. "
    "Start exploring ShopEase and enjoy a seamless shopping experience like never before!"
)