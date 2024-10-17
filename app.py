import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
from views.new_project import new_project_page
from views.projects_list import projects_list_page
from database import get_database
from utils import hash_password, verify_password
from themes import apply_custom_css
from datetime import datetime, timedelta
import os


try:
    st.set_page_config(
        page_title="Project Management App",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Initialize EncryptedCookieManager with password and a prefix
    cookies = EncryptedCookieManager(
        prefix="project_manager", 
        password=os.getenv("COOKIE_SECRET", "your_secret_password")  # Use env variable for better security
    )

    # Stop execution if cookies are not ready
    if not cookies.ready():
        st.stop()


    st.markdown(apply_custom_css(), unsafe_allow_html=True)

    # Function to set cookies with a 5-day expiration
    def set_session_cookie(name, value):
        expiration_time = datetime.now() + timedelta(days=5)
        cookies[name] = value
        cookies[f"{name}_expires_at"] = expiration_time.strftime('%Y-%m-%d %H:%M:%S')
        cookies.save()

    # Function to get a session cookie and check if it is valid
    def get_session_cookie(name):
        expiration_str = cookies.get(f"{name}_expires_at", None)
        if expiration_str:
            expiration_time = datetime.strptime(expiration_str, '%Y-%m-%d %H:%M:%S')
            if expiration_time > datetime.now():
                return cookies.get(name)
            else:
                st.warning(f"Session for {name} has expired.")
                cookies.pop(name, None)  # Remove expired cookie
                cookies.pop(f"{name}_expires_at", None)
                cookies.save()
        return None

    # Main application logic
    def main():
        try:
            if 'logged_in' not in st.session_state:
                st.session_state.logged_in = False

            # Check if a valid session exists in cookies
            stored_username = get_session_cookie("username")
            if stored_username:
                st.session_state.logged_in = True
                st.session_state.username = stored_username

            if not st.session_state.logged_in:
                login()
            else:
                st.logo("MENU.svg")
                show_main_app()
        except Exception as e:
            print(f"Exception at main: {e}")
            st.rerun()

    # Login function
    def login():
        try:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown(f"""<h2 style="padding-bottom:7vh;">Welcome to Project Manager</h2>""", unsafe_allow_html=True)

                username = st.text_input("Username")
                password = st.text_input("Password", type="password")

                if st.button("Login / Register", key="login"):
                    db = get_database()
                    user = db.users.find_one({"username": username})

                    if user and verify_password(password, user['password']):
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        set_session_cookie("username", username)  # Store session in cookies
                        st.success("Logged in successfully!")
                        st.rerun()
                    elif user:
                        st.error("Incorrect password")
                    else:
                        hashed_password = hash_password(password)
                        db.users.insert_one({"username": username, "password": hashed_password})
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        set_session_cookie("username", username)  # Store new session in cookies
                        st.success("New account created and logged in successfully!")
                        st.rerun()
        except Exception as e:
            print(f"Exception at login: {e}")
            st.rerun()

    # Show main application
    def show_main_app():
        try:
            st.sidebar.title(f"Welcome, {st.session_state.username}!")
            page = st.sidebar.radio("Navigate", ["📊 Dashboard", "🆕 New Project", "📋 Projects List"])

            if page == "📊 Dashboard":
                show_dashboard()
            elif page == "🆕 New Project":
                new_project_page()
            elif page == "📋 Projects List":
                projects_list_page()

            if st.sidebar.button("Logout"):
                st.session_state.logged_in = False
                cookies.pop("username", None)  # Remove session cookie
                cookies.pop("username_expires_at", None)
                cookies.save()
                st.rerun()
        except Exception as e:
            print(f"Exception at show_main_app: {e}")
            st.rerun()

    # Show dashboard
    def show_dashboard():
        try:
            st.title("📊 Project Dashboard")
            db = get_database()
            projects = list(db.projects.find({"created_by": st.session_state.username}))

            total_projects = len(projects)
            completed_projects = sum(1 for p in projects if p['status'] == 'Completed')
            ongoing_projects = sum(1 for p in projects if p['status'] == 'In Progress')
            not_started_projects = sum(1 for p in projects if p['status'] == 'Not Started')

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Projects", total_projects)
            col2.metric("Completed", completed_projects)
            col3.metric("In Progress", ongoing_projects)
            col4.metric("Not Started", not_started_projects)

        except Exception as e:
            print(f"Exception at show_dashboard: {e}")
            st.rerun()

    # Run the main function
    if __name__ == "__main__":
        main()
except Exception as e:
    print(f"Exception at APP: {e}")
    st.rerun()