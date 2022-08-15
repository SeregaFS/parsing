import sqlite3 as sq


db = sqlite3.connect('server.db')
sq = db.cursor()

sq.execute("""CREAT TABLE IF NOT EXISTS users(
login TEXT,
password TEXT,
cash BIGIN)""")

db.commit()
user_login = input('Login')
user_password = input('Password: ')

sq.execute("SELECT Login FROM users")
if sq.fetchone() is None:
    pass
else:
    print('ЕСТЬ УЖЕ')
