import streamlit as st
import json


st.title("NextGen Recruit")
if st.button("Add Job Post"):
    st.switch_page("pages/ad_posting.py")


def read_jsonl(filename):
  data = []
  with open(filename, 'r') as f:
    for line in f:
      data.append(json.loads(line))
  return data


data = read_jsonl("../job-description.jsonl")  
search_term = st.text_input("Search Jobs by Title (optional)")
applied_jobs = set()

def apply_button_clicked(job_title, company_name, location, row_index,description):
  st.session_state["selected_job"] = {
      "job_title": job_title,
      "company_name": company_name,
      "location": location,
      "description": description,  # Access job description
  }
  st.switch_page("pages/apply.py")

# Search within the loop
for row_index, row_data in enumerate(data):
  job_title = row_data.get("Title")
  company_name = row_data.get("Company")
  location = row_data.get("Location")
  description = row_data.get("JobDescription")

  if search_term and search_term.lower() in job_title.lower():  # Check for search term in job title
    st.write(f"Job Title: {job_title}")
    st.write(f"Company Name: {company_name}")
    st.write(f"Location: {location}")
    if st.button(f"Apply", key=f"apply_button_{row_index}"):
      apply_button_clicked(job_title, company_name, location, row_index,description)
