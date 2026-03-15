import sqlite3

conn = sqlite3.connect("reviews.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS reviews(
restaurant TEXT,
food TEXT,
cost INTEGER,
rating INTEGER,
review TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")