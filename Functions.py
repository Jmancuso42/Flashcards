 
import json
import random
import os




class ioTools:


    def printListOfQuizzes(path_to_json):
        for fileName in [filePos for filePos in os.listdir(path_to_json) if file.endswith('.json')]
        i = 0
        with open(path_to_json + fileName) as jsonFile:
        
            quizName = fileName
 #       quizFile = json.load(jsonFile)
            print(f"{quizName}")
            i += 1
            


    ##maybe make a function that puts all the questions into a list, and either seperate or same function into an

    def bufferQuestion():
        #scrap function right now 
        superDict = {"Q", "C", "A"}

        with open('questionsAlt.json','r') as json_file:
        ### Grab jason data

            quizData = json.load(json_file)
            questions = []
            choices = []
            for i in quizData:
                #i think i need to iterate into a dictionary and see if I can return it and then shuffle it, then print it
                questions = questions.append([quizData][quiz][i]["question"])
                print(questions[i])
                choices = choices.append([quizData]["quiz"][i]["choices"])
                print(choices[i])

            superDict




        ## return value
    def shuffleQuestions(superDict):

        return ""
    def playGame():
        buferQuestion()
