import smtplib
from email.message import EmailMessage
from secrets import sender_email,receiver_email,app_password

# Email details
def send_email(receiver_email,content):

# Create email
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "subject"
    msg.set_content(content)

    # Connect to Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()                 # Secure connection
        server.login(sender_email, app_password)
        server.send_message(msg)

    print("Email sent successfully!")

send_email(receiver_email="keerthanahrkeerthana18@gmail.com",subject="Hello from python",content="This is a email sent using python.")