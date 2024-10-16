import streamlit as st
from database import get_database
from datetime import datetime
# https://arnaudmiribel.github.io/streamlit-extras/extras/stylable_container/
def get_status_color(status):
    if status == "Not Started":
        return "#F85149"  # Red (from our refined color palette)
    elif status == "In Progress":
        return "#D29922"  # Yellow (from our refined color palette)
    elif status == "Completed":
        return "#2EA043"  # Green (from our refined color palette)
    else:
        return "#C9D1D9"  # Default text color

container_style = """
    <style>
        .container1 {
            border: 2px solid #3498db;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 20px;
        }
        .container2 {
            /* Add styles for Container 2 if needed */
        }
    </style>
"""

# Display the CSS styles
st.markdown(container_style, unsafe_allow_html=True)


def projects_list_page():
    try:
        st.title("📋 Projects List")

        db = get_database()
        projects = list(db.projects.find({"created_by": st.session_state.username}))

        # Filter options for project status
        status_filter = st.selectbox("Filter by Project Status", ["All", "Not Started", "In Progress", "Completed"])

        if status_filter != "All":
            projects = [project for project in projects if project['status'] == status_filter]

        # Display projects based on the selected filter
        status_titles = {
            "Not Started": ("red", "Not Started"),
            "In Progress": ("#ad7c00", "In Progress"),
            "Completed": ("green", "Completed")
        }

        for status, (color, title) in status_titles.items():
            if status_filter == "All" or status_filter == status:
                st.markdown(f"<h2 style='color: {color};'>{title}</h2>", unsafe_allow_html=True)
                for project in [p for p in projects if p['status'] == status]:
                    status_color = get_status_color(project['status'])
                    with st.expander(project['name'], expanded=False):
                        st.markdown(f"""
                        <div class="project-container">
                            <div class="project-header">
                                <span class="project-name">{project['name']}</span>
                                <span class="project-status" style="background-color: {status_color}; color: none; font-weight:400;">{project['status']}</span>
                            </div>
                            <div class="desc">
                                <div class="desc-text"><span class="detail-label">Description:</span> {project['description']}</div>
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
    except Exception as e:
        print("Exception handled at Project Lists.PY \n",e)
        st.rerun()

def edit_project(project):
    try:
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
            st.rerun()
    except Exception as e:
        print("Exception handled at Edit Projects function \n",e)
        st.rerun()