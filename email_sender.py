from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, recipient_email, sender_email, app_password, cc_emails=None):
    """
    Sends an email to a single recipient with optional CC recipients.
    """
    server = None  # Initialize server to None
    try:
        # Email server configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Set up the SMTP server
        server = SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)

        # Create the email
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient_email

        # Add CC recipients
        if cc_emails:
            msg["Cc"] = ", ".join(cc_emails)

        # Add email body
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        recipients = [recipient_email] + (cc_emails if cc_emails else [])
        server.sendmail(sender_email, recipients, msg.as_string())
        print(f"Email sent successfully to {recipient_email} (CC: {cc_emails})")

    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

    finally:
        # Quit server if it was initialized
        if server is not None:
            server.quit()
