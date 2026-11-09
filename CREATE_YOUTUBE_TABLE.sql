CREATE TABLE IF NOT EXISTS  videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    author TEXT,
    duration INTEGER,
    views INTEGER
)


