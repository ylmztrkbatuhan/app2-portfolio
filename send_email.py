import smtplib,ssl

host = "smtp.gmail.com"
port = 465

username = "write your email"
password = "write your email code that you take for app"

receiver="same emil adress"
context = ssl.create_default_context()
message = """\
Subject: hi!!
how are you?
bye!"""

with smtplib.SMTP_SSL(host, port, context=context ) as server:
    server.login(username, password)
    server.sendmail(username,receiver, message)