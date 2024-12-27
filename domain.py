import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
from tabulate import tabulate
import tempfile
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GODADDY_API_KEY")
api_secret = os.getenv("GODADDY_API_SECRET")
chat_webhook_url = os.getenv("GOOGLE_CHAT_WEBHOOK_URL")
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")

enable_email_notifications = os.getenv("ENABLE_EMAIL_NOTIFICATIONS", "false").lower() == "true"

notified_domains = set()  # Global set to track notified domains

def fetch_domains_from_api(status="ACTIVE", limit=100):
    """Fetch domain names from GoDaddy API."""
    url = f"https://api.godaddy.com/v1/domains?statuses={status}&limit={limit}"
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        domains = response.json()
        domain_names = [domain["domain"] for domain in domains]
        return domain_names
    except Exception as e:
        print(f"Error fetching domains from API: {e}")
        return []

def check_and_notify(domain):
    """Check the domain's expiry date and collect for notifications if needed."""
    if domain in notified_domains:
        return None  # Skip if already notified

    url = f"https://api.godaddy.com/v1/domains/{domain}"
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        expiry_date_str = data["expires"]
        expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        formatted_expiry_date = expiry_date.strftime("%d-%m-%Y")

        today = datetime.now()
        notification_date = expiry_date - timedelta(days=30)

        if today >= notification_date:
            # Add domain to notified list
            notified_domains.add(domain)

        return domain, formatted_expiry_date

    except Exception as e:
        print(f"Error processing domain {domain}: {e}")
        return domain, "Error"

def send_email_notification(table):
    """Send the tabular data via email."""
    if not enable_email_notifications:
        print("Email notifications are disabled.")
        return

    subject = "Domain Expiry Notifications"
    body = f"Hello,\n\nPlease find below the domain expiry notifications:\n\n{table}\n\nRegards,\nYour Team"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, recipient_email, message.as_string())
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email notification: {e}")

def main():
    # Fetch domain names from GoDaddy API
    domain_list = fetch_domains_from_api()

    if not domain_list:
        print("No domains found in the GoDaddy account.")
        return

    processed_domains = []

    for domain in domain_list:
        result = check_and_notify(domain)
        if result:
            processed_domains.append(result)

    # Sort domains by expiry date
    processed_domains.sort(key=lambda x: datetime.strptime(x[1], "%d-%m-%Y") if x[1] != "Error" else datetime.max)

    # Display domains in a tabular format
    headers = ["Domain Name", "Expiry Date"]
    table = tabulate(processed_domains, headers=headers, tablefmt="grid")
    print(table)

    # Save the table to a temporary file
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp_file:
        tmp_file.write(table)
        print("Table saved as temporary file:", tmp_file.name)

    # Send only the table to Google Chat
    chat_payload = {"text": f"GoDaddy Domain Expiry Notifications:\n{table}"}
    chat_response = requests.post(chat_webhook_url, json=chat_payload)

    if chat_response.status_code == 200:
        print("Table sent to Google Chat successfully.")
    else:
        print("Failed to send table to Google Chat.")

    # Send email notification if enabled
    send_email_notification(table)

if __name__ == "__main__":
    main()
