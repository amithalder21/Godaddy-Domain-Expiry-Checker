# GoDaddy Domain Expiry Checker

This project is a Python script that checks the expiry dates of domains registered with GoDaddy and sends notifications when the expiry date is approaching. It utilizes the GoDaddy API to retrieve domain information and sends notifications via Google Chat and optionally via email.

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
   ENABLE_EMAIL_NOTIFICATIONS=true
   ```

   Replace `your_godaddy_api_key`, `your_godaddy_api_secret`, `your_google_chat_webhook_url`, `your_sender_email`, `your_sender_password`, and `your_recipient_email` with the appropriate values.

   Set `ENABLE_EMAIL_NOTIFICATIONS` to `true` to enable email notifications or `false` to disable them.

## Usage

1. Run the script using the following command:

   ```shell
   python domain.py
   ```

   The script will:
   - Retrieve domain details from the GoDaddy API.
   - Check the expiry dates of the domains.
   - Send a consolidated notification in tabular format to Google Chat.
   - Optionally, send an email notification if `ENABLE_EMAIL_NOTIFICATIONS` is set to `true`.

2. The output will also display the domain list with expiry dates in tabular form in the terminal.

## Example Output

A sample table output in the terminal:

```
+--------------------------+---------------+
| Domain Name              | Expiry Date   |
+==========================+===============+
| example.com              | 01-01-2025    |
| example.org              | 15-02-2025    |
| example.net              | 20-03-2025    |
+--------------------------+---------------+
```

The same table will be sent to Google Chat and, if enabled, via email.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

### Key Updates:
1. **`ENABLE_EMAIL_NOTIFICATIONS`**:
   - Added instructions for enabling or disabling email notifications.
2. **Removed `domain_list.txt`**:
   - No need for a `domain_list.txt` file since the script fetches domains directly from the GoDaddy API.
3. **Updated Usage**:
   - Clarified that notifications are consolidated in tabular format and sent to Google Chat and optionally via email.
4. **Example Output**:
   - Included a sample table to visualize the output.

Let me know if further refinements are needed!
