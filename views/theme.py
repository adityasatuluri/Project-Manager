import streamlit as st

def github_dark_theme():
    st.markdown("""
    <style>
    /* General App Background */
    body {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stApp {
        background-color: #0d1117;
    }

    /* Containers Background */
    .css-1d391kg {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #f0f6fc;
    }

    /* Input elements (text, text area, etc.) */
    input, textarea {
        background-color: #161b22;
        color: #c9d1d9;
        border: 1px solid #30363d;
    }
    
    /* Dropdowns and selection elements */
    .stMultiSelect, .stSelectbox {
        background-color: #161b22;
        color: #c9d1d9;
        border: 1px solid #30363d;
    }

    /* Buttons */
    .stButton>button {
        background-color: #238636;
        color: white;
        border-radius: 5px;
        border: none;
    }

    /* Expander Header */
    .st-expanderHeader {
        background-color: #161b22;
        color: #c9d1d9;
        border-bottom: 1px solid #30363d;
    }

    /* Status labels */
    .project-status {
        font-weight: bold;
        padding: 5px 10px;
        border-radius: 5px;
        color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True)
