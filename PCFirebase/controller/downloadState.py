import firebase_admin
from firebase_admin import credentials, db

def downState(app):
    db_ref = db.reference(app=app)

    ref = db_ref.child("control/photo")

    state = str(ref.get())

    newRunningValue = state.capitalize()
    newRunningBool = newRunningValue == "True"


    return newRunningBool