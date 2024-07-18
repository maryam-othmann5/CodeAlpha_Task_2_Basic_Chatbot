
#task 2 : Basic Chatbot
import nltk
from nltk.chat.util import Chat, reflections

# Define reflections for the chatbot
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I am fine, thank you."],
    ],
    [
        r"sorry (.*)",
        ["Apologies for the inconvenience.", "No problem, take your time."],
    ],
    [
        r"(.*) (good|great|fine|ok)",
        ["That's good to hear!", "Awesome!", "Great! How can I assist you further?"],
    ],
    [
        r"(.*) age?",
        ["I'm just a computer program, age doesn't apply to me.",]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to assist you with any questions or tasks you have.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm an online chatbot, so I'm everywhere!"]
    ],
    [
        r"exit",
        ["Goodbye! Have a nice day!", "Bye! Take care."]
    ],
]

# Define a function to start the chatbot
def chatbot():
    print("Hello! I'm ChatBot. How can I assist you today? (type 'exit' to end the conversation)")

    # Create a Chat instance with pairs and reflections
    chat = Chat(pairs, reflections)

    # Start the conversation loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            response = chat.respond(user_input)
            print(response)
            break
        else:
            response = chat.respond(user_input)
            print("ChatBot:", response)

# Call the chatbot function to start the conversation
if __name__ == "__main__":
    chatbot()