import requests
import json
import uuid
from main import app
from fastapi.params import Body

def send_test_event():
    # API endpoint URL (adjust if your server runs on a different port)
    url = "http://localhost:8000/events/"

    # prompt = "Explain the importance of fast language models"
    prompt = "what is fastapi, give answer for a beginner"

    # Headers for JSON content
    headers = {
        "Content-Type": "application/json",
    }

    # Send POST request to the endpoint
    # response = requests.post(url=url, data=json.dumps(event_data), headers=headers)
    # response = requests.post(url=url, data=json.dumps(prompt), headers=headers)
    # response = requests.post(url=url, data=json.dumps({"prompt": prompt}), headers=headers)
    response = requests.post(url=url, json = {"prompt": prompt}, headers=headers)


    # Print response information
    print(f"Status Code: {response.status_code}")
    # try:
    #     print(f"Response: {response.json()}")
    # except ValueError:
    #     print("oops")
    print(f"Response: {response.json()}")
    # print(f"Response: {response.text}")
    print(f"Full Response Headers: {response.headers}")


if __name__ == "__main__":
    send_test_event()

