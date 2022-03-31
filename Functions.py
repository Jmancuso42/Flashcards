 
import json
import random





class ioTools:


    ##maybe make a function that puts all the questions into a list, and either seperate or same function into an

    def bufferQuestion():
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
