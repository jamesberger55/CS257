/*
James Berger
CS257
Olympics data assingment
*/

/* creates olympian table*/
olympics=# CREATE TABLE olympian (
  id INTEGER,
  name TEXT
);

/* creates event table*/
olympics=# CREATE TABLE event (
  id INTEGER,
  name TEXT
);

/* creates country/team table*/
olympics=# CREATE TABLE country (
  id INTEGER,
  name TEXT
);

/* creates info about specific olympic games table*/
olympics=# CREATE TABLE olympics_info(
  id INTEGER,
  year TEXT,
  season TEXT,
  city TEXT
);

/* creates games table*/
olympics=# CREATE TABLE games (
  id INTEGER,
  name TEXT
);

/* creates teh NOC table */
olympics=# CREATE TABLE noc_regions(
  id INTEGER,
  noc TEXT,
  region TEXT,
  notes TEXT
);

/* Links all the tables */
olympics=# CREATE TABLE event_results (
  athlete_id INTEGER,
  event_id INTEGER,
  team_id INTEGER,
  game_id INTEGER,
  olympic_id INTEGER,
  noc_id INTEGER,
  medal TEXT
);

