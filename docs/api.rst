Scoutify API
==============

Some or All information protected under a proprietary license: `Located Here <proprietary.html>`_.

- API Version: *version*
- Status: *status*
- Current Season: *currentSeason*
- Max Season: *maxSeason*

API Keys
---------

.. note::
    The following section provides a basic overview. For detailed URI routes, refer to the documentation.

- **TheBlueAlliance**: Any request to The Blue Alliance from this API requires data to be in their format.
- **StatBotics**: Any request to StatBotic from this API requires data to be in their format.

User Levels
~~~~~~~~~~~

- **Super Admin**: Level 1 // Super Admin API Key (Usually for internal use only)
- **Admin**: Level 2 // Admin API Key
- **Team Lead**: Level 3 // Team Lead API Key
- **Team**: Level 4 // Student API Key and/or Account ID Connection

Key Operations
~~~~~~~~~~~~~~

- **postONLY**: Creates data and posts it to the API (Requires Admin/Team API Key and/or Account login)
- **put**: Updates data in the API (Requires Admin/Team API Key and/or Account login)
- **getONLY**: Gets data from the API (Requires Admin/Team API Key and/or Account login)
- **postGet**: Creates data and gets data from the API (Requires Admin/Team API Key and/or Account login)

Routes
------

.. note::
    Do not use "/routes/" in the URI. An example of a valid URI route would be "/api/events/2024nyro".

- **login**: Logs in the user
- **logout**: Logs out the user
- **register**: Registers a new user (Requires Admin/Team Lead API Key)
- **predictions**: "/predictions" route has more information on how to use it

User
~~~~

- **get**: Gets user info
- **put**: Updates user info (Requires Super Admin API Key)
- **delete**: Deletes user (Requires Super Admin API Key)

Events
~~~~~~

- **get**: Gets all events
- **post**: Creates a new event (Requires Admin API Key)

Scouting
~~~~~~~~

- **get**: Gets all scouting data
- **post**: Creates new scouting data (Requires Admin/Team API Key and/or Account login)
- **put**: Updates scouting data (Requires Admin/Team API Key and/or Account login)
- **delete**: Deletes scouting data (Requires Admin/Team API Key and/or Account login)
- **getEvent**: Gets all scouting data for a specific event
- **getTeam**: Gets all scouting data for a specific team
- **getMatch**: Gets all scouting data for a specific match

2024
~~~~

- **eventCode**: In TBA format (YYYY + event code) (Ex: 2024nyro)
- **teamNumber**: Team Number
- **matchNumber**: Match Number

Auto
~~~~

- **leftStartingZoneAuto**: Left Starting Zone in Auto
- **AMPScoredAuto**: Amp Scored in Auto
- **speakerScoredAuto**: Speaker Scored in Auto

Teleop
~~~~~~

- **AMPScoredTeleop**: Amp Scored in Teleop
- **speakerScoredTeleop**: Speaker Scored in Teleop

Endgame
~~~~~~~~

- **park**: Parked in Endgame
- **harmony**: Harmony in alliance in Endgame
- **soloClimb**: Solo Climb in Endgame
- **neither**: Neither in Endgame // Alliance member did not climb
- **scoredTrap**: Scored in Trap (true or false)

Defense
~~~~~~~

- **playedDefense**: Played Defense
- **defenseRating**: Defense Rating

Other
~~~~~

- **feedOtherBots**: Fed other bots
- **comments**: Additional Comments
