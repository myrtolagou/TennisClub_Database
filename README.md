# Tennis Club Database Management System
 
A relational database application built with Python and SQLite for managing a tennis club's operations, developed as part of the "Databases" course at the University of Patras, December 2022.
 
## Overview
 
This system handles the full operational data of a tennis club, including member management, coach scheduling, court reservations, equipment rentals, and tournament tracking.
 
## Features
 
- **Member & Coach Management:** Add, update, and delete member and coach records
- **Court Reservations:** Book courts with time conflict detection and operating hours validation
- **Equipment Rental:** Track racket and ball rentals per session
- **Tournament Management:** Manage singles and doubles tournaments, track match results and winners
- **Analytical Queries:** 8 built-in queries including:
  - Training sessions per coach per month
  - Match schedule
  - Available coaches and courts by date/time
  - Average match duration per tournament winner
  - Individual vs. group training sessions per member
    
## Tech Stack
 
- **Python:** Application logic and CLI interface
- **SQLite:** Relational database engine
- **SQL:** Queries with JOINs, window functions, aggregations, and date filtering

## Project Structure
 
```
├── TennisClub_Sql.py     # Database schema creation
├── TennisClub_Data.py    # Data population
├── TennisClub_Queries.py # Analytical queries (CLI)
├── TennisClub_Main.py    # Main menu: insert, update, delete operations
└── TennisClub.db         # SQLite database (auto-generated)
```
 
## How to Run
 
```bash
python TennisClub_Main.py
```
 
The script will automatically create the database and load the data on first run.
 
## Database Schema
 
9 tables with full referential integrity (foreign keys, cascade rules, unique constraints):
 
`Member`, `Coach`, `Court`, `Reserves`, `Equipment`, `Rents`, `Player`, `Team`, `Participates`, `Tournament`, `SignsUp`, `Game`
