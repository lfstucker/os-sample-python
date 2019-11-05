from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!, testing to learn how to redeploy!"

if __name__ == "__main__":
    application.run()
