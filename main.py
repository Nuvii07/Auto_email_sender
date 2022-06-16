import email
from os import getenv
from multiprocessing import context
import sqlite3
from string import Template
from dotenv import load_dotenv
from borrowers import get_borowers_by_return_date
from database import Database
from emails import EmailSender, Credentials


load_dotenv()
connection = sqlite3.connect('database.db')

ssl_enable = getenv('SSL_ENABLE', False)
port = getenv('PORT')
smtp_server = getenv('SMTP_SERVER')
username = getenv('MAIL_USERNAME')
password = getenv('MAIL_PASSWORD')

subject = getenv('SUBJECT')
sender = getenv('SENDER')

credentials = Credentials(username, password)


def setup(connection):
    with Database(connection) as database:
        database.cursor.execute('''CREATE TABLE borrowed(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            name TEXT,
            book_title TEXT,
            return_at DATE)''')

def send_reminder_to_borower(borower):
    template = Template('''Hej $name!
    Masz moją książkę do oddania $book_title
    Data zwrotu mineła $return_at
    ''')

    text = template.substitute({
        'name': borower.name,
        'title': borower.book_title,
        'book_return_at': borower.return_at
    })

    message = email.message_from_string(text)

    message.set_charset('utf-8')
    message['From'] = sender
    message['To'] = borower.email
    message['Subject'] = 'Oddaj mi ksiazke'
    connection.sendmail(sender, borower.email, message)

    print(f'Wysylam email do {borower.email}')


if __name__ == '__main__':
    borowers = get_borowers_by_return_date(connection, '2024-12-24')

    with EmailSender(port, smtp_server, credentials) as connection:
        for borower in borowers:
            send_reminder_to_borower(borower)
