from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This should be working now...."

if __name__ == "__main__":
    app.run(debug=False)