import smtplib
from keys import *
email = "goberbott@gmail.com"
reciever = input("RECIEVER EMAIL: ")

title = "EMAIL SENT THROUGH GOOBERBOT ON DISCORD"
message = input("EMAIL MESSAGE: ")

text = f"Subject: {title}\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, GMAILKEY)

server.sendmail(email, reciever, text)

print("email has been sent to: " + reciever)