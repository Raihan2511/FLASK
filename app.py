from flask import Flask
# wbsgi application

app=Flask(__name__)

# decorator
@app.route('/')
def welcome():
    return "welcome to my page,my name is Raihan"

if __name__=='__main__':
    app.run(debug=True)

