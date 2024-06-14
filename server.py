from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Welcome To Github Actions Page This Is New JIRA"
if __name__ == "__main__":
        app.config['TEMPLATES_AUTO_RELOAD'] = True
        app.run(host='0.0.0.0', debug=True, port=8080)
