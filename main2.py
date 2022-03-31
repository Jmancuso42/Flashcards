import json

from cupshelpers import Printer

#for now, load two different files into memory hard code

techQuiz = 'questionsMC.json'
musicQuiz ='questions.json'

#How To do?
#advanced would be to have a way to *find* a json file in a folder and select to load
#and also to be able to do CRUD for new quiz files



#put in a menu/orther input in future for quiz selection


#this works with the non multiple choice file
with open(musicQuiz, 'r') as file:
    data = json.load(file)
    total = len(data["cards"])
    score = 0
    #reads data inside what matches "cards"

    #How to index via other than Key item versus 'q' or 'a', so that it
    #is reusable for differently configged json files?
    for card in data["cards"]:

        guess = input(card['q']+" > ")
        if guess.lower() == card['a'].lower():
            print(f"Great Success! Very nice \n Score:  {score}/{total}")
            score += 1
        #slight pause?
    else:
            print("Wroooong! The right answer was ", card["q/"])
            print(f"Score: {score}/{total}")


