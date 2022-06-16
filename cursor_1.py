import sqlite3


def create_connection():
    with sqlite3.connect('baza.db') as connection:
        cursor = connection.cursor()
        #print(cursor.fetchall())
        return cursor

def get_book(cursor):
    cursor.execute('SELECT * FROM books WHERE author=?', ('Henryk Sienkiewicz',))
    data = []

    for id, title, author, created_at in cursor.fetchall():
        data.append({
            'book_id': id,
            'title': title,
            'author': author,
            'created_at': created_at
        })

    return data
        
if __name__ == "__main__":
    cursor = create_connection()
    book = get_book(cursor)
    print(book)
