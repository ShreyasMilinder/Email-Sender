from flask import Flask, render_template, request, redirect, url_for
from recipient_loader import load_recipients
from email_sender import send_email
import os

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def send_bulk_emails():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return "No file part in the request."
        
        file = request.files['file']
        if file.filename == '':
            return "No file selected for uploading."

        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Load recipients from the uploaded file
        recipients = load_recipients(file_path)
        
        if recipients:
            subject = request.form['subject']
            body_template = request.form['body_template']
            sender_email = request.form['sender_email']
            app_password = request.form['app_password']

            for recipient in recipients:
                personalized_body = body_template.format(
                    name=recipient["name"],
                    company=recipient.get("company", ""),
                    custom_message=recipient.get("custom_message", "")
                )
                # Send the email
                send_email(subject, personalized_body, recipient["email"], sender_email, app_password)
            
            return "Emails sent successfully!"
        else:
            return "No valid recipients found."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
