from multiprocessing.connection import Connection
import sqlite3
import pytest
from borrowers import get_borowers_by_return_date

@pytest.fixture
def create_connection():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE borrowed(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            name TEXT,
            book_title TEXT,
            return_at DATE)''')

    sample_data = [
        (1, 'kacper@rmail.pl', 'Kacper', 'Pan Samochodzik', '2020-11-12'),
        (2, 'martyna@email.pl', 'Martyna', 'W Pustyni i w puszczy', '2021-10-13'),
        (3, 'mateusz@email.com', 'Mateusz', 'Cyberiada', '2019-03-04')
    ]

    cursor.executemany('INSERT INTO borrowed VALUES(?,?,?,?)', sample_data)
    return connection

def test_borowers(create_connection):
    borowers = get_borowers_by_return_date(create_connection, '2020-11-12')
    assert len(borowers) == 2
    assert borowers[0].name == 'Kacper'
    assert borowers[1].name == 'Mateusz'
