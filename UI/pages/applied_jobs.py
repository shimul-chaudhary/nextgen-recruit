import streamlit as st


st.write("## Applied Jobs")

job = st.session_state.get("applied_jobs")

if job:
  job_title = job["job_title"]
  company_name = job["company_name"]
  location = job["location"]
  job_description = job["description"]
  flag=job["flag"]
  row_index=job["row_index"]
  status=job["status"]
  list=job["list"]
  for row_index, row_data in enumerate(list):
    job_title = row_data.get("job_title")
    company_name = row_data.get("company_name")
    location = row_data.get("location")
    description = row_data.get("description")
    flag = row_data.get("flag")
    row_index=row_data.get("row_index")
    status=row_data.get("status")
    st.write(f"Job Title: {job_title}")
    st.write(f"Company Name: {company_name}")
    st.write(f"Location: {location}")
    st.write(f"Job Description: {job_description}")
    st.write(f"Status: {status}")