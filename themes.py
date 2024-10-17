def apply_custom_css():
    return """
    <style>
    /* Main app styles */
    .stApp {
        background-color: none;
        color: none;
    }

    /* Sidebar styles */
    .stSideBar {
        background-color: none;
    }

    /* Headers */
    h1, h2, h3 {
        color: none;
    }

    /* Buttons */
    .stButton > button {
        background-color: #014746;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        font-size: 1rem;
    }

    .stButton > button:hover {
        background-color: none;
    }

    /* Input fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: none;
        color: none;
        border: 1px solid none;
    }

    /* Select boxes */
    .stSelectbox > div > div > select {
        background-color: none;
        color: none;
        border: 1px solid none;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: none;
        color: none;
    }

    /* Project container */
    .project-container {
        background-color: none;
        border: 1px solid none;
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
        color: none;
    }

    .project-status {
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.9rem;
    }

    .project-details {
        display: grid;
        grid-template-columns: 1fr 1fr; /* Two equal-width columns */
        gap: 0.8rem; /* Spacing between elements */
        margin-top: 0.8rem;
    }

    .detail-label {
        font-weight: 600; /* Slightly bold, not too heavy */
        font-size: 0.95rem; /* Adjusted size for better readability */
        color: #007554;
        margin-bottom: 0.2rem;
        letter-spacing: 0.5px; /* Slight letter spacing for a modern look */
        text-transform: uppercase; /* Make it more distinct */
    }

    .desc-text{
        width:75%;
    }
    
    .container1{
        border: 1px solid black;
    }

    }
    </style>
    """
