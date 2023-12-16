import os

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat()
response = chat.send_message('Hello, what should I have for dinner?')
print(response.text)  # 'Here are some suggestions...'
response = chat.send_message("How do I cook the first one?")
