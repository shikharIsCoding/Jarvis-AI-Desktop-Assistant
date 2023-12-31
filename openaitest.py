from openai import OpenAI
from hidden import apikey
import os

# Initialize the client with your API key
client = OpenAI(api_key=apikey)

# Create a completion request to the API
response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write an email to my boss for resignation?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Extracting the text from the response object
resignation_letter = response.choices[0].text
print("Resignation Letter:")
print(resignation_letter)
