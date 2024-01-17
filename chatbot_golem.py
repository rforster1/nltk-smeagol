import nltk
from nltk.chat.util import Chat, reflections

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
    ],
    [
        r'(.*)',
        ['What does it say, my precious? We listens.', 'Speak, speak, speak!']
    ]
]

def chatbot():
    print("Smeagol: Hi, it's Smeagol, the chatbot. They calls me Gollum, they does. What does it want, precious?")
    chat = Chat(set_pairs, reflections)
    chat.converse()

if __name__ == '__main__':
    chatbot()

