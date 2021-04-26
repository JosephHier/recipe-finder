import sqlite3

conn = sqlite3.connect('video.db')

c = conn.cursor()

c.execute("""CREATE TABLE videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            apple  REAL NOT NULL DEFAULT 0.0,
            lemon  REAL NOT NULL DEFAULT 0.0,
            mango  REAL NOT NULL DEFAULT 0.0,
            onion  REAL NOT NULL DEFAULT 0.0,
            orange REAL NOT NULL DEFAULT 0.0,
            tomato REAL NOT NULL DEFAULT 0.0,
            type TEXT,
            title TEXT NOT NULL,
            yt_link TEXT,
            filename TEXT NOT NULL
            )""")

conn.commit()
conn.close()
