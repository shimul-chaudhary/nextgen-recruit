import streamlit as st

st.title("Apply")
selected_job = st.session_state.get("selected_job")

if selected_job:
  job_title = selected_job["job_title"]
  company_name = selected_job["company_name"]
  location = selected_job["location"]
  job_description = selected_job["description"]

  st.write(f"Job Title: {job_title}")
  st.write(f"Company Name: {company_name}")
  st.write(f"Location: {location}")
  st.write(f"Job Description: {job_description}")

else:
  st.write("No job selected")
st.file_uploader("Upload your resume")