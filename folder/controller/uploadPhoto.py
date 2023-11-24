import firebase_admin
from firebase_admin import credentials, storage

def uploadPhoto(localImagePath, remoteImagePath, app):
    bucket = storage.bucket(app=app)
    # Sube la imagen al bucket de Firebase Storage
    blob = bucket.blob(remoteImagePath)
    blob.upload_from_filename(localImagePath)

    print(f"Imagen subida exitosamente a {remoteImagePath}")
