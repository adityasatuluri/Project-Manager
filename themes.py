# themes.py

def apply_custom_css():
    return """
    <style>
    /* Main app styles */
    .stSideBar {
        background-color: #0D1117;
        color: #C9D1D9;
    }

    /* Sidebar styles */
    .stSidebar {
        background-color: #161B22;
    }

    /* Headers */
    h1, h2, h3 {
        color: #58A6FF;
    }

    /* Buttons */
    .stButton > button {
        background-color: #238636;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        font-size: 1rem;
    }

    .stButton > button:hover {
        background-color: #2EA043;
    }

    /* Input fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #161B22;
        color: #C9D1D9;
        border: 1px solid #30363D;
    }

    /* Select boxes */
    .stSelectbox > div > div > select {
        background-color: #161B22;
        color: #C9D1D9;
        border: 1px solid #30363D;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: #161B22;
        color: #C9D1D9;
    }

    /* Project container */
    .project-container {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 4px;
        padding: 1rem;
        margin-bottom: 1rem;
    }

    .project-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }

    .project-name {
        font-size: 1.2rem;
        font-weight: bold;
        color: #58A6FF;
    }

    .project-status {
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.9rem;
    }

    .project-details {
        display: flex;
        justify-content: space-between;
    }

    .detail-label {
        font-weight: bold;
        color: #8B949E;
    }

    /* Metrics */
    .stMetric {
        background-color: #161B22;
        padding: 1rem;
        border-radius: 4px;
    }

    .stMetric label {
        color: #8B949E;
    }

    .stMetric .metric-value {
        color: #58A6FF;
        font-size: 1.5rem;
    }
    </style>
    """

def apply_custom_css2():
    return """
    <style>
    /* Main app styles */
    * {
        background-color: #0D1117;
        color: white;
    }

    /* Sidebar styles */
    .stSidebar {
        background-color: #161B22;
    }

    /* Headers */
    h1, h2, h3 {
        color: #58A6FF;
    }

    /* Buttons */
    .stButton > button {
        background-color: #238636;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        font-size: 1rem;
    }

    .stButton > button:hover {
        background-color: #2EA043;
    }

    /* Input fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #161B22;
        color: #C9D1D9;
        border: 1px solid #30363D;
    }

    /* Select boxes */
    .stSelectbox > div > div > select {
        background-color: #161B22;
        color: #C9D1D9;
        border: 1px solid #30363D;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: #161B22;
        color: #C9D1D9;
    }

    /* Project container */
    .project-container {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 4px;
        padding: 1rem;
        margin-bottom: 1rem;
    }

    .project-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }

    .project-name {
        font-size: 1.2rem;
        font-weight: bold;
        color: #58A6FF;
    }

    .project-status {
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.9rem;
    }

    .project-details {
        display: flex;
        justify-content: space-between;
    }

    .detail-label {
        font-weight: bold;
        color: #8B949E;
    }

    /* Metrics */
    .stMetric {
        background-color: #161B22;
        padding: 1rem;
        border-radius: 4px;
    }

    .stMetric label {
        color: #8B949E;
    }

    .stMetric .metric-value {
        color: #58A6FF;
        font-size: 1.5rem;
    }
    </style>
    """