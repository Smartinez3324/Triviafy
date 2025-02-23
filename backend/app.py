from flask import Flask, render_template

app = Flask(__name__)

'''
Home Redirect
'''
@app.route("/")
def hello_world():
    return render_template('idk.html')
