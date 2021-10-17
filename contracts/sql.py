from . import db
from . import cursor
def save_to_db(order, city):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Orders'")
    if not cursor.fetchall():
        cursor.execute("CREATE TABLE Orders (id int, city varchar(255) )")
        print('Created table for Orders')
    cursor.execute(f"SELECT * FROM Orders WHERE id={order}")
    if cursor.fetchall():
        print(f'Already have order {order}. Skipped saving this order.')
        return
    currently_save(order, city)

def currently_save(order, city):
    cursor.execute(f"""
    INSERT INTO Orders (id, city)
    VALUES(?, ?);
    """, (order, city))
    db.commit()
def search(order: str = None, city: str = None):
    if order:
        cursor.execute(f"""
        SELECT city FROM Orders WHERE id={order}
        """)
        return cursor.fetchall()[0][0]
    elif city:
        cursor.execute(f"""
        SELECT id FROM Orders WHERE city=?
        """, (city,))
        return cursor.fetchall()

def save_json(json_):
    """

    :param json_: Json
    :type json_: Looks like:
    {
    "<order num>": "<city>",
    "<order num>": "<city>",
    "<order num>": "<city>",
    ...
    }
    :return:
    :rtype:
    """
    for order, city in json_.items():
        save_to_db(order, city)
def drop(table='Orders'):
    cursor.execute(f"DROP TABLE {table}")
    db.commit()