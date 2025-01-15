from flask import Flask
# wbsgi application

app=Flask(__name__)

# decorator
@app.route('/')
def welcome():
    return "welcome to my page,my name is Raihan"

if __name__=='__main__':
    app.run(debug=True)
# from flask import Flask

# # Create a Flask application instance
# app = Flask(__name__)

# # Define a route for the home page
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# # Define a route for another page
# @app.route('/about')
# def about():
#     return 'This is the about page!'

# # Run the app (For development only, we won't use this in production)
# if __name__ == '__main__':
#     app.run(debug=True)

