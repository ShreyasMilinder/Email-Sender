import pandas as pd
from email_validator import validate_email, EmailNotValidError

def load_recipients(file_path):
    """
    Loads the recipient list from a CSV file and validates the email addresses.
    """
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Validate required columns
        required_columns = ["name", "email"]
        if not all(column in df.columns for column in required_columns):
            print(f"Missing required columns in the file. Required: {required_columns}")
            return []

        # Process and validate each recipient
        recipients = []
        for _, row in df.iterrows():
            try:
                # Validate the email address
                valid = validate_email(row["email"])
                email = valid.email
                
                # Add recipient data to the list
                recipients.append({
                    "name": row["name"],
                    "email": email,
                    "company": row.get("company", ""),  # Optional: company column (if available)
                    "custom_message": row.get("custom_message", "")  # Optional: custom_message column (if available)
                })
            except EmailNotValidError as e:
                print(f"Invalid email {row['email']}: {e}")
        
        return recipients

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Failed to load recipients: {e}")
    
    return []
