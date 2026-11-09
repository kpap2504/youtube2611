import sqlite3
import pandas as pd

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect('youtube_videos_26_11.db')
cursor = conn.cursor()

# Read the CSV file into a DataFrame
df = pd.read_csv('Output/youtube-2026-10-29.csv')

# Insert the data into the SQLite database
for index, row in df.iterrows():
    cursor.execute('''
        INSERT OR IGNORE INTO videos (video_id, title, author, duration, views)
        VALUES (?, ?, ?, ?, ?)
    ''', (row['video_id'], row['title'], row['author'], row['duration'], row['views']))

    # cursor.execute(
    #     "INSERT OR IGNORE INTO videos (original_url, video_id) VALUES (?, ?)",
    #     (url, video_id)
    # )

conn.commit()
conn.close()
