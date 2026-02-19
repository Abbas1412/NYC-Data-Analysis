from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("airbnb_data.csv")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/notebook")
def notebook():
    return render_template("notebook.html")


if __name__ == "__main__":
    app.run(debug=True)
