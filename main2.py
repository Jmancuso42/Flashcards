from fileinput import filename
import json, os 

from cupshelpers import Printer

#modularizeEee?
def user_quiz_select(path_to_json):
#for now, load two different files into memory hard code
#`How To do?
#advanced would be to have a way to *find* a json file in a folder and select to load
#and also to be able to do CRUD for new quiz files
#enumerate from all json items in a filepath
#boop into a list
#match case of options via user choice of enumerator index
#load that json filestring into a variable 
#return filestring and pass it into other functions


    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')] #the logic is loopy here

    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json,js)) as cur_json_file:       
            print(f"Option {index}. {js}")
            
    quiz_choice = input("choose a quiz to load ")
    
    loaded_text = json.load(cur_json_file)






def game_run_loop(path_to_json):
    
#put in a menu/orther input in future for quiz selection


#this works with the non multiple choice file
    #how to make this look more flecible? json formatting?
    with open(path_to_json, 'r') as file:
        
        data = json.load(file);
        total = len(data["cards"]);
        score = 0;
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
              print("Wroooong! The right answer was ", card["q/"])               print(f"Score: {score}/{total}")


