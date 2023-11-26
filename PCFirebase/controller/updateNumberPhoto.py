import firebase_admin
from firebase_admin import credentials, db

def updateNP(app):
    db_ref = db.reference(app=app)

    ref = db_ref.child("count/numberLett")

    state = ref.get()

    return state