from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Jesus Loves You and Me and All:)"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
