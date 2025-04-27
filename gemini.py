import google.generativeai as genai
#get an api key from "https://aistudio.google.com/apikey"
API_KEY="AIzaSyBxWIWCGfP12Y0DKWq2adEXybF8fQgJ2JQ"
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel("gemini-2.0-flash")
chat=model.start_chat()
print("Chat with Gemini! Type 'exit' to quit.")
while True:
    user_input=input("You:")
    if user_input.lower=='exit':
        break
    response=chat.send_message(user_input)
    print("Gemini:",response.text)