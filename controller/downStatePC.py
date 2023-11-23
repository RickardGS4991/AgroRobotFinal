import firebase_admin
import time, threading

#Va a esperar hasta que photo sea igual a false, y se va a romper el ciclo, y continuara con todo
def downStatePc(app):
    
    ref = db.reference(app=app)
    parameterRef = ref.child('control/photo')
    state = parameterRef.get()
    
    while state:
        print(state)
        state = ref.get()
        time.sleep(5)
        
thread1 = threading.Thread(target=downStatePc)
thread1.start()    
