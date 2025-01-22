### INTEGRATE HTML WITH PYTHON/
# HTTP VERB AND GET AND POST METHODS

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index2.html')


@app.route('/success/<int:score>')
def success(score):
    return render_template('results.html',result='pass',score=score)


@app.route('/fail/<int:score>')
def fail(score):
    return "THE PERSON HAS FAILED AND MARKS IS " + str(score)



@app.route('/results/<int:score>')
def results(score):
    result=""
    if score<=60:
        result="fail"
    else:
        result="pass"
    return redirect(url_for(result,score=score)) 



@app.route("./submit",methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        english=float(request.form['english'])
        social=float(request.form['social'])
        total_score=science+maths+english+social
        res=""
        if total_score<=60:
            res="fail"
        else:
            res="pass"
        


if __name__=='__main__':
    app.run(debug=True,port=1223)