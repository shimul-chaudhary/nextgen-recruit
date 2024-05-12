import streamlit as st
from utils import data


st.title("NextGen Recruit")
if st.button("Add Job Post"):
    st.switch_page("pages/ad_posting.py")



search_term = st.text_input("Search Jobs by Title (optional)")

def apply_button_clicked(job_title, company_name, location, row_index,description,flag,status,resume,summary):
  st.session_state["selected_job"] = {
      "job_title": job_title,
      "company_name": company_name,
      "location": location,
      "description": description, 
      "row_index":row_index,
      "flag":flag,
      "status":status,
      "resume":resume,
      "summary":summary
  }
  st.switch_page("pages/apply.py")


for row_index, row_data in enumerate(data):
  job_title = row_data.get("Title")
  company_name = row_data.get("Company")
  location = row_data.get("Location")
  description = row_data.get("JobDescription")
  flag = row_data.get("flag")
  status = row_data.get("status")
  resume = row_data.get("resume")
  summary = row_data.get("summary")

  if search_term and search_term.lower() in job_title.lower():  
    if flag==False:
        st.write(f"Job Title: {job_title}")
        st.write(f"Company Name: {company_name}")
        st.write(f"Location: {location}")
        if st.button(f"Apply", key=f"apply_button_{row_index}"):
            apply_button_clicked(job_title, company_name, location, row_index,description,flag,status,resume,summary)

