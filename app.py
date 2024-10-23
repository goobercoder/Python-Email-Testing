import smtplib
from keys import *
email = "goberbott@gmail.com"
reciever = input("RECIEVER EMAIL: ")

title = input("EMAIL TITLE: ")
message = input("EMAIL MESSAGE: ")

text = f"Subject: {title}n\n\{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, GMAILKEY)

server.sendmail(email, reciever, text)

print("email has been sent to: " + reciever)