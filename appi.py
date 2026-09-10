from flask import Flask
app = Flask(_name_)

@app.route('/')
def home():
    return "Hello, this is my Task Manager project!"

if _name_ == '_main_':
    app.run(debug=True)
