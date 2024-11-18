import requests
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve necessary environment variables
access_token = os.getenv("ACCESS_TOKEN")
job_id = os.getenv("JOB_ID")
server_h = os.getenv("SERVER_HOSTNAME")

# Build the API URL for triggering the job
url = f'https://{server_h}/api/2.0/jobs/run-now'

# Set headers for authentication and content type
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

# Prepare the data payload with the job ID
data = {
    'job_id': job_id
}

# Make a POST request to trigger the job
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    print('Job run successfully triggered')
else:
    print(f'Error: {response.status_code}, {response.text}')
