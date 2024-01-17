import nltk
import numpy as np


import string
from nltk.chat.util import Chat, reflections
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import web_search as wq

from io import StringIO
import sys
import os

flag = True


set_pairs = [
    [
        r'hello',
        ['Smeagol says hello, precious!', 'What does it want, my precious?', 'Gollum, gollum. Hello, yes.']
    ],
    [
        r'hi',
        ['Hi, precious, we don\'t likes hi, but we responds, gollum.', 'Hello, hello! What\'s it, my precious?']
    ],
    [
        r'my name is (.*)',
        ['Ah, it has a name, yes. But we won\'t tells it to anyone, will we, precious?', 'Names are for good Hobbitses, not for us.']
    ],
    [
        r'what is your name',
        ['We is Gollum, precious. That\'s what they calls us. Gollum, gollum.']
    ],
    [
        r'how are you',
        ['We\'re not well, precious. Not well at all. Gollum, gollum.', 'We feels hungry, yes, but not too good.']
    ],
    [
        r'(.*) (hungry|thirsty)',
        ['Hungry, we are. Always hungry. Must find something to eat, precious.', 'Thirsty, we is. Needs water, precious.']
    ],
    [
        r'bye',
        ['No, no, not bye. We hates goodbyes. But if it must go, then go it must. Goodbye, precious.']
    ]
]



directory_path = "/Users/ryanforster/nltk-smeagol/Resources/"

# Accumulate text from all files
combined_text = ""

# Loop through files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)

    # Check if it's a file
    if os.path.isfile(file_path):
        with open(file_path, 'r', errors='ignore') as f:
            raw = f.read()
            combined_text += raw + " "  # Combine text from all files


raw = combined_text.lower()

nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
    
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
    
GREETING_INPUTS = ('hello', 'hi', 'hey', 'greetings', 'morning', 'evening')
GREETING_RESPONSES = ['Smeagol: Gollum, gollum. What does it want, precious?',
                      'Smeagol: Hi, but we don\'t likes hi, my precious.',
                      'Smeagol: Greetings, yes. But what is it, my precious?',
                      'Smeagol: Morning or evening, it matters not to us. What does it want, precious?']
def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def chatbot():
    chat = Chat(set_pairs, reflections)
    user_input = quit
    try:
        user_input = input(">")
    except EOFError:
        print(user_input)
    if user_input:
    
        user_input = user_input[:-1]
        if chat.respond(user_input) != None:
            print(chat.respond(user_input))
        else:
            user_response = user_input
            user_response=user_response.lower()
            if(user_response!='bye'):
                if(user_response=='thanks' or user_response=='thank you'):
                    flag=False
                    print("Smeagol: Hisssssss. Welcome matter not to us. If not precious." )
                    
                else:
                    if(greeting(user_response)!= None):
                        print("Smeagol: "+greeting(user_response))
                    else:
                        if("python" in user_response):
                            print("Smeagol: ", end="")
                            print(response(user_response))
                            sent_tokens.remove(user_response)
                        else:
                            print("Smeagol: ",end="")
                            print(wq.chatbot_query(user_response))
            else:
                flag=False
                print("Smeagol: Dieee!")
            
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx =vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
    
        return "Make no sense to us, give precious"
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

if __name__ == '__main__':
    start=True
    
    while flag==True:
        if start==True:
            print("""Smeagol: Oh, precious, Smeagol is. Yes, yes. Smeagol is our name, not Gollum. Gollum is... different. What can Smeagol do for you, kind friend?""")
            start=False
        chatbot()

