/*
James Berger
CS257
Olympics data assingment
*/

/* creates olympian table*/
CREATE TABLE olympian (
  id INTEGER,
  name TEXT
);

/* creates event table*/
CREATE TABLE event (
  id INTEGER,
  name TEXT
);

/* creates country/team table*/
CREATE TABLE country (
  id INTEGER,
  name TEXT
);

/* creates info about specific olympic games table*/
CREATE TABLE olympics_info(
  id INTEGER,
  year TEXT,
  season TEXT,
  city TEXT
);

/* creates games table*/
CREATE TABLE games (
  id INTEGER,
  name TEXT
);

/* creates teh NOC table */
CREATE TABLE noc_regions(
  id INTEGER,
  noc TEXT,
  region TEXT,
  notes TEXT
);

/* Links all the tables */
CREATE TABLE event_results (
  athlete_id INTEGER,
  event_id INTEGER,
  team_id INTEGER,
  game_id INTEGER,
  olympic_id INTEGER,
  noc_id INTEGER,
  medal TEXT
);
