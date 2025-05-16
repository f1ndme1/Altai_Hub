import sqlite3

def connect_db():
    return sqlite3.connect('bot.db')

def init_db():
    with connect_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS user_rooms (
                user_id INTEGER PRIMARY KEY,
                room TEXT
            )
        ''')
        conn.commit()

def join_room(user_id: int, room: str):
    with connect_db() as conn:
        conn.execute('REPLACE INTO user_rooms (user_id, room) VALUES (?, ?)', (user_id, room))
        conn.commit()

def leave_room(user_id: int):
    with connect_db() as conn:
        conn.execute('DELETE FROM user_rooms WHERE user_id=?', (user_id,))
        conn.commit()

def get_user_room(user_id: int):
    with connect_db() as conn:
        result = conn.execute('SELECT room FROM user_rooms WHERE user_id=?', (user_id,)).fetchone()
        return result[0] if result else None

def get_users_in_room(room: str):
    with connect_db() as conn:
        rows = conn.execute('SELECT user_id FROM user_rooms WHERE room=?', (room,)).fetchall()
        return [row[0] for row in rows]
