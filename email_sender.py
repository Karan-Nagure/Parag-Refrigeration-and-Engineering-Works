import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Database connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Karan@12345',
    database='Form_Details'
)

try:
    with connection.cursor() as cursor:
        # Example SQL query to fetch data
        query = "SELECT * FROM form;"
        cursor.execute(query)
        result = cursor.fetchall()
finally:
    connection.close()

# Email setup
sender_email = 'nagurekaran77@gmail.com'
sender_password = 'Pass@472004'

# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587

recipient_email = "harshalmali5557@gmail.com"

# Create the email
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Customer Details'

# Send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(result)

# # Sending emails
# for row in result:
#     # recipient_email = row[0]  # Assuming the first column is the email
#     # name = row[1]
#     # message_content = row[2]

#     # Create the email
#     message = MIMEMultipart()
#     message['From'] = sender_email
#     message['To'] = recipient_email
#     message['Subject'] = 'Customer Details'

#     # Create the body of the message
#     body = f"{row}"
#     message.attach(MIMEText(body, 'plain'))


    

print(f'Email sent to {recipient_email}')

