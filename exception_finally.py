import sqlite3

conn = sqlite3.connect('wombats.db')
cur = conn.cursor()

try:
    cur.execute('select foo from bar where blah')
except sqlite3.Error as err:
    print(err)
    quit()
else:
    print(cur.fetchall())
finally:
    conn.close()

print("continuing...")