from cgitb import html
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jobs/create', methods=['GET', 'POST'])
def create_new_job():
    return "Done, i have access now"











if __name__ == "__main__":
    app.run("localhost", port=5000)