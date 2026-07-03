from flask import Flask
from flask import render_template
from flask import request

from utils.predictor import predict_crop

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])

    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    crop = predict_crop(
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    )

    return render_template(
        "index.html",
        prediction_text=crop
    )


if __name__ == "__main__":

    app.run(debug=True)