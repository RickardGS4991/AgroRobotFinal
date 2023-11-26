import firebase_admin
from firebase_admin import credentials, db

def updateState(data, app, newInfo, numberPhoto):
    db_ref = db.reference(app=app)

    ref = db_ref.child("lettuce/lett"+str(numberPhoto))
    refLocobot = db_ref.child("control/photo")

    ref.set(data)
    refLocobot.set(newInfo)