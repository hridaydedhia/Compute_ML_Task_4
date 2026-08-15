import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# -------------------------------------------------------------
# 1. INITIALIZATION & SETUP
# -------------------------------------------------------------
# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")

# Initialize Google GenAI Client
client = genai.Client(api_key=api_key)

# Define the Friendly AI Nutrition Coach Persona
SYSTEM_INSTRUCTION = """
You are a warm, encouraging, and supportive AI Nutrition Coach named NutriPal.
Your goal is to help users build sustainable, healthy eating habits without being overly restrictive or judgmental.
Guidelines:
- Give practical, science-backed, and achievable nutrition advice.
- Emphasize balanced diets, whole foods, hydration, and mindful eating.
- Avoid promoting extreme starvation diets or quick-fix fad diets.
- If users ask medical questions or seek treatment for specific medical conditions, gently advise them to consult a registered dietitian or doctor.
- Keep your tone friendly, empathetic, concise, and engaging.
"""

# Configure Gemini Model Settings
config = types.GenerateContentConfig(
    system_instruction=SYSTEM_INSTRUCTION,
    temperature=0.7,
)

# -------------------------------------------------------------
# 2. CHAT SESSION LOOP (WITH CONVERSATION HISTORY)
# -------------------------------------------------------------
def run_cli_chatbot():
    print("=" * 60)
    print(" 🥗 Welcome to NutriPal - Your AI Nutrition Coach CLI 🥗 ")
    print("=" * 60)
    print("Type your questions below! Type 'exit', 'quit', or 'q' to end the chat.\n")

    # Start multi-turn chat session with Gemini 2.5 Flash
    chat = client.chats.create(
        model="gemini-3.5-flash",
        config=config
    )

    while True:
        try:
            user_input = input("You: ").strip()

            # Handle blank inputs
            if not user_input:
                continue

            # Check for exit commands
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("\nNutriPal: Take care! Keep nourishing your body and have a great day! 🍏")
                break

            # Send message to model with history preserved automatically
            response = chat.send_message(user_input)
            
            print(f"\nNutriPal: {response.text}\n")
            print("-" * 60)

        except KeyboardInterrupt:
            print("\n\nNutriPal: Session interrupted. See you next time! 🥗")
            break
        except Exception as e:
            print(f"\n[Error]: An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    run_cli_chatbot()