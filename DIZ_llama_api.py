"""
Main file for the DIZ Llama API
Version:    0.1
Date   :    12.12.2024
Author :    Eric Einspänner
Mail   :    eric.einspaenner@med.ovgu.de
"""

# **************************************************************************
# * Import
# **************************************************************************
import os
import requests
from dotenv import load_dotenv


# **************************************************************************
# * Init
# **************************************************************************
# Load API keys
load_dotenv()
DIZ_API_KEY = os.getenv("DIZ_API_KEY")

# Define the API endpoint and headers
url = "https://ki-plattform.diz-ag.med.ovgu.de/api/chat/completions"
headers = {
    "Authorization": f"Bearer {DIZ_API_KEY}",
    "Content-Type": "application/json"
}


# **************************************************************************
# * Function
# **************************************************************************
def request_DIZ_llama(prompt: str) -> str:
    r"""
    Send a prompt to DIZ API (Llama) and return the response.

    Args:
        - prompt: The prompt to send to the API.

    Returns:
        The response from the API.
    """
    # Define the JSON data to be sent in the POST request
    data = {
        "model": "llama3.2-vision:90b",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    # Make the POST request using the requests library
    response = requests.post(url, headers=headers, json=data)

    return response.json().get("choices")[0].get("message").get("content")
    

# **************************************************************************
# * Main
# **************************************************************************
if __name__ == '__main__':

    # Test the DIZ Llama API
    response = request_DIZ_llama("What is the capital of Germany?")
    print(response)