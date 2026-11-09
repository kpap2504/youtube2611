import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect('youtube_videos_26_11.db')
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video_id TEXT NOT NULL UNIQUE,
        title TEXT NOT NULL,
        author TEXT,
        duration INTEGER,
        views INTEGER
    )
''')
conn.commit()
conn.close()

