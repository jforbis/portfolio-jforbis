from flask import Flask, render_template, redirect, jsonify, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/make-that-bread", methods=['GET'])
def proj():
    return render_template("stock-predictor.html")


@app.route("/leaflet", methods=['GET'])
def leaf():
    return render_template("leaflet.html")

@app.route("/mpl", methods=['GET'])
def mat():
    return render_template("matplotlib.html")

if __name__ == "__main__":
    app.run(debug=True)