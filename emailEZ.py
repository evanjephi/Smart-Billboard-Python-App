import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "ez.ads.noreply@gmail.com"  # Enter your address
receiver_email = "n.drake2045@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi thkkkkere

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, 'Ezadsnoreply3')
    server.sendmail(sender_email, receiver_email, message)
