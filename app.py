from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore
import json

app = Flask(__name__)
app.config.from_object("config.Config")

# Initialize Firebase Admin SDK
cred = credentials.Certificate(app.config["FIREBASE_CONFIG"])
firebase_admin.initialize_app(cred)

# Firebase Firestore
db = firestore.client()


def get_mock_data():
    with open("mock_data.json") as f:
        restaurants = json.load(f)["restaurants"]
    return restaurants


def get_restaurants():
    # Get all documents from the restaurants collection
    restaurants = db.collection("restaurants").get()
    restaurants = [restaurant.to_dict() for restaurant in restaurants]
    return restaurants


def add_restaurant(restaurant):
    # Add a new document
    db.collection("restaurants").add(restaurant)


@app.route("/")
def index():
    restaurants = get_mock_data()
    return render_template("index.html", restaurants=restaurants)


if __name__ == "__main__":
    app.run(debug=True)
