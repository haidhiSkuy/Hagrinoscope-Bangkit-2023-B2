import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import re

# Use a service account.
cred = credentials.Certificate('tes-capstone-firebase-adminsdk-tsmq6-ce0bfdabfd.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()


def give_recommendation(fruit_prediction, soil_prediction):
    fruit_name = re.sub(r".+_", "", fruit_prediction)
    doc_ref = db.collection("fruit").document(fruit_name)
    doc = doc_ref.get()
    recommendation_data = doc.to_dict()
    return recommendation_data[fruit_prediction], recommendation_data[soil_prediction]