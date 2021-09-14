import cv2
import random
import time
import dropbox

starttime = time.time()

def takeimage():
    number=random.randint(1,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        h="photo" +str( number) + ".jpg"
        cv2.imwrite(h,frame)
        result = False
    return h
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "sl.A4I_0lpsErpNSw-K9hUJGGqaSnNaRRJMRqUPDtlKwYelG6GLakJrlbMALn7iNwUVQD93tdFY221ys7Co17ex8pBhPkajLsdxupAiSUn5NOfwkKyb796fycv8IIaWGMvub7jbVtH6VP0"
    file =img_name
    file_from = file
    file_to="/empty_folder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

while(True):
    if((time.time()-starttime)>5):
        d=takeimage()
        upload_file(d)