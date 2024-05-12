import streamlit as st
from utils import data,job_list

st.title("Apply")

selected_job = st.session_state.get("selected_job")
def display_applied_jobs(job_title,company_name,location,job_description,row_index,flag,status,list):
            st.session_state["applied_jobs"] = {
            "job_title": job_title,
            "company_name": company_name,
            "location": location,
            "description": job_description, 
            "row_index":row_index,
            "flag":flag,
            "status":status,
            "list":list
        }
            st.switch_page("pages/applied_jobs.py")
if selected_job:
  job_title = selected_job["job_title"]
  company_name = selected_job["company_name"]
  location = selected_job["location"]
  job_description = selected_job["description"]
  flag=selected_job["flag"]
  row_index=selected_job["row_index"]
  status=selected_job["status"]

  st.write(f"Job Title: {job_title}")
  st.write(f"Company Name: {company_name}")
  st.write(f"Location: {location}")
  st.write(f"Job Description: {job_description}")
  st.write(f"flag: {flag}")
  st.write(f"status: {status}")
  upload_file=st.file_uploader("Upload your resume")
  if upload_file is not None:
    
    if st.button("Submit"):

        data[selected_job["row_index"]]["flag"] = True
        selected_job["flag"] = True  
        selected_job["status"]="Applied and Under Review"
        st.session_state["selected_job"] = selected_job
        job_list.append(selected_job)
        display_applied_jobs(selected_job["job_title"],selected_job["company_name"],selected_job["location"],selected_job["description"],selected_job["row_index"],selected_job["flag"],selected_job["status"],job_list)
        

    st.write(f"flag: {flag}")

else:
  st.write("No job selected")



