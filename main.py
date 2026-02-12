from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# 2. Retrieve the variable using os.getenv()
api = os.getenv("MY_SECRET_API_KEY")

api= "AIzaSyBqV0eGY_Q10_As21LxuqU-nZ1daDzAGh4"

ai = genai.Client(api_key=api)

response= ai.models.generate_content(
    model="gemini-2.5-flash",
    contents="how to get more likes ?"
)

print(response.text)