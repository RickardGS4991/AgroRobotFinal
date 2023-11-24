import firebase_admin
from firebase_admin import credentials, db

#COn esta funcion, comenzamos todo el proceso del locobot
def downStatePhoto(app):
    ref = db.reference(app=app)
    parameterRef = ref.child('control/locobot')
    state = parameterRef.get()
    print('downStatePhoto')
    return state
