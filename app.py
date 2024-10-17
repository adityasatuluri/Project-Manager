import streamlit as st
from views.new_project import new_project_page
from views.projects_list import projects_list_page
from database import get_database
from utils import hash_password, verify_password

# Set page config
st.set_page_config(
    page_title="Project Management App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define refined color palette
colors = {
    "background": "#0D1117",
    "surface": "#161B22",
    "primary": "#6E40C9",
    "secondary": "#30363D",
    "text": "#C9D1D9",
    "text_secondary": "#8B949E",
    "border": "#30363D",
    "success": "#2EA043",
    "warning": "#D29922",
    "error": "#F85149",
}

# Custom CSS with refined Stract-inspired design
st.markdown(f"""
<style>
    :root {{
        --background-color: {colors['background']};
        --surface-color: {colors['surface']};
        --primary-color: {colors['primary']};
        --secondary-color: {colors['secondary']};
        --text-color: {colors['text']};
        --text-secondary-color: {colors['text_secondary']};
        --border-color: {colors['border']};
    }}
    
    .stApp {{
        background-color: var(--background-color);
        color: var(--text-color);
    }}
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {{
        background-color: var(--surface-color);
        color: var(--text-color);
        border: 1px solid var(--border-color);
        border-radius: 6px;
    }}
    
    .stTextInput > label,
    .stTextArea > label,
    .stSelectbox > label {{
        color: var(--text-secondary-color);
    }}
    
    .stButton > button {{
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }}
    
    .stButton > button:hover {{
        background-color: var(--primary-color);
        opacity: 0.8;
    }}
    
    .stSidebar {{
        background-color: var(--surface-color);
        border-right: 1px solid var(--border-color);
    }}
    
    .stSidebar .stRadio > label {{
        color: var(--text-secondary-color);
    }}
    
    [data-testid="stMetricValue"] {{
        background-color: var(--surface-color);
        border: 1px solid var(--border-color);
        border-radius: 6px;
        padding: 1rem;
        color: var(--text-color);
    }}
    
    [data-testid="stMetricLabel"] {{
        color: var(--text-secondary-color);
    }}
    
    h1, h2, h3, h4, h5, h6 {{
        color: var(--text-color);
    }}
    
    .stAlert {{
        background-color: var(--surface-color);
        border: 1px solid var(--border-color);
        color: var(--text-color);
        border-radius: 6px;
    }}
    
    .stSuccess {{
        border-left-color: {colors['success']};
    }}
    
    .stWarning {{
        border-left-color: {colors['warning']};
    }}
    
    .stError {{
        border-left-color: {colors['error']};
    }}
    
    .stDateInput > div > div > input {{
        background-color: var(--surface-color);
        color: var(--text-color);
        border: 1px solid var(--border-color);
        border-radius: 6px;
    }}
    
    .stSelectbox > div > div > div {{
        background-color: var(--surface-color);
        color: var(--text-color);
        border: 1px solid var(--border-color);
        border-radius: 6px;
    }}
    
    .stCheckbox > label > div[role="checkbox"] {{
        background-color: var(--surface-color) !important;
        border-color: var(--border-color) !important;
    }}
    
    .stCheckbox > label > div[role="checkbox"]::before {{
        background-color: var(--primary-color) !important;
    }}
    .stExpander {{
        color:white;
        background-color: #161b22;
    }}
</style>
""", unsafe_allow_html=True)

# Rest of your Streamlit app code goes here

# Hide Streamlit default elements
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Rest of your application code remains the same
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