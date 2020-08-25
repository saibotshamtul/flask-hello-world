from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def hello():
    #return "Hello! This is a basic Flask app."
	return Response("Hello! This is a <b>basic</b> Flask app.",mimetype="text/html")

if __name__ == "__main__":
    app.run("0.0.0.0")
