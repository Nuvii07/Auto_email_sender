import pytest
from random import sample
from cursor_1 import get_book
import sqlite3


@pytest.fixture
def create_data_base():
    conn = sqlite3.connect(':memory:')
    cursor =  conn.cursor()
    cursor.execute('''
        CREATE TABLE books
        (id integer, title text, author text, created_at data)''')
    sample_data = [
        (1, 'Pan samochodzik', 'Zbigniew Nienacki', '2020-01-03 20:21:23'),
        (1, 'Dzienniki Gwiazdkowe', 'Stanisław Lem', '2022-02-04 21:22:24'),
        (1, 'W Pustyni i w puszczy', 'Henryk Sienkiewicz', '2021-10-12 10:15:30')
    ]
    cursor.executemany('INSERT INTO books VALUES(?, ?, ?, ?)', sample_data)
    return cursor

def test_get_book(create_data_base):
    cursor = create_data_base
    data = get_book(cursor)
    assert data[0] == {'book_id': 1, 'title': 'W Pustyni i w puszczy', 'author': 'Henryk Sienkiewicz', 'created_at': '2021-10-12 10:15:30'}
