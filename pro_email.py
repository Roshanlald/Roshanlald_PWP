#email
import smtplib
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("roshanlalabde17@gmail.com", "*********")
message = "hello"
s.sendmail("roshanlalabde17@gmail.com", "pravesh368@gmail.com", message)
print("ss")
s.quit()
