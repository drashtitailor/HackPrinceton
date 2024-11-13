import openai

def generate_chat_response(user_input):
    prompt = f"You are a helpful finance investment coach, you should carefully teach everything a user needs inroder to understand some concepts in stock investment. According to user input, give the user data base on what you have, as it is use for education purposes for user to learn investment:\n{user_input}"
    
    try:
        # Use the correct endpoint for chat models
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # You can use GPT-4 or another model, depending on what you have access to
            messages=[
                {"role": "system", "content": "You are a helpful finance investment coach, you should carefully teach everything a user needs inroder to understand some concepts in stock investment. "
                 "According to user input, give the user data base on what you have, as it is use for education purposes for user to learn investment."},
                {"role": "user", "content": user_input},
            ],
            max_tokens=150
        )
        return response['choices'][0]['message']['content'].strip()  # Extract the message content from the response
    except Exception as e:
        return f"Error generating response: {str(e)}"
