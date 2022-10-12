/*
James Berger
CS257
Olympics data assingment
*/

/* creates olympian table*/
CREATE TABLE athletes (
  id INTEGER,
  name TEXT,
  sex TEXT,
  age TEXT,
  height TEXT,
  weight TEXT
);


CREATE TABLE events (
  id INTEGER,
  name TEXT,
  sport TEXT
);




CREATE TABLE games (
  id INTEGER,
  name TEXT
);


CREATE TABLE olympics_info(
  id INTEGER,
  year TEXT,
  season TEXT,
  city TEXT
);

CREATE TABLE noc_regions(
  id INTEGER,
  noc TEXT,
  region TEXT,
  notes TEXT
);

CREATE TABLE event_results (
  athlete_id INTEGER,
  event_id INTEGER,
  team_id INTEGER,
  game_id INTEGER,
  olympic_id INTEGER,
  noc_id INTEGER,
  medal TEXT
);

