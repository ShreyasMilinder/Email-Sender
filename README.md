
# Bulk Email Sender Web Application

A simple web application for sending personalized bulk emails using a CSV file as the recipient list. This project utilizes Python's Flask framework for the backend and a user-friendly HTML form for the frontend.

## Features

- Upload recipient details via a CSV file.
- Send personalized emails to multiple recipients.
- Use placeholders (`{name}`, `{company}`, `{custom_message}`) in the email body for dynamic content.
- Validate recipient email addresses before sending.
- Securely send emails using Gmail's app passwords.

## Tech Stack

- **Backend:** Flask, Python
- **Frontend:** HTML, CSS
- **Email Library:** smtplib, email.mime
- **Validation:** `email_validator`
- **CSV Handling:** `pandas`

## Prerequisites

- Python 3.x installed on your system.
- A Gmail account with an [App Password](https://support.google.com/accounts/answer/185833?hl=en).
- Required Python libraries:
  - Flask
  - pandas
  - email-validator

Install dependencies using the following command:

```bash
pip install flask pandas email-validator
```

## Project Structure

```
project/
├── app.py                # Main Flask application
├── email_sender.py       # Handles email sending functionality
├── recipient_loader.py   # Processes and validates the recipient list
├── templates/
│   └── index.html        # Frontend HTML template
├── uploads/              # Directory for uploaded CSV files
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/ShreyasMilinder/Email-Sender.git
   cd Email-Sender
   ```

2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open the web application in your browser:
   - Navigate to `http://127.0.0.1:5000/`

## How to Use

1. Prepare a CSV file (`recipients.csv`) with the following columns:
   - **name** (required): Name of the recipient.
   - **email** (required): Email address of the recipient.
   - **company** (optional): Recipient's company name.
   - **custom_message** (optional): Custom message for the recipient.

   Example CSV:

   ```csv
   name,email,company,custom_message
   John Doe,johndoe@example.com,Example Corp,Hello John!
   Jane Smith,janesmith@example.com,,Welcome aboard!
   ```

2. Access the application in your browser.
3. Upload the CSV file and fill in the required fields (email subject, body, etc.).
4. Click "Send Emails" to send personalized emails to all recipients.

## Notes

- Ensure your Gmail account has an app password for secure email sending.
- The `uploads/` directory stores the uploaded CSV files temporarily.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests to improve the project.
