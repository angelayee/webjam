from flask import Flask, render_template, request

app = Flask(__name__)

# Define your route for the homepage
@app.route('/')
def index():
    return render_template('index.html')  # Make sure you have an 'index.html' template

if __name__ == '__main__':
    app.run(debug=True)