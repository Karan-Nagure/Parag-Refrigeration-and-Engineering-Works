import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp@gmail.com', 587)
# start TLS for security
s.starttls()

# Email setup
sender_email = 'nagurekaran77@gmail.com'
sender_password = 'Pass@472004K'

recipient_email = "harshalmali5557@gmail.com"
    

# Authentication
s.login(sender_email, sender_password)
# message to be sent
message = "Customer Details"
# sending the mail
s.sendmail(sender_email, recipient_email, message)
# terminating the session
s.quit()