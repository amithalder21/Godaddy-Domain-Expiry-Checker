# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY domain.py .

# Set default environment variables (can be overridden at runtime)
ENV GODADDY_API_KEY=""
ENV GODADDY_API_SECRET=""
ENV GOOGLE_CHAT_WEBHOOK_URL=""
ENV SENDER_EMAIL=""
ENV SENDER_PASSWORD=""
ENV RECIPIENT_EMAIL=""
#By default email notification is disabled
ENV ENABLE_EMAIL_NOTIFICATIONS="false" 

# Command to run the application
CMD ["python", "domain.py"]
