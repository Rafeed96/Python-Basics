import smtplib as s

ob =s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("raicobd@gmail.com","tenyasha")
subject="test python"
body="I love myself, my computer and python"
message = "subject:{}\n\n{}".format(subject,body)


emaiList = ["rafeed.ibrahim@gmail.com","ribrahim173095@bscse.uiu.ac.bd"]

ob.sendmail("")