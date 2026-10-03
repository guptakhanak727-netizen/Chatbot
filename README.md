# Chatbot
# Simple Python Chatbot

A lightweight, rule-based chatbot built entirely in **Python**. It does not require any external packages or complex machine-learning libraries. Instead, it relies purely on core programming fundamentals: functions, continuous execution loops, and conditional pattern matching.

## 🚀 Features
* **Zero External Dependencies:** Built using only standard Python built-ins (`print`, `input`).
* **Persistent Session Loop:** Keeps the conversation going until explicitly closed.
* **Case-Insensitive Input Processing:** Recognizes triggers regardless of whether they are typed in uppercase, lowercase, or mixed case.
* **Modular Architecture:** Separates conversational text evaluation from input/output orchestration.

## 🛠️ Prerequisites
* **Python 3.x** installed on your system.

## 📂 Project Structure
```text
.
├── chatbot.py   # The executable source code file
└── README.md    # Documentation (This file)
```

## 💻 Getting Started

### 1. Installation
Clone or download this repository. Alternatively, copy the source code block below into a new file named `chatbot.py`:

```python
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I am just a Python program, but I am doing great!"
    elif "your name" in user_input:
        return "I am a simple rule-based chatbot built with Python."
    elif "help" in user_input:
        return "You can say hello, ask how I am, ask my name, or type 'bye' to exit."
    elif "bye" in user_input:
        return "Goodbye! Have a wonderful day!"
    else:
        return "I don't understand that. Type 'help' for options."

def run_chatbot():
    print("Chatbot: Hello! I'm your friendly Python bot. Type 'bye' to exit.")
    
    while True:
        user_message = input("You: ")
        bot_reply = chatbot_response(user_message)
        print(f"Chatbot: {bot_reply}")
        
        if "bye" in user_message.lower():
            break

if __name__ == "__main__":
    run_chatbot()
```

### 2. Running the Application
Open your terminal or command prompt, navigate to the directory holding your file, and run:

**Windows Command Prompt:**
```bash
python chatbot.py
```

**macOS / Linux Terminal:**
```bash
python3 chatbot.py
```

## ⚙️ How It works

* **Function Segmentation (`def`):** `chatbot_response()` maps input text strings to predetermined response phrases, keeping string filtering isolated. `run_chatbot()` handles interactive console loops and user updates.
* **Infinite Execution (`while True`):** Holds the terminal session open to process subsequent commands smoothly without forcing a manual application reload.
* **Sub-String Validation (`if/elif/else`):** Scans the input text using the `in` operator. Rather than demanding exact dictionary matches, it looks for target trigger words anywhere within your phrase.
* **Loop Termination Sequence (`break`):** Intercepts the `"bye"` phrase to break out of the infinite processing loop and exit safely back to the default system command prompt.
