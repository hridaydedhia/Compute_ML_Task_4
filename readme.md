# 🥗 NutriPal - LLM-Powered AI Nutrition Coach

A friendly, supportive CLI and Web-based AI Nutrition Coach built using Python and the **Google GenAI SDK (`gemini-2.5-flash`)**. NutriPal helps users build sustainable eating habits, balance their diets, and stay motivated on their wellness journey.

---

## 📌 Features

- **Personalized Persona:** Configured with system instructions to act as an encouraging, empathetic nutrition guide.
- **Context-Aware Memory (Brownie Point):** Maintains complete session chat history so users can follow up on previous conversation context.
- **Secure Credentials:** API keys are managed securely via environment variables (`.env`) to avoid exposing credentials.
- **Dual Interface:**
  - **CLI Mode:** Fast terminal-based interaction.
  - **Streamlit Web UI (Brownie Point):** Interactive web application.

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- Python 3.9 or higher installed on your system.
- A **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/).

### 2. Clone Repository & Setup Virtual Environment
```bash
git clone [https://github.com/YOUR_USERNAME/djs-compute-task4.git](https://github.com/YOUR_USERNAME/djs-compute-task4.git)
cd djs-compute-task4

# Create & activate virtual environment
python -m venv venv

# Windows Command Prompt:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate