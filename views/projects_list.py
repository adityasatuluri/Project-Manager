import streamlit as st
from database import get_database
from datetime import datetime
from colorama import Fore

def get_status_color(status):
    if status == "Not Started":
        return "#FF4136"  # Red
    elif status == "In Progress":
        return "#FFDC00"  # Yellow
    elif status == "Completed":
        return "#2ECC40"  # Green
    else:
        return "#FFFFFF"  # White

def projects_list_page():
    st.markdown("""
    <style>
    .project-container {
        background-color: #1E1E1E;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #333;
    }
    .project-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    .project-name {
        font-size: 24px;
        font-weight: bold;
        color: #FFFFFF;
    }
    .project-status {
        font-weight: bold;
        padding: 5px 10px;
        border-radius: 5px;
    }
    .project-details {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
    }
    .detail-label {
        font-weight: bold;
        color: #888;
    }
    .edit-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("📋 Projects List")

    db = get_database()
    projects = list(db.projects.find({"created_by": st.session_state.username}))

    for project in projects:

        status_color = get_status_color(project['status'])
        ss = str(status_color[0:len(status_color)])
    #     st.markdown(f"""
    #     <style>
    #         .streamlit-expanderHeader {{
    #             background-color: {status_color};  /* Use Python variable here */
    #             border-radius: 5px;
    #             color: white;
    #         }}
    #     </style>
    # """, unsafe_allow_html=True)
        with st.expander(project['name']):
            st.markdown(f"""
            <div class="project-header">
                <span class="project-name">{project['name']}</span>
                <span class="project-status" style="background-color: {status_color};">{project['status']}</span>
            </div>
            <div class="project-details">
                <div>
                    <p><span class="detail-label">Type:</span> {', '.join(project['type'])}</p>
                    <p><span class="detail-label">Description:</span> {project['description']}</p>
                    <p><span class="detail-label">Tools:</span> {', '.join(project['tools'])}</p>
                </div>
                <div>
                    <p><span class="detail-label">Start Date:</span> {project['start_date']}</p>
                    <p><span class="detail-label">Deadline:</span> {project['deadline']}</p>
                    <p><span class="detail-label">Purpose:</span> {project['purpose']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Edit", key=f"edit_{project['_id']}", use_container_width=True):
                edit_project(project)

def edit_project(project):
    st.subheader(f"Edit Project: {project['name']}")

    name = st.text_input("Project Name", value=project['name'])
    project_type = st.multiselect(
            "Project Type", 
            ["Crossplatform", "Responsive Web App", "Android", "iOS", "PC", "Extension", "Service"]
        )
    description = st.text_area("Description", value=project['description'])
    tools = st.text_input("Tools (comma-separated)", value=", ".join(project['tools']))
    start_date = st.date_input("Start Date", value=datetime.fromisoformat(project['start_date']))
    deadline = st.date_input("Deadline", value=datetime.fromisoformat(project['deadline']))
    purpose = st.text_area("Purpose", value=project['purpose'])
    status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"], index=["Not Started", "In Progress", "Completed"].index(project['status']))

    if st.button("Update Project"):
        db = get_database()
        updated_project = {
            "name": name,
            "type": project_type,
            "description": description,
            "tools": [tool.strip() for tool in tools.split(",")],
            "start_date": start_date.isoformat(),
            "deadline": deadline.isoformat(),
            "purpose": purpose,
            "status": status,
            "updated_at": datetime.utcnow()
        }
        db.projects.update_one({"_id": project['_id']}, {"$set": updated_project})
        st.success("Project updated successfully!")
        st.experimental_rerun()