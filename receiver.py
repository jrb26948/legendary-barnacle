#Receives JPEG compressed live video over UDP
import socket
import numpy
import time
import cv2

#Set IP and Port
IP = ""
PORT = 5005

#Initialize frame count
framecounter = 0

#Specify UDP and bind.
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind ((IP, PORT))

#Loop receiving frames
while True:

    #Get length from first packet
    length, addr = sock.recvfrom(5)
    length = int(length.decode())
    
    #Use length to determine frame size
    data, addr = sock.recvfrom(length)
    
    #Turn JPEG string back into image
    frame = numpy.fromstring(data,dtype=numpy.dtype('uint8'))
    frame = cv2.imdecode(frame, -1)
    frame = frame.reshape(240,320,3)
    
    #Display frame
    cv2.imshow('Receiving', frame)
    framecounter+=1
    print("Frames received: ", framecounter)
    
    #End when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break

#Close display
cv2.destroyAllWindows()
