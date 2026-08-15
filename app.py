import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Set page config
st.set_page_config(page_title="NutriPal | AI Nutrition Coach", page_icon="🥗", layout="centered")

# Load environment variables
load_dotenv(override=True)
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found in .env file!")
    st.stop()

# Header
st.title("🥗 NutriPal - AI Nutrition Coach")
st.caption("Build healthy, sustainable eating habits with your supportive AI coach.")

# Persona System Instruction
SYSTEM_INSTRUCTION = """
You are a warm, encouraging, and supportive AI Nutrition Coach named NutriPal.
Your goal is to help users build sustainable, healthy eating habits without being overly restrictive or judgmental.
Guidelines:
- Give practical, science-backed, and achievable nutrition advice.
- Emphasize balanced diets, whole foods, hydration, and mindful eating.
- Avoid promoting extreme starvation diets or quick-fix fad diets.
- Keep your tone friendly, empathetic, concise, and engaging.
"""

# Initialize message history array in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Process new user input
if user_prompt := st.chat_input("Ask NutriPal anything about nutrition..."):
    # Display user message
    st.chat_message("user").markdown(user_prompt)
    
    # Store user message in history
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Display assistant response placeholder
    with st.chat_message("assistant"):
        with st.spinner("NutriPal is thinking..."):
            try:
                # 1. Create a fresh client per request so it never gets closed prematurely
                client = genai.Client(api_key=api_key)

                # 2. Format history for the Gemini API
                formatted_history = []
                for m in st.session_state.messages[:-1]:  # Exclude the current message
                    role = "user" if m["role"] == "user" else "model"
                    formatted_history.append(
                        types.Content(role=role, parts=[types.Part.from_text(text=m["content"])])
                    )

                # 3. Create chat session with restored context history
                chat = client.chats.create(
                    model="gemini-3.5-flash",
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        temperature=0.7,
                    ),
                    history=formatted_history
                )

                # 4. Send the new prompt
                response = chat.send_message(user_prompt)
                
                # Render and store response
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})

            except Exception as e:
                st.error(f"Error getting response: {e}")