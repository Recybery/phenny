import random
answers=[
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful" ,
]
def fortune(phenny, input):
    phenny.say(answers[random.randrange(0,len(answers))])
fortune.commands=['m8b']
fortune.priority='medium'


                       
                       
                       
                       
                       
                       