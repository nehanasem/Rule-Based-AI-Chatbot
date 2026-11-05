
# =====================================
# Project: Rule-Based AI Chatbot
# Internship: DecodeLabs
# =====================================

import random
import re

# Knowledge base: predefined responses
responses = {
    "hello": "Hello! Welcome to my chatbot.",
    "hi": "Hi there! How can I help you?",
    "hey": "Hey! Nice to meet you.",
    "how are you": "I'm doing great! Thanks for asking.",
    "who are you": "I am a simple rule-based AI chatbot.",
    "what is your name": "You can call me ChatBot.",
    "thank you": "You're welcome!",
    "thanks": "Happy to help!",
    "bye": "Goodbye! Have a wonderful day.",
    "exit": "Goodbye! See you again.",
    "quit": "Goodbye! Take care.",
    "good morning": "Good morning! Hope you have a wonderful day.",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! Nice to hear from you.",
    "good night": "Good night! Sweet dreams.",
    "how is your day": "My day is going great! How about yours?",
    "what can you do": "I can respond to greetings, answer simple questions, and chat with you!",
    "help": "Sure! You can greet me, ask how I am, or type 'exit' to end our conversation."
}

# Fallback responses
fallback_responses = [
    "I'm not sure I understand. Could you rephrase that?",
    "That's interesting! Can you tell me more?",
    "Hmm, I don't know the answer to that yet.",
    "I'm still learning. Try asking me something else!",
    "Could you use different words? I want to understand you."
]

# Keyword categories
keywords = {
    "greeting": ["hello", "hi", "hey", "hye"],
    "food": ["pizza", "food", "burger", "burgers"],
    "wellbeing": [
        "how are you",
        "how are you doing",
        "how you doing",
        "how's it going",
        "how are things"
    ],
    "thanks": ["thanks", "thank you", "thankyou"]
}

# Starting chatbot
print("Chatbot: Hello! Welcome. Type 'exit' to end the chat.")

# Continuous conversation
while True:

    # Taking and cleaning user input
    user_input = input("You: ").lower().strip()
    user_input = user_input.rstrip("?!.,")

    # Checking exit command
    if user_input in ["bye", "exit", "quit"]:
        print("Chatbot:", responses.get(user_input))
        break

    # Checking empty input
    if user_input == "":
        print("Chatbot: You didn't type anything. Please say something!")
        continue

    # Checking exact predefined responses first
    if user_input in responses:
        reply = responses[user_input]

    else:
        # Checking keyword categories
        matched_response = None

        for intent, words in keywords.items():
            if any(
                re.search(r"\b" + re.escape(word) + r"\b", user_input)
                for word in words
            ):

                if intent == "greeting":
                    matched_response = "Hello! It's lovely to chat with you."

                elif intent == "food":
                    matched_response = "I don't eat, but that sounds delicious!"

                elif intent == "wellbeing":
                    matched_response = "I'm doing great! Thanks for asking."

                elif intent == "thanks":
                    matched_response = "You're very welcome!"

                break

        # Selecting keyword response or fallback
        if matched_response:
            reply = matched_response
        else:
            reply = random.choice(fallback_responses)

    # Displaying chatbot response
    print("Chatbot:", reply)

# Ending conversation
print("Chatbot: Conversation ended.")
