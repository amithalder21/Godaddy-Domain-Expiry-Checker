
```
# GoDaddy Domain Expiry Checker

This project is a Python script that checks the expiry dates of domains registered with GoDaddy and sends notifications when the expiry date is approaching. It utilizes the GoDaddy API to retrieve domain information and sends notifications via Google Chat and email.

## Prerequisites

- Python 3.6 or higher
- Pip package manager

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/amit-successive/godaddy-domain-expiry-checker.git
   ```

2. Navigate to the project directory:

   ```shell
   cd godaddy-domain-expiry-checker
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Configuration

1. Create a file named `.env` in the project directory.
2. Open the `.env` file in a text editor and add the following environment variables:

   ```
   GODADDY_API_KEY=your_godaddy_api_key
   GODADDY_API_SECRET=your_godaddy_api_secret
   GOOGLE_CHAT_WEBHOOK_URL=your_google_chat_webhook_url
   SENDER_EMAIL=your_sender_email
   SENDER_PASSWORD=your_sender_password
   RECIPIENT_EMAIL=your_recipient_email
   ```

   Replace `your_godaddy_api_key`, `your_godaddy_api_secret`, `your_google_chat_webhook_url`, `your_sender_email`, `your_sender_password`, and `your_recipient_email` with the appropriate values.

## Usage

1. Create a file named `domain_list.txt` in the project directory.
2. Add the domain names, each on a separate line, to the `domain_list.txt` file.
3. Run the script using the following command:

   ```shell
   python domain.py
   ```

   The script will retrieve the expiry dates for the domains in `domain_list.txt` and send notifications if the expiry date is within 30 days.
   It will also print the domain list with expiry dates in tabular form.

   **Note:** Ensure that the environment variables in the `.env` file are correctly configured before running the script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

Please note that this README assumes the existence of a file named `domain_expiry_checker.py` in the repository, based on the provided repository link. You can modify the instructions as needed or provide additional information specific to your project.
