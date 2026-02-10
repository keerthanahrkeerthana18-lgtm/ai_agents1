import smtplib
from email.message import EmailMessage
from secrets import sender_email,receiver_email,app_password

# Email details
sender_email = "keerthanahrkeerthana18@gmail.com"
receiver_email = "4mh23cs063@gmail.com"
app_password = "xlyq lisg bpqh zyjp"

# Create email
msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email from Python"
msg.set_content("Hello!\nThis email was sent using Python.")

# Connect to Gmail SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()                 # Secure connection
    server.login(sender_email, app_password)
    server.send_message(msg)

print("Email sent successfully!")