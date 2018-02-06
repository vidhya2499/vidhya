import smtplib
server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("vidhyabidrakote2@gmail.com","nagaraju9")
msg = "hi!"
server.sendmail("vidhyabidrakote2@gmail.com","swathi1213@gmail.com", hi)
server.quit()
