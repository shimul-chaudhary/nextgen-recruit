import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import os

# Sending an email with a calendly link
def send_email(recipient_name, recipient_email, job_title):
    # Email Credentials
    sender_email = os.getenv("SENDER_MAIL")
    password = os.getenv("EMAIL_PASSWORD")
    calendly_link = "https://calendly.com/shivamsharma00"
    # Email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Invitation to Schedule Your Screening Call with NextGen Recruit"

    body = f"""
Dear {recipient_name},

I hope you are doing well! I'm John, Recruitment Coordinator at NextGen Recruit. Thank you for your interest in the {job_title} position with us. We are impressed with your background and would like to invite you to the next step in our hiring process. We are delighted by your application and would like to arrange an initial screening call to discuss your profile and the exciting opportunities awaiting at our company. This call will be conducted by one of our friendly recruiters who will guide you through the next steps.

Please take a moment to schedule your call by clicking on this placeholder LINK. This will lead you to our online scheduler, where you can select a date and time that works best for you.
{calendly_link} 

We eagerly anticipate speaking with you and discovering how your talents can contribute to our success.

Warmest Regards,

John Kwan
RecruitmentCoordinator
NextGen Recruiter
    """

    message.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        print("Interview invite email sent successfully!")
    except Exception as e:
        print(f"Error sending email : {e}")

def send_reject_email(recipient_name, recipient_email, job_title):
    # Email Credentials
    sender_email = os.getenv("SENDER_MAIL")
    password = os.getenv("EMAIL_PASSWORD")
    # Email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Feedback after Resume Screening"

    body = f"""
Dear {recipient_name},

I hope you are doing well! I'm John, Recruitment Coordinator at NextGen Recruit. Thank you for your interest but for now we have decided to move forward with other candidates.

Warmest Regards,

John Kwan
RecruitmentCoordinator
NextGen Recruiter
    """

    message.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        print("Rejected email sent successfully!")
    except Exception as e:
        print(f"Error sending email : {e}")

def send_meet_link(recipient_name, recipient_email, job_title):
    # Email Credentials
    sender_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")
    meeting_link = os.getenv("MEET_LINK")
    # Email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Invitation to Screening Round Interview"

    body = f"""
Dear {recipient_name},
I hope this email finds you well.

I am writing to invite you to participate in the screening round interview for the {job_title}. We were impressed by your qualifications and experience, and we believe that you could be a valuable addition to our team.

The screening round interview is an opportunity for us to get to know you better and to discuss your background, skills, and career aspirations in more detail. It will also provide you with the chance to learn more about our company culture, values, and the role itself.

Meeting Link: {meeting_link}

Please make sure to test the meeting link prior to the interview to ensure that you can access the virtual meeting platform without any issues. If you encounter any difficulties or have any questions, please don't hesitate to reach out to me.

We are excited to learn more about you and explore the possibility of you joining our team. We look forward to meeting you virtually and discussing how your skills and experiences align with our requirements.

Best regards,

John Kwan
RecruitmentCoordinator
NextGen Recruiter
    """

    message.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        print("Screening round email sent successfully!")
    except Exception as e:
        print(f"Error sending email : {e}")
