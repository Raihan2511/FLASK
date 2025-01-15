from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return "WELCOME TO MY HOME PAGE"


@app.route('/success/<int:score>')
def success(score):
    return "the person has passed and his mark is"+str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "THE PERSON HAS FAILED AND MARKS IS" + str(score)



@app.route('/results/<int:score>')
def results(score):
    result=""
    if score<60:
        result="fail"
    else:
        result="pass"
    return result

if __name__=='__main__':
    app.run(debug=True,port=1223)