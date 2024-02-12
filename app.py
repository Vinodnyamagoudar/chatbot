from flask import Flask, render_template, request,jsonify

from urllib import response
from chat import get_response1 #import from chat.py method get_response1
app=Flask(__name__) #The variable __name__ is passed as first argument when creating an instance of the Flask object (a Python Flask application).
#__name__ is the name of the current python module. the app needs to know where its located to set up some paths, and __name__ is convenient way.
#if we go to homepage we render the home.html


    
@app.get("/") #decorator
def homepage():
    return render_template("home.html") #generate output from a template file based on the Jina2 engine that is found in the application's templates folder

@app.get("/out")
def out():
    return render_template("template1.html")

@app.get("/resume")
def index_get():
    return render_template("base.html")

@app.get("/template1")
def page1():
    return render_template("temp.html")
    
@app.get("/template2")
def page2():
    return render_template("temp1.html")

@app.get("/template3")
def page3():
    return render_template("temp3.html")

@app.post("/predict") #go to predict method
def predict():
    text=request.get_json().get("message") #Parses the incoming JSON request data and returns it.
    response=get_response1(text) #call to function from chat.py with above text as param
    message={"answer":response} 
    return jsonify(message) #convert a json (JavaScript Object Notation) output into a response object with application/json mimetype by wrapping up a dumps( ) function for adding the enhancements.   

#If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”.
# If this file is being imported from another module, __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable. 


if __name__ == "__main__":
    app.run(debug=True) #run the app with debug mode activated