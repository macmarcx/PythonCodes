import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Email server settings
email_host = 'your_email_host'
email_port = 587
email_user = 'your_email@example.com'
email_password = 'your_email_password'

# Email configuration
sender_address = 'your_email@example.com'
receiver_address = 'recipient_email@example.com'
subject = 'Email Subject'
body = 'Email Body'

# Attachment settings
attachment_path = 'path/to/attachment.pdf'

# Creating the email message
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Attaching the resume
with open(attachment_path, "rb") as attachment:
    part = MIMEApplication(attachment.read(), Name="resume.pdf")
    part['Content-Disposition'] = f'attachment; filename="{attachment_path}"'
    message.attach(part)

# Connecting and sending the email
with smtplib.SMTP(email_host, email_port) as server:
    server.starttls()
    server.login(email_user, email_password)
    server.sendmail(sender_address, receiver_address, message.as_string())

print("Email sent successfully.")
