from flask import Flask, render_template, redirect, jsonify, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/make-that-bread", methods=['GET'])
def proj():
    return render_template("stock-predictor.html")


# @app.route("/projects", methods=['GET'])
# def proj():
#     return render_template("under_construction.html")

if __name__ == "__main__":
    app.run(debug=True)