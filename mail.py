import csv
import requests

# change this to your Mailgun credentials
MAILGUN_DOMAIN = ""
MAILGUN_API_KEY = ""
email = ""
def send_email(subject, recipient_email, recipient_name, body_text, sender=f"{email}@mailgun.org"):
    """
    Sending an email using the Mailgun API.
    """
    return requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": sender,
            "to": recipient_email,
            "subject": subject,
            "text": body_text.replace("{name}", recipient_name)
        }
    )

def read_csv_and_send_emails(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row.get('Name')
            email = row.get('Email')

            if not name or not email:
                print(f"Skippingrow with missing data: {row}")
                continue  

            subject = "iChrispin"
            body_text = "Hello {name},\nThis is a test email created by iChrispin sent to you from my own domain using Mailgun and Kali Linux."
            
            try:
                response = send_email(subject, email, name, body_text)
                if response.status_code == 200:
                    print(f"Email sent successfully to {email}")
                else:
                    print(f"Failed to send email to {email}: {response.status_code} - {response.text}")
            except Exception as e:
                print(f"An error occurred while sending email to {email}: {e}")

if __name__ == "__main__":
   
    csv_file_path = str(input("Path to Your CSV file:")) 
    
    read_csv_and_send_emails(csv_file_path)
