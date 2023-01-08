import sqlite3;
conn= sqlite3.connect("TennisClub.db");

conn.execute('''CREATE TABLE Member  
       (id_member integer NOT NULL,
	first_name varchar,
	last_name varchar,
	birthdate date, 
	identity_number varchar,
	phone_number integer,
	address varchar,
	gender varchar,
	PRIMARY KEY (id_member),
	FOREIGN KEY (id_member) REFERENCES Player(id_player)
	ON DELETE CASCADE ON UPDATE CASCADE);''')  


conn.execute('''CREATE TABLE Coach
       (id_coach integer,
	first_name varchar,
	last_name varchar,
	phone_number integer,
	birthdate date,
	PRIMARY KEY (id_coach));''')


conn.execute('''CREATE TABLE Court
       (court_number integer NOT NULL,
	court_type varchar,
	PRIMARY KEY (court_number));''')  


conn.execute('''CREATE TABLE Reserves
       (id_member integer,
        id_coach integer,
        court_number integer,
        reservation_date date,
        start_time time,
        ending_time time,
        number_of_members integer,
        PRIMARY KEY (id_member,id_coach,court_number,reservation_date),
        FOREIGN KEY (id_member) REFERENCES Member(id_member)
        ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (id_coach) REFERENCES coach(id_coach)
        ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (court_number) REFERENCES Court(court_number)
        ON DELETE CASCADE ON UPDATE CASCADE,
        UNIQUE (reservation_date,start_time,ending_time,court_number),
        UNIQUE (reservation_date,start_time,ending_time,id_coach),
        CONSTRAINT opening_time_check CHECK(start_time >= TIME ('09:00:00')),
        CONSTRAINT closing_time_check CHECK(start_time <= TIME ('21:00:00'))
        );''')

 
conn.execute('''CREATE TABLE Equipment
       (id_eq integer NOT NULL,
	equipment_type varchar,
	PRIMARY KEY (id_eq));''') 


conn.execute('''CREATE TABLE Rents
        (id_member integer,
         id_racket integer,
         id_balls integer,
         reservation_date date,   
         start_time time,
         ending_time time,
         PRIMARY KEY (id_member,id_racket,id_balls,reservation_date),
         FOREIGN KEY (id_member) REFERENCES Member(id_member)
         ON DELETE CASCADE ON UPDATE CASCADE,
         FOREIGN KEY (id_racket) REFERENCES Equipment(id_eq)
         ON DELETE CASCADE ON UPDATE CASCADE,
         FOREIGN KEY (id_balls) REFERENCES Equipment(id_eq)
         ON DELETE CASCADE ON UPDATE CASCADE,
         UNIQUE (reservation_date,start_time,ending_time,id_racket),
         UNIQUE (reservation_date,start_time,ending_time,id_balls),
         CONSTRAINT opening_time_check CHECK(start_time >= TIME ('09:00:00')),
         CONSTRAINT closing_time_check CHECK(start_time <= TIME ('21:00:00'))
         );''')


conn.execute('''CREATE TABLE Player
       (id_player integer NOT NULL,
	PRIMARY KEY (id_player));''');


conn.execute('''CREATE TABLE Team
       (id_team integer NOT NULL,
        team_name varchar,
        PRIMARY KEY(id_team),
        FOREIGN KEY (id_team) REFERENCES Player(id_player)
        ON DELETE CASCADE ON UPDATE CASCADE);''');  


conn.execute('''CREATE TABLE Participates
       (id_team integer,
        id_member integer,
        PRIMARY KEY(id_team,id_member),
        FOREIGN KEY(id_team) REFERENCES  Team(id_team)
        ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY(id_member) REFERENCES  Member(id_member)
        ON DELETE CASCADE ON UPDATE CASCADE);''')


conn.execute('''CREATE TABLE Tournament
       (tournament_name varchar NOT NULL,
        category varchar,
        start_date date,
        ending_date date,
        participants integer,
        prize varchar,
        winner_female integer,
        winner_male integer,
        PRIMARY KEY(tournament_name),
        FOREIGN KEY(winner_female) REFERENCES  Player(id_player)
        ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY(winner_male) REFERENCES  Player(id_player)
        ON DELETE CASCADE ON UPDATE CASCADE);''')


conn.execute('''CREATE TABLE SignsUp
        (id_player integer,
         tournament_name varchar,
         PRIMARY KEY(id_player,tournament_name),
         FOREIGN KEY (tournament_name) REFERENCES Tournament(tournament_name)
         ON DELETE CASCADE ON UPDATE CASCADE,
         FOREIGN KEY (id_player) REFERENCES Player(id_player)
         ON DELETE CASCADE ON UPDATE CASCADE);''')


conn.execute('''CREATE TABLE Game
       (id_match integer NOT NULL,
	tournament_name varchar,
	home_id integer,
	away_id integer,
	court_number integer,
	gamedate date,
	start_time datetime,
	ending_time datetime,
	final_score varchar,
	winner_id integer,
	PRIMARY KEY (id_match),
	FOREIGN KEY (tournament_name) REFERENCES Tournament(tournament_name)
	ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (home_id) REFERENCES Player(id_player)
	ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (away_id) REFERENCES Player(id_player)
	ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (court_number) REFERENCES Court(court_number)
	ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (winner_id) REFERENCES Player(id_player)
	ON DELETE CASCADE ON UPDATE CASCADE,
	UNIQUE (court_number,gamedate,start_time,ending_time)
	CONSTRAINT opening_time_check CHECK(start_time >= TIME ('09:00:00')),
        CONSTRAINT closing_time_check CHECK(start_time <= TIME ('20 :00:00'))
        );''')


conn.close();
