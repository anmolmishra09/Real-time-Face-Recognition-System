import cv2, time

# load dataset
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# source
cap=cv2.VideoCapture(0)
count=0

while True:
    # reading images
    _,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.1,4)

    # face reading
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)

        cv2.imshow('img',img)
        t=time.strftime("%Y-%m-%d-%H-%M-%S")

        print("Image"+t+"saved")
#       
        # save the file
        file='C:/Users/AARSH SAXENA/Desktop/test_open_cv/pictures/'+t+'.jpg'
        cv2.imwrite(file,img)
        count+=1

    k=cv2.waitKey(30)&0xff
    if k==27:
        break

cap.release()
