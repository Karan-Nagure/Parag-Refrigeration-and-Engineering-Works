import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd = "Karan@12345",
    database = "Form_Details"
	)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE form_details")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
# 	print(db)

# USE users;
# my_cursor.execute("ALTER TABLE users ADD (name VARCHAR(30), email VARCHAR(30), message VARCHAR(30)) ");


# query = "SELECT * FROM form;"
# df = pd.read_sql(query, mydb)


# csv_content = df.to_csv(index=False)

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# message = MIMEMultipart()
# message['Subject'] = "Customer Details"
# message['From'] = "nagurekaran77@gmail.com"
# message['To'] = "harshvardhanl7804@gmail.com"

# part = MIMEText(csv_content, "csv")
# message.attach(part)

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
# server.login("nagurekaran77@gmail.com", "Pass@472004")
# server.sendmail("nagurekaran77@gmail.com", "harshvardhanl7804@gmail.com", message.as_string())
# server.quit()