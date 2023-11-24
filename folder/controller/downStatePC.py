import firebase_admin
from firebase_admin import credentials, db, storage
import time, threading

#Va a esperar hasta que photo sea igual a false, y se va a romper el ciclo, y continuara con todo
def downStatePc(app):
    ref = db.reference(app=app)
    parameterRef = ref.child('control/photo')
    
    while True:  # Ejecuta indefinidamente hasta que state sea False
        state = parameterRef.get()
        print(state)
        
        if not state:  # Sale del ciclo si state es False
        
            break
        print('downStatePC')
        time.sleep(5)   
