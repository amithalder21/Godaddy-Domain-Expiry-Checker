# GoDaddy Domain Expiry Checker

This project is a Python script that checks the expiry dates of domains registered with GoDaddy and sends notifications when the expiry date is approaching. It utilizes the GoDaddy API to retrieve domain information and sends notifications via Google Chat and optionally via email.

## Prerequisites

- Python 3.6 or higher
- Pip package manager
- Docker (optional for containerized deployment)

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/amit-successive/Godaddy-Domain-Expiry-Notifier.git
   ```

2. Navigate to the project directory:

   ```shell
   cd Godaddy-Domain-Expiry-Notifier
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Docker Setup (Optional)

To run the application in a Docker container:

1. Build the Docker image:

   ```shell
   docker build -t godaddy-notifier:latest .
   ```

2. Create a `.env` file in the project directory with the following content:

   ```plaintext
   GODADDY_API_KEY=your_godaddy_api_key
   GODADDY_API_SECRET=your_godaddy_api_secret
   GOOGLE_CHAT_WEBHOOK_URL=your_google_chat_webhook_url
   SENDER_EMAIL=your_sender_email
   SENDER_PASSWORD=your_sender_password
   RECIPIENT_EMAIL=your_recipient_email
   ENABLE_EMAIL_NOTIFICATIONS=true
   ```

3. Run the Docker container, passing the `.env` file:

   ```shell
   docker run --env-file .env godaddy-notifier:latest
   ```

4. Alternatively, run the Docker container with environment variables directly:

   ```shell
   docker run -d \                                      
     -e GODADDY_API_KEY="9EBukYs4Sgf_J75tAYRtZKVXJ18sqZCpPA" \
     -e GODADDY_API_SECRET="ApquUUtamm9tgyReUrDbTK" \
     -e GOOGLE_CHAT_WEBHOOK_URL="https://chat.googleapis.com/v1/spaces/AAAAYA7rjAs/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=myuxKGbW7wjUDYciGC5Uw7AbHZ9ef3qmytzOufGlSrY" \
     -e SENDER_EMAIL="your_email@example.com" \
     -e SENDER_PASSWORD="your_password" \
     -e RECIPIENT_EMAIL="recipient_email@example.com" \
     -e ENABLE_EMAIL_NOTIFICATIONS="true" \
     godaddy-notifier:latest
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

   OR, if using Docker:

   ```shell
   docker run --env-file .env godaddy-notifier:latest
   ```

   OR, use direct environment variables:

   ```shell
   docker run -d \                                      
     -e GODADDY_API_KEY="9EBukYs4Sgf_J75tAYRtZKVXJ18sqZCpPA" \
     -e GODADDY_API_SECRET="ApquUUtamm9tgyReUrDbTK" \
     -e GOOGLE_CHAT_WEBHOOK_URL="https://chat.googleapis.com/v1/spaces/AAAAYA7rjAs/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=myuxKGbW7wjUDYciGC5Uw7AbHZ9ef3qmytzOufGlSrY" \
     -e SENDER_EMAIL="your_email@example.com" \
     -e SENDER_PASSWORD="your_password" \
     -e RECIPIENT_EMAIL="recipient_email@example.com" \
     -e ENABLE_EMAIL_NOTIFICATIONS="true" \
     godaddy-notifier:latest
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
