import sqlite3


conn = sqlite3.connect('mydata.db')
sql = "CREATE TABLE fastfud (name TEXT, price TXT, text TXT, url_img TXT)"
sql = "SELECT * FROM fastfud"

cursor = conn.cursor()
cursor.execute(sql)
res = cursor.fetchall()

for r in res:
    print(r)
conn.close()

# db.commit()
#
# user_login = input('login')
# user_pasword = input('pasword')
#
# sql.execute("SELECT login FROM users")
# if sql.fetchone() is None:
#     sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_pasword, 0))
# else:
#     print('Такая запись уже существует')
#
#     for value in sql.execute("SELECT * FROM users"):
#         print(value)
#
#
#
#
#
#
#
#
#




# with sqlite3.connect('db_database.db') as db:
#     cursor = db.cursor()
#     query1 = """ TNSERT INTO expenses (id, name) VALIES(1, 'name') """
#     query2 = """ TNSERT INTO expenses (id, name) VALIES(2, 'price') """
#     query3 = """ TNSERT INTO expenses (id, name) VALIES(3, 'text') """
#     query4 = """ TNSERT INTO expenses (id, name) VALIES(4, 'url_img') """
#     # cursor.execute(query1)
#     # cursor.execute(query2)
#     # cursor.execute(query3)
#     # cursor.execute(query4)
#     # db.commit()