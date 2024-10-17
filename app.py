import streamlit as st
from views.new_project import new_project_page
from views.projects_list import projects_list_page
from database import get_database
from utils import hash_password, verify_password

st.set_page_config(
    page_title="Project Management App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


st.markdown("""
                <style>
                * {
                    background-color: #0d1117;
                    color: white; /* Ensure text is always white */
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                }
                .stTextInput {
                    color: white; /* Text inside input areas is white */
                    border: 1px solid #30363d;
                    padding: 10px;
                    border-radius: 6px;
                }
                .stButton button {
                    background-color: #F8331D;
                    border: none;
                    color: white;
                    padding: 6px 16px;
                    text-align: center;
                    font-size: 14px;
                    cursor: pointer;
                    border-radius: 6px;
                    width: 100%; /* Make the button fill the container */
                }
                .stButton button:hover {
                    background-color: white;
                    color: #89251A; /* Ensure the text remains dark red instead of black */
                }
                .stExpander {
                    border: 1px solid #30363d;
                    border-radius: 6px;
                    box-shadow: 0 1px 3px rgba(27,31,35,.12);
                }
                .stTextInput, .stTextArea {
                    border: 1px solid #30363d;
                    color: white; /* Text inside text areas is white */
                    border-radius: 6px;
                }
                .stTextArea textarea {
                    border: 1px solid #30363d;
                    color: white; /* Text inside textarea is white */
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                }
                h3 {
                    background-color: #0d1117;
                    color: white;
                }

                </style>
                """, unsafe_allow_html=True)

st.markdown("""
    <style>
    .stTextInput > label {
        background-color: transparent;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login()
    else:
        show_main_app()

def login():
    st.markdown("<h1 style='text-align: center;'>Welcome to Project Manager</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<h3 style='text-align: center;'>Login</h3>", unsafe_allow_html=True)
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login", key="login"):
            db = get_database()
            user = db.users.find_one({"username": username})

            if user and verify_password(password, user['password']):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Logged in successfully!")
                st.experimental_rerun()
            elif user:
                st.error("Incorrect password")
            else:
                if st.button("Create New Account"):
                    hashed_password = hash_password(password)
                    db.users.insert_one({"username": username, "password": hashed_password})
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("New account created and logged in successfully!")
                    st.experimental_rerun()

def show_main_app():
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
        st.experimental_rerun()

def show_dashboard():
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

    # Add more visualizations if needed

if __name__ == "__main__":
    main()
