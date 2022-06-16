import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 465
sender_email = "matkop666@gmail.com"
password = "Fksmks07@"

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, sender_email, 'Pisze z replit')

    """from os import environ, getenv
from dotenv import load_dotenv

load_dotenv()

print('FIRST_NAME', getenv('FIRST_NAME'))
print('LAST_NAME', getenv('LAST_NAME'))
print('EMAIL', getenv('EMAIL'))
    """