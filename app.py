from flask import Flask
from app1 import demo

app = Flask(__name__)

@app.route("/")
def home():
    return demo()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
