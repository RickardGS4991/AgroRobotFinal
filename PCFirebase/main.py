from controller.downloadPhoto import downloadPhoto
from controller.sickDetect import sickDetect
from controller.updateState import updateState
from controller.detectLettuce import detectObjects
from controller.downloadState import downState
from controller.updateNumberPhoto import updateNP
from firebase_admin import credentials
import firebase_admin
import threading
import time

running = False

cred = credentials.Certificate("./key.json")
app = firebase_admin.initialize_app(cred, {"storageBucket": "ga-ulv.appspot.com"})

app2 = firebase_admin.initialize_app(cred, {
    "databaseURL": "https://ga-ulv-default-rtdb.firebaseio.com/"
}, name="app2")

def fiveSeconds():
    while True:
        running = downState(app2)
        if running:
            numberPhoto = updateNP(app2)
            downloadPhoto("storage.jpg", app)
            lettuceBoolean = detectObjects('C:/Users/labra/Desktop/LettuceDetect/photos/banana.jpg')

            if lettuceBoolean:
                print("Holi")
                data = sickDetect("/Users/ritchie928/Desktop/firebaseLocobot/photos/lettuce.jpg")

                updateState(data, app2, False, numberPhoto)
                print("Finish")
            else:
                print('error, it is not a lettuce')
                updateState(False, app2, False, numberPhoto)
        time.sleep(5)
        print("Hola de nuevo")

thread = threading.Thread(target=fiveSeconds)
thread.start()
