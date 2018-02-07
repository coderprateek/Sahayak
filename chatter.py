from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")
from chatterbot.trainers import ListTrainer
import sys
conversation = [
    # "Hello",
    # "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "You're welcome.",
    "Bye",
    "See You Soon!",
    "Good Day!"

]

chatbot.set_trainer(ListTrainer)
chatbot.train([
    "Hi there!",
    "Hello",
])

chatbot.train([
    "Greetings!",
    "Hello",
])
chatbot.train(conversation)

def get_output(text):
	response = chatbot.get_response(text)
	print(response)


text = sys.argv[1] ;
get_output(text)