from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return " Aplicación desplegada con Cloud Build + Cloud Run + triger"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
