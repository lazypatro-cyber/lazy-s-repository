# to make ai chat bot assistant
# to print the introduction of the chat bot and its use.
print('hello!!!!')
print('my name is motivational chatex.')
print('i am motivational personal chat assistant bot.')
print('I will motivate you to do execute your task irrespective of the domain.')

# The Question dictionary must be defined and uncommented so the program can access it
Question = {
    'not able to score good.': 'you have to practise. its make a man perfect.',
    'getting distracted': 'try to focus by being a quiet type environment.',
    'not getting anything': 'ask more question the one who asks is more wiser.',
}

def responses(response):
    response = response.lower()
    for i in Question:
        if i in response:
            return Question[i]

    return 'i cant process as i have not learnt yet.' 

while True:
    userinput = input('what new today: ')
    
    if 'bye' in userinput.lower():
        print('Goodbye!')
        break
        
    reply = responses(userinput)
    print('bots reply- ', reply)
