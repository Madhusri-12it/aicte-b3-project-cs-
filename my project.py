import cv2
import os
import string
import datetime
from art import text2art
stylish_text = text2art("*my project*")
print(stylish_text)
img = cv2.imread("Balloon.png")
print("hidding text in an image")
msg = input("Enter secert message")
password = input("Enter password")
d={}
c={}
for i in range(255):
    d[chr(i)]=i
    c[i] = chr(i)
m=0
n=0
z=0
for i in range(len(msg)):
    img[n,m,z] = d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3
cv2.imwrite("Encryptedmsg.jpg",img)
os.system("start Encryptedmsg.jpg")
message =""
n=0
m=0
z=0
print("Message is Encrypted")
pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1) % 3
    print("Decryption message : ",message)
else:
    print("the key is not valid")
print("\n")
current_time = datetime.datetime.now()
print("the encrytion and decryption done at :")
print("\n")
print("Year :", current_time.year)
print("Month : ", current_time.month)
print("Day : ", current_time.day)
formatted_time = current_time.strftime("%I:%M %p")
print("time :", formatted_time)







