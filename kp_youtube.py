import sqlite3
import re

# 1. Setup the extraction function
def get_youtube_id(url):
    # Matches the 11-character ID following common YouTube URL structures
    pattern = r'(?:v=|\/shorts\/|\/embed\/|\/v\/|\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None


# 2. Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# 3. Create a table to store the data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT NOT NULL,
        video_id TEXT NOT NULL UNIQUE
    )
''')
conn.commit()

# 4. Extract and Save Data Function
def save_video(url):
    video_id = get_youtube_id(url)
    if video_id:
        cursor.execute(
            "INSERT OR IGNORE INTO videos (original_url, video_id) VALUES (?, ?)",
            (url, video_id)
        )
        conn.commit()
        print(f"Saved: {video_id}")
    else:
        print("Invalid YouTube URL")


file_path = "youtube-2026-08-21.txt"   # Replace with your file path

# Read the file and get a list of video_ids
with open(file_path, 'r') as file:
    video_ids = [(f"https://www.youtube.com/watch?v={get_youtube_id(line.strip())}", get_youtube_id(line.strip())) for line in file.readlines() if line.strip()]

print(f"Total video IDs read from file: {len(video_ids)}")
print(f"Video IDs: {video_ids[:10]}")  # Print the first 10 video IDs for verification

v_id = video_ids[0]  # Get the first video ID for testing
print(f"First video ID: {v_id}")

# 3. Batch insert the collected URLs
if video_ids:
    cursor.executemany(
            "INSERT OR IGNORE INTO videos (original_url, video_id) VALUES (?, ?)", 
            video_ids
    )
    conn.commit()
    print(f"\nSuccessfully processed file. Attempted to insert {len(video_ids)} items.")


# Clean up connection when finished
conn.close()