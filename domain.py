import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tabulate import tabulate

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GODADDY_API_KEY")
api_secret = os.getenv("GODADDY_API_SECRET")
chat_webhook_url = os.getenv("GOOGLE_CHAT_WEBHOOK_URL")
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")

domain_list = []  # List to store the domain names and expiry dates

file_path = "domain_list.txt"  # Path to the file containing domain names
with open(file_path, "r") as file:
    for line in file:
        domain = line.strip()

        url = f"https://api.godaddy.com/v1/domains/{domain}"
        headers = {
            "Authorization": f"sso-key {api_key}:{api_secret}",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        expiry_date_str = data["expires"]
        expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        formatted_expiry_date = expiry_date.strftime("%d-%m-%Y")

        today = datetime.now()
        notification_date = expiry_date - timedelta(days=30)

        if today >= notification_date:
            # Send notification to Google Chat API
            notification_message = f"The domain {domain} expires on {formatted_expiry_date}. Please take necessary actions."

            payload = {
                "text": notification_message
            }
            response = requests.post(chat_webhook_url, json=payload)
            if response.status_code == 200:
                print("Google Chat notification sent successfully.")
            else:
                print("Failed to send Google Chat notification.")

            # Send notification via email
            subject = "Domain Expiry Notification"
            body = """Hello,

This is to inform you that the domain {} will expire on {}. Please take the necessary actions.

Regards,
Your Name""".format(domain, formatted_expiry_date)

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            try:
                # Create a secure SSL/TLS connection with the SMTP server
                smtp = smtplib.SMTP("smtp.gmail.com", 587)
                smtp.starttls()
                smtp.login(sender_email, sender_password)

                # Send the email
                smtp.sendmail(sender_email, recipient_email, message.as_string())
                print("Email notification sent successfully.")
            except Exception as e:
                print("Failed to send email notification.")
                print(e)
            finally:
                # Close the SMTP connection
                smtp.quit()

        domain_list.append((domain, formatted_expiry_date))  # Collect the domain name and expiry date

# Print the domain list in tabular form
headers = ["Domain Name", "Expiry Date"]
tabulated_data = tabulate(domain_list, headers=headers, tablefmt="grid")
print(tabulated_data)

# Store the tabular data in a temporary file
tmp_file_path = "domain_list.txt.tmp"
with open(tmp_file_path, "w") as tmp_file:
    tmp_file.write(tabulated_data)

print(f"Tabular data stored in {tmp_file_path}")
