import streamlit as st
from database import get_database
from datetime import datetime

def get_status_color(status):
    if status == "Not Started":
        return "#F85149"  # Red (from our refined color palette)
    elif status == "In Progress":
        return "#D29922"  # Yellow (from our refined color palette)
    elif status == "Completed":
        return "#2EA043"  # Green (from our refined color palette)
    else:
        return "#C9D1D9"  # Default text color

def projects_list_page():
    
    st.title("📋 Projects List")

    db = get_database()
    projects = list(db.projects.find({"created_by": st.session_state.username}))

    for project in projects:
        status_color = get_status_color(project['status'])
        with st.expander(project['name']):
            st.markdown("""
                <style>
                .streamlit-expander {
                    background-color: {{status_color}};
                    color: white; # Adjust this for expander header color
                }
                </style>
            """, unsafe_allow_html=True)
            st.markdown(f"""
            <div class="project-container">
                <div class="project-header">
                    <span class="project-name">{project['name']}</span>
                    <span class="project-status" style="background-color: {status_color}; color: #0D1117;">{project['status']}</span>
                </div>
                <div>
                    <p><span class="detail-label">Description:</span> {project['description']}</p>
                </div>
                <div class="project-details">
                    <div>
                        <p><span class="detail-label">Type:</span> {', '.join(project['type'])}</p>
                        <p><span class="detail-label">Tools:</span> {', '.join(project['tools'])}</p>
                    </div>
                    <div>
                        <p><span class="detail-label">Start Date:</span> {project['start_date'] or 'Not set'}</p>
                        <p><span class="detail-label">Deadline:</span> {project['deadline'] or 'Not set'}</p>
                        <p><span class="detail-label">Purpose:</span> {project['purpose']}</p>
                    </div>
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
        ["Crossplatform", "Responsive Web App", "Android", "iOS", "PC", "Extension", "Service"],
        default=project['type']
    )
    description = st.text_area("Description", value=project['description'])
    tools = st.text_input("Tools (comma-separated)", value=", ".join(project['tools']))
    start_date = st.date_input("Start Date", value=datetime.fromisoformat(project['start_date']) if project['start_date'] else None)
    deadline = st.date_input("Deadline", value=datetime.fromisoformat(project['deadline']) if project['deadline'] else None)
    purpose = st.text_area("Purpose", value=project['purpose'])
    status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"], index=["Not Started", "In Progress", "Completed"].index(project['status']))

    if st.button("Update Project"):
        db = get_database()
        updated_project = {
            "name": name,
            "type": project_type,
            "description": description,
            "tools": [tool.strip() for tool in tools.split(",") if tool.strip()],
            "start_date": start_date.isoformat() if start_date else None,
            "deadline": deadline.isoformat() if deadline else None,
            "purpose": purpose,
            "status": status,
            "updated_at": datetime.utcnow()
        }
        db.projects.update_one({"_id": project['_id']}, {"$set": updated_project})
        st.success("Project updated successfully!")
        st.experimental_rerun()