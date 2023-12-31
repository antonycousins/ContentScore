import requests
from dotenv import load_dotenv

load_dotenv()

OPENAPI_KEY = os.getenv("OPENAI_KEY")

headers = {
    'Authorization': f'Bearer {OPENAPI_KEY}',
    'Content-Type': 'application/json',
}

data = {
    "model": "gpt-3.5-turbo-instruct",
    "prompt": "rate the following headline for how clickbaity it is on a scale of 0.0 (certainly not clickbait) to 1.0 (certainly clickbait). Respond only with the score.: '{{you'll never guess what he did}}'",
    "temperature": 0.0,
    "max_tokens": 150
}

response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)

print(response.json())
