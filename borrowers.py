from collections import namedtuple
from database import Database

Entity = namedtuple('Entity', 'name email book_title return_at')

def get_borowers_by_return_date(connection, return_at):
    entities = []
    with Database(connection) as database:
        database.cursor.execute('''SELECT
            name,
            email, 
            book_title,
            return_at
        FROM borrowed 
        WHERE return_at < ?''', (return_at,))

        for name, email, book_title, return_at in database.cursor.fetchall():
            entities.append(Entity(name, email, book_title, return_at))
    
    return entities
