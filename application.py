from flask import Flask, render_template
import os

application = Flask(__name__,  template_folder='/templates')
app.debug = True
app.run()


@application.route('/')
def root():
    return render_template('index.html')

@application.route("/help")
def helppage():
    return render_template("help.html")

@application.route("/hello")
def hellopage():
    NAME_F = os.getenv('NAME_FIRST', 'Thomas')
    NAME_L = os.getenv('NAME_LAST', 'Anderson')
    HELLO_MESSAGE = "Hello, Mr. " + NAME_F + " " + NAME_L
    return HELLO_MESSAGE

### MAIN ###
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080)
### ---- ###