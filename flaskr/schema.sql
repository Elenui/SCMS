DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS websites;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE websites (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  web_url TEXT NOT NULL
);