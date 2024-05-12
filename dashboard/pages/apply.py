import streamlit as st
from utils import data,job_list
from langchain_community.document_loaders.pdf import PyPDFLoader
from PyPDF2 import PdfReader

import os
import sys


def run():
    st.session_state.run = True
if 'run' not in st.session_state:
    st.session_state.run = False
    st.session_state.result = None
# Add the parent directory of your project to the Python path
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(project_directory)
sys.path.append(project_directory + "/filter_agents")
sys.path.append(project_directory + "/interview_bot")
from filter_agents.bots import get_filter_app

st.title("Apply")

selected_job = st.session_state.get("selected_job")
applied_job=st.session_state.get("applied_jobs")
def display_applied_jobs(job_title,company_name,location,job_description,row_index,flag,status,resume,summary,list):
            st.session_state["applied_jobs"] = {
            "job_title": job_title,
            "company_name": company_name,
            "location": location,
            "description": job_description, 
            "row_index":row_index,
            "flag":flag,
            "status":status,
            "resume":resume,
            "summary":summary,
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
  resume=selected_job["resume"]
  summary=selected_job["summary"]

  st.write(f"Job Title: {job_title}")
  st.write(f"Company Name: {company_name}")
  st.write(f"Location: {location}")
  st.write(f"Job Description: {job_description}")
  st.write(f"status: {status}")
  upload_file=st.file_uploader("Upload your resume")
      

  if upload_file is not None:
    
    if st.button("Submit",on_click=run, disabled=st.session_state.run):
        pdf = PdfReader(upload_file)
        page = pdf.pages[0]
        data[selected_job["row_index"]]["flag"] = True
        selected_job["flag"] = True  
        selected_job["status"]="Applied and Under Review"
        selected_job["resume"]=page.extract_text()

        st.session_state["selected_job"] = selected_job
        with st.spinner("Reviewing your resume..."):
          summary, parsed_resume = get_filter_app(selected_job)

        selected_job["summary"] = summary
        selected_job["resume"] = parsed_resume

        job_list.append(selected_job)
        st.session_state.run = False

        if "**Output:** No" in selected_job["summary"]:
            selected_job["status"]="Rejected"
        display_applied_jobs(selected_job["job_title"],selected_job["company_name"],selected_job["location"],selected_job["description"],selected_job["row_index"],selected_job["flag"],selected_job["status"],selected_job["resume"],selected_job["summary"],job_list)
        
else:
  st.write("No job applied")



