import streamlit as st
import mysql.connector as sql

# --- Database Connection Function ---
def get_db_connection():
    """Connect to the MySQL database and return the connection and cursor."""
    try:
        connection = sql.connect(
            host='localhost',
            user='root',
            passwd='sit123',  # Replace with your actual password
            database='Ecommerce_M_S'
        )
        cursor = connection.cursor()
        return connection, cursor
    except sql.Error as e:
        st.error(f"Database connection error: {e}")
        return None, None


# --- Customer Actions ---
def customer_actions():
    st.title("Welcome to ShopEase - Customer Portal")

    # Fetch Categories
    connection, cursor = get_db_connection()
    if not cursor:
        return

    # Fetch categories for dropdown
    try:
        cursor.execute("SELECT category_id, category_name FROM Categories")
        categories = cursor.fetchall()
    except sql.Error as e:
        st.error(f"Error fetching categories: {e}")
        return

    if categories:
        # Category selection dropdown
        category_names = [category[1] for category in categories]
        selected_category = st.selectbox("Browse Categories", category_names)
        selected_category_id = [cat[0] for cat in categories if cat[1] == selected_category][0]

        # Fetch and display products based on selected category
        try:
            cursor.execute("""
                SELECT product_name, description, price, stock
                FROM Products
                WHERE category_id = %s
            """, (selected_category_id,))
            products = cursor.fetchall()

            if products:
                for product in products:
                    st.write(f"**{product[0]}**")
                    st.write(f"Description: {product[1]}")
                    st.write(f"Price: ₹{product[2]}")
                    st.write(f"Stock Available: {product[3]}")
                    if st.button(f"Add to Cart - {product[0]}"):
                        st.success(f"Added {product[0]} to your cart!")
            else:
                st.write("No products available in this category.")
        except sql.Error as e:
            st.error(f"Error fetching products: {e}")
        finally:
            connection.close()

    else:
        st.write("No categories available.")

    # Cart and Order History placeholders
    st.subheader("Your Cart")
    st.write("Your cart is empty.")  # You can integrate this with actual cart data.

    st.subheader("Order History")
    st.write("No past orders.")  # You can integrate this with actual order history data.

    st.subheader("Track Your Orders")
    st.write("No orders to track.")  # Placeholder, can be replaced with order tracking logic.


# --- Seller Actions ---
def seller_actions():
    st.header("Seller Dashboard - Manage Inventory and Orders")

    # Fetch Categories for adding products
    category_options = get_category_options()
    if not category_options:
        return  # Exit if no categories are found

    # Add New Product
    st.subheader("Add New Product")
    product_name = st.text_input("Product Name")
    description = st.text_area("Description")
    price = st.number_input("Price", min_value=0.0)
    stock = st.number_input("Stock Quantity", min_value=0, step=1)
    category_name = st.selectbox("Category", list(category_options.keys()))

    if st.button("Add Product"):
        category_id = category_options[category_name]
        add_product(category_id, product_name, description, price, stock)

    # Display Inventory
    st.subheader("Inventory")
    display_inventory()

    # Display Orders
    st.subheader("Orders")
    display_orders()


# --- Utility Functions ---
def get_category_options():
    """Retrieve categories for selection in the seller's product addition."""
    connection, cursor = get_db_connection()
    if not cursor:
        return None
    try:
        cursor.execute("SELECT category_id, category_name FROM Categories")
        categories = cursor.fetchall()
        return {name: id for id, name in categories}
    except sql.Error as e:
        st.error(f"Error fetching categories for selectbox: {e}")
        return None
    finally:
        connection.close()


def add_product(category_id, product_name, description, price, stock):
    """Add a new product to the inventory."""
    connection, cursor = get_db_connection()
    if not cursor:
        return
    try:
        cursor.execute("""
            INSERT INTO Products (category_id, product_name, description, price, stock)
            VALUES (%s, %s, %s, %s, %s)
        """, (category_id, product_name, description, price, stock))
        connection.commit()
        st.success(f"{product_name} added to inventory!")
    except sql.Error as e:
        st.error(f"Error adding product: {e}")
    finally:
        connection.close()


def display_inventory():
    """Display inventory for the seller."""
    connection, cursor = get_db_connection()
    if cursor:
        try:
            cursor.execute("""
                SELECT P.product_name, P.description, P.price, P.stock, C.category_name 
                FROM Products P
                JOIN Categories C ON P.category_id = C.category_id
            """)
            inventory = cursor.fetchall()
            if inventory:
                for product_name, description, price, stock, category_name in inventory:
                    st.write(f"{product_name} - {category_name} - ₹{price} - {stock} in stock")
            else:
                st.write("No products in inventory.")
        except sql.Error as e:
            st.error(f"Error fetching inventory: {e}")
        finally:
            connection.close()


def display_orders():
    """Display orders for the seller."""
    connection, cursor = get_db_connection()
    if cursor:
        try:
            cursor.execute("""
                SELECT O.order_id, O.order_date, O.total_amount, OD.shipping_status
                FROM Orders O
                JOIN Order_Details OD ON O.order_id = OD.order_id
            """)
            orders = cursor.fetchall()
            if orders:
                for order_id, order_date, total_amount, shipping_status in orders:
                    st.write(
                        f"Order ID: {order_id} | Date: {order_date} | Total: ₹{total_amount} | Status: {shipping_status}")
            else:
                st.write("No orders found.")
        except sql.Error as e:
            st.error(f"Error fetching orders: {e}")
        finally:
            connection.close()



# --- Main Application ---
if "Login" not in st.session_state:
    st.session_state["Login"] = ""
    st.error("Please Login to Continue")
elif st.session_state["Login"] == "Customer":
    customer_actions()
elif st.session_state["Login"] == "Seller":
    seller_actions()
else:
    st.error("Please Login to Continue")
