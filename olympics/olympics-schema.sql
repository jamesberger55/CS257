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

\copy events FROM 'events.csv' DELIMITER ',' CSV NULL as 'NULL';
\copy games FROM 'games.csv' DELIMITER ',' CSV NULL as 'NULL';
\copy event_results FROM 'event_results.csv' DELIMITER ',' CSV NULL as 'NULL';
\copy noc_regions FROM 'noc_data.csv' DELIMITER ',' CSV NULL as 'NULL';
\copy athletes FROM 'athletes.csv' DELIMITER ',' CSV NULL as 'NULL';
\copy olympics_info FROM 'olympics_info.csv' DELIMITER ',' CSV NULL as 'NULL';