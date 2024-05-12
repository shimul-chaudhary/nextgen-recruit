import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

# Sending an email with a calendly link
def send_email(recipient_name, recipient_email, job_title):
    # Email Credentials
    sender_email = "prachi1615@gmail.com"
    password = "xyly jzmq ucfu ayii"
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
        return "Email sent successfully!"
    except Exception as e:
        return f"Error sending email : {e}"
