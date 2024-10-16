import streamlit as st
from datetime import datetime
from database import get_database

def new_project_page():
    st.title("🆕 New Project")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Project Name")
        project_type = st.multiselect(
            "Project Type", 
            ["Crossplatform", "Responsive Web App", "Android", "iOS", "PC", "Extension", "Service"]
        )
        description = st.text_area("Description")
        tools = st.text_input("Tools (comma-separated)")

    with col2:
        # Option to clear Start Date
        clear_start = st.checkbox("Clear Start Date")
        start_date = None if clear_start else st.date_input("Start Date (Optional)")

        # Option to clear Deadline
        clear_deadline = st.checkbox("Clear Deadline")
        deadline = None if clear_deadline else st.date_input("Deadline (Optional)")

        purpose = st.text_area("Purpose")
        status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])

    if st.button("Save Project", key="save_new_project"):
        db = get_database()

        # Build the project dictionary, only adding dates if provided.
        project = {
            "name": name,
            "type": project_type,
            "description": description,
            "tools": [tool.strip() for tool in tools.split(",")],
            "purpose": purpose,
            "status": status,
            "created_by": st.session_state.get("username", "Unknown"),
            "created_at": datetime.utcnow()
        }

        # Add dates to the project only if they were selected.
        if start_date:
            project["start_date"] = start_date.isoformat()
        else:
            project["start_date"] = None

        if deadline:
            project["deadline"] = deadline.isoformat()
        else:
            project["deadline"] = None

        # Insert the project into the database.
        db.projects.insert_one(project)

        st.success("Project saved successfully!")
        st.balloons()
