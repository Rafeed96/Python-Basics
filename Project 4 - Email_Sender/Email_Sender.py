from email.message import EmailMessage
from app2 import password


email_sender = "ribrahim173095@bscse.uiu.ac.bd"
email_password = password

email_receiver = ""

subject = "Trial of email sender"
body = "Lets see if this works or not "


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
