print("Welcome to the Rule-Based Chatbot!")
print("Type 'bye' to exit the chatbot.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user_input:
        print("Bot: My name is CodSoft Chatbot.")

    elif "help" in user_input:
        print("Bot: I can answer simple questions and have a basic conversation.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
