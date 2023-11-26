import firebase_admin
from firebase_admin import credentials, storage

def downloadPhoto(downloadFile, app):
    bucket = storage.bucket(app=app)

    # Obtener una referencia al archivo en el bucket
    refFile = bucket.blob(downloadFile)

    # Descargar el archivo a la ruta local especificada
    refFile.download_to_filename("/Users/ritchie928/Desktop/firebaseLocobot/photos/lettuce.jpg")

    print(f"El archivo ha sido descargado a: /Users/ritchie928/Desktop/firebaseLocobot/photos")
