import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, recipient_email, sender_email, app_password):
    """
    Sends an email to a single recipient.
    """
    try:
        # Email server configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)

        # Create the email
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient_email

        # Add email body
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Email sent successfully to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

    finally:
        server.quit()
