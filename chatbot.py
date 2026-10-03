def chatbot_response(user_input):
    # Convert input to lowercase for easy matching
    user_input = user_input.lower()
    
    # Conditional logic using if, elif, and else
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
    # Output initial greeting
    print("Chatbot: Hello! I'm your friendly Python bot. Type 'bye' to exit.")
    
    # Loop to keep the conversation running continuously
    while True:
        # Input from the user
        user_message = input("You: ")
        
        # Get the appropriate response using the function
        bot_reply = chatbot_response(user_message)
        
        # Output the bot's reply
        print(f"Chatbot: {bot_reply}")
        
        # Exit condition to break the loop
        if "bye" in user_message.lower():
            break

# Start the program
if __name__ == "__main__":
    run_chatbot()
