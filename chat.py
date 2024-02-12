import random # to generate random values/ data
import json,os # to work with json files in case required
import re #to match with re( regularexpression) 
import torch # for tensors(n-D arrays)
from model import NeuralNet #from model.py create instance of class
from nltk_utils import bag_of_words, tokenize # for NLP, import bag_of_words to generate vector embeddings and import tokenize to break sentence into words
from resume import enter_html1,enter_html2,enter_html3 #from resume import functions for cretng resume
from careerguide1 import run_search # from careerguide1 import run_search for getting careerguidance through api.

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') #if CUDA is avaolable use CUDA for processing else use CPU

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

with open('intents1.json', 'r') as json_data1:
    regdata = json.load(json_data1)
intents1=regdata['intents']

outputdata=[] # variable to store user details


#A PTH file is a machine learning model created using PyTorch, an open-source machine learning library.
#PyTorch is a Python-based machine learning library that allows developers to create and save machine learning models.

FILE = "data.pth"
data = torch.load(FILE) #facilitates device to load data into FILE

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]


model = NeuralNet(input_size, hidden_size, output_size).to(device) #Returns a Tensor with the specified device and (optional) dtype.
#A state_dict is simply a Python dictionary object that maps each layer to its parameter tensor. 
model.load_state_dict(model_state)
model.eval() #kind of switch for some specific layers/parts of the model that behave differently during training and inference (evaluating) time.

bot_name = "resumebot"

def get_response(msg):
    sentence = tokenize(msg) # tolenize the inputted message msg
    X = bag_of_words(sentence, all_words) #convert into bag of words the input with the unique stemmed words 
    X = X.reshape(1, X.shape[0])  #shape[0] gives no. of rows in the array, 
    #The reshape() function is used to give a new shape to an array without changing its data.
    X = torch.from_numpy(X).to(device) #torch.from_numpy(X) creates a tensor from numpy ndarray 
    #required becoz tensors are backed by the accelerator memory like GPU and they are immutable, unlike NumPy arrays. 


    output = model(X)
    _, predicted = torch.max(output, dim=1) #returns the maximum value of all elements in the input tensor.dim (int) – the dimension to reduce.

    tag = tags[predicted.item()] #get the index using predicted.item() and access the value of the index in tags set and store it in var tag

    probs = torch.softmax(output, dim=1) #Applies the Softmax function to an n-dimensional input Tensor rescaling them so that the elements of the n-dimensional output Tensor lie in the range [0,1] and sum to 1.
    prob = probs[0][predicted.item()] #get first item
    if prob.item() > 0.75:
        for intent in intents['intents']:
            for pattern in intent['patterns']:
                if tag == intent["tag"] :
                    x={intent["tag"]:msg}
                    enter_json(x)
                    if intent['tag']=="email":
                        outputdata.append(msg)
                    elif intent['tag']=="ug":
                        outputdata.append(msg)
                    elif intent['tag']=="undergrad":
                        outputdata.append(msg)
                    elif intent['tag']=="ugcgpa":
                        outputdata.append(msg)
                        print(outputdata)
                    elif intent['tag']=="incolname":
                        outputdata.append(msg)
                    elif intent['tag']=="incgpa":
                        outputdata.append(msg)
                    elif intent['tag']=="schoolName":
                        outputdata.append(msg)
                    elif intent['tag']=="schoolper":
                        outputdata.append(msg)
                    elif intent['tag']=="techskills":
                        outputdata.append(msg)
                    elif intent['tag']=="protitle":
                        outputdata.append(msg)
                    elif intent['tag']=="protools":
                        outputdata.append(msg)
                    elif intent['tag']=="programminglanguages":
                        outputdata.append(msg)
                    elif intent['tag']=="webtechnology":
                        outputdata.append(msg)
                    elif intent['tag']=="database":
                        outputdata.append(msg)
                    elif intent['tag']=="opsys":
                        outputdata.append(msg)
                    elif intent['tag']=="courses":
                        outputdata.append(msg)
                    elif intent['tag']=="experience":
                        outputdata.append(msg)
                        print(outputdata)
                        enter_html1(outputdata)
                        enter_html2(outputdata)
                        enter_html3(outputdata)
                    return random.choice(intent['responses'])
    return "I did'nt understand please enter correctly..." # if no match found

def get_response1(msg):
    if msg=="stop"  or msg=="Stop" or msg=="STOP":
        outputdata.clear()
        return "Thank you"
    elif msg=="clear" or msg=="Clear" or msg=="CLEAR":
        print(outputdata)
        outputdata.pop()
        print(outputdata)
        return "Enter the previous information again"
    elif msg=="resume" or msg=="RESUME" or msg=="Resume":
        outputdata.clear()

  
    for intent in intents1:
        for pattern in intent['patterns']:
            if re.search(pattern,msg):
                y={intent["tag"]:msg}
                enter_json(y)
                if intent['tag']=="person_name":
                  outputdata.append(msg)
                elif intent['tag']=="phone_number":
                    outputdata.append(msg) 
                elif intent['tag']=="resiaddress":
                  outputdata.append(msg)
                elif intent['tag']=="linkedin":
                    outputdata.append(msg)
                elif intent['tag']=="careerobjective":
                    outputdata.append(msg)
                elif intent['tag']=="inyear":
                    outputdata.append(msg)
                elif intent['tag']=="github":
                    outputdata.append(msg)
                elif intent['tag']=="protitle2":
                    outputdata.append(msg)
                elif intent['tag']=="protools2":
                    outputdata.append(msg)
                elif intent['tag']=="prodes":
                    outputdata.append(msg)
                elif intent['tag']=="careerassistance":
                    search=[]
                    search=msg.split(':')
                    return run_search(search[1])
                elif intent['tag']=="prodes2":
                    outputdata.append(msg)
                    print(outputdata)
                return intent['responses']
    return get_response(msg)

def enter_json(data,filename="data1.json"):
    with open(filename,'r+') as file:
        file_data=json.load(file)
        file_data["person_details"].append(data)
        file.seek(0)
        json.dump(file_data,file,indent=4)
#If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”.
# If this file is being imported from another module, __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable.
if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    filename='data.json'
    
    while True:
        sentence = input("You: ") # take user input
        if sentence == "quit":
            print("done")
            break
       
        resp = get_response1(sentence)# function call with user input as parameter
        print(resp) #display response on screen

    


