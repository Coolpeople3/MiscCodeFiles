import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
print("This is Hitarth's emailing platform, Only compatible with Gmail")   #Enable "less secure apps" in gmail from which you are sending
EmailToSendTo=input("What email would you like to send to? ")
# Email details
sender_email = input("What is your email address? ")
receiver_email = EmailToSendTo
subject = "This is a test"
body = """\
Hello,

This is a test email sent from a Python script!

Best regards,
Hitarth """

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# SMTP server configuration
smtp_server = "smtp.gmail.com"  # e.g., smtp.gmail.com for Gmail
smtp_port = 587  # Use 465 for SSL
smtp_password = input("What is the password associated with your email? ")   #Perhaps this is wrong, pls check

try:
    # Create an SMTP session
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade to secure connection
    server.login(sender_email, smtp_password)  # Login to the email server
    server.send_message(msg)  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  # Close the connection
