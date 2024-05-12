import streamlit as st
from interview_bot.send_mail import send_email, send_meet_link, send_reject_email
import time
from conversational_bot.interview_bot import voice_bot
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
  resume=job["resume"]
  summary=job["summary"]
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

  if status=="Rejected":
    send_reject_email("Shimul","shimul.chaudhary@gmail.com", job["job_title"])

  else:
    send_email("Shimul","shimul.chaudhary@gmail.com", job["job_title"])
    time.sleep(5)
    send_meet_link("Shimul","shimul.chaudhary@gmail.com", job["job_title"])
    time.sleep(5)
    voice_bot(job["summary"])
  