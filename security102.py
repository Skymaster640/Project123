import  cv2
import dropbox
import time 
import random
starttime = time.time()

def takesnapshot():
    number=random.randint(0,100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        imagename = 'img'+str(number)+'.png'
        cv2.imwrite(imagename,frame)
        starttime=time.time
        result=False
        
    return imagename 
    print('snapshottaken')
    videocaptureobject.release()
    cv2.destroyAllWindows()
    
def uploadfile(imagename):
    accesstoken = 'sl.A_LS7MBusf80Zu5lwvgtFjpGIhT1UzxDsj8NbNjMg-bSW0_pcGgFP4U0qKY2c0HWlPlq3AV7rGz2yFs_MqiSS9Ir0o4E5fYusC5tFpFjnSSGlRqGrX0d11iAfa5GKY3B2L8hcn8'
    file=imagename
    filefrom = file
    fileto = '/folder/Dropbox'
    dbx = dropbox.Dropbox(accesstoken)
    with open(filefrom,'rb')as f:
        dbx.files_uplaod(f.read(),fileto,mode = dropbox.files.Writemode.overwrite)
        print('fileuploaded')
        
def main():
    while(True):
        if((time.time()-starttime)>=50):
            name = takesnapshot()
            uploadfile(name)
            
main()