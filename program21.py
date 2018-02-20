import smtplib
server=smtplib.SMTP('smtp.gmail.com', 587)
l=["swathik.8685@gmail.com", "vidhyabidrakote2@gmail.com"]
for i in l:
server.starttls()
server.login("vidhyabidrakote2@gmail.com", "chiru243")
msg ="hi!"
server.sendmail("vidhyabidrakote2@gmail.com", l[i], msg)
print("success")
server.quit()
