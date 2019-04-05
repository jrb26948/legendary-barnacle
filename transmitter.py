#Transmits live video over UDP with JPEG compression
import numpy as np
import cv2
import socket

#Set IP and Port
IP = ""
PORT = 5005

#Initialize webcam with capture resolution
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

#Initialize frame count
framecounter = 0

#Loop the Transmission 
while(True):

    #Return good capture frames and display them
    ret, frame = cap.read()
    cv2.imshow('Transmitting', frame)

    #Encode each frame as a JPEG
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    result, encimg = cv2.imencode('.jpg', frame, encode_param)

    #Create length packet
    l = len(encimg)
    l = str.encode(str(l).zfill(5))

    #Specify UDP as protocol
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #Send length packet
    sock.sendto((l),(IP,PORT))

    #Send JPEG and count frames sent
    sock.sendto((encimg),(IP, PORT))
    framecounter+=1
    print("Frames sent: ", framecounter)

    #End when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release capture and close display
cap.release()
cv2.destroyAllWindows()
