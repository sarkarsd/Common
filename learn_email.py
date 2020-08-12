# Edit Configurations >> emulate terminal in console (due to getpass problems)[<< IN PYCHARM >>]
from email.message import EmailMessage
import os
import mimetypes
import smtplib
import getpass

sender = "sarkarsd19@gmail.com"
receiver = "sarkarsd18@gmail.com"
body = "Yo! I am superman trying to send emails"

# generating EmailMessage object and setting up the basic configuration of the email object
message = EmailMessage()
message['From'] = sender
message['To'] = receiver
message['Subject'] = "Check"
message.set_content(body)
print(message)

image_path = 'E:\\PycharmProjects\\automation-python-capstone\\week3\\Myphoto.jpg'

# taking the filename from the path using os.path.basename()
filename = os.path.basename(image_path)
mime_type, _ = mimetypes.guess_type(filename)  # for checking the MIME TYPE example(image/png, image/jpeg etc.)
print(mime_type)
main_type, sub_type = mime_type.split('/', 1)  # separating the image(type) and jpeg/png(sub-type)

with open(image_path, 'rb') as f:  # 'rb' for byte read mode
    message.add_attachment(f.read(),
                           maintype=main_type,
                           subtype=sub_type,
                           filename='myself')
f.close()
print(message)
sender_pass = getpass.getpass("Password:")  # for getting the password from the user without being visible
mail_server = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
mail_server.starttls()  # enable security
mail_server.login(sender, sender_pass)  # login with mail_id and password
print('connection made...')
mail_server.send_message(message)  # loop can used here for sending as many emails as wanted
mail_server.quit()
print('Mail Sent')
