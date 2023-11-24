import firebase_admin
from firebase_admin import credentials, db

#Funcion que terminando de tomar la foto, mandara un trigger para iniciar el proceso desde la otra PC
def uploadStatePhoto(app, setup):
    ref = db.reference(app=app)
    parameterRef = ref.child('control/photo')
    state = parameterRef.set(setup)
    print('uploadPhoto')
    return state
