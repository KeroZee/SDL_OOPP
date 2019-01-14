from flask import render_template, Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('SDL.html')

if __name__ == "__main__":
    app.secret_key='secret123'
    app.debug = True
    app.run(port='80')