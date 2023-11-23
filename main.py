from controller.uploadPhoto import uploadPhoto
from controller.takephoto import takePhoto
from controller.downStatePhoto import downStatePhoto
from controller.uploadStatePhoto import uploadStatePhoto
from controller.downStatePC import downStatePc
import firebase_admin
from firebase_admin import credentials, db, storage
import time
import threading

running = False
setup = False
cred = credentials.Certificate("./key.json")
app1 = firebase_admin.initialize_app(cred, {"databaseURL": "https://ga-ulv-default-rtdb.firebaseio.com/"}, name='app1')
app2 = firebase_admin.initialize_app(cred, {"storageBucket": "ga-ulv.appspot.com"}, name='app2')

def executeLoco():
    while True:
        running = downStatePhoto(app1)
        if running:
            takePhoto()
            uploadPhoto("/home/locobot/interbotix_ws/src/image_detect_pkg/src/image/locobotFirebase/photos/lettuce.jpg", "storage.jpg", app2)
            setup = True
            uploadStatePhoto(app1, setup)
            downStatePc(app1)
        time.sleep(5)

thread1 = threading.Thread(target=executeLoco)
thread1.start()
   
