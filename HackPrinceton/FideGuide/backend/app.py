from flask import Flask, request, jsonify
import openai
import yfinance as yf
from chatbot import generate_chat_response
from stock_data_fetcher import fetch_stock_data
from flask_cors import CORS 
import os # Import CORS
from dotenv import load_dotenv

app = Flask(__name__)

# Enable CORS for all routes (you can restrict this later if needed)
CORS(app)  # This allows your frontend to communicate with the backend
load_dotenv()
# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    if user_input.lower().startswith("stock"):
        # If the user asks for stock information, retrieve stock data
        stock_symbol = user_input.split()[1].upper()  # Assume the second word is the stock symbol
        stock_data = fetch_stock_data(stock_symbol)
        return jsonify({"response": stock_data})
    else:
        # Use OpenAI API to generate a chatbot response
        response = generate_chat_response(user_input)
        return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
