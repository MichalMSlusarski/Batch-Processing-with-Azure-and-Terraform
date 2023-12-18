-- Description: Create tables for the Playtest database
-- The database follows the star schema, with the fact table being the Sessions table.

CREATE TABLE Users (
    userId VARCHAR(20) NOT NULL,
    username VARCHAR(64),
    secretPath VARCHAR(64),
    email VARCHAR(64),
    country VARCHAR(64),
    city VARCHAR(64),
    paymentInfoPath VARCHAR(64),    
    consentBasic BOOLEAN,
    consentAnalytics BOOLEAN,
    consentCampaings BOOLEAN,
    firstName VARCHAR(64),
    lastName VARCHAR(64),
    isActive BOOLEAN,
    subscriptionType VARCHAR(64),
    subscriptionStartDate DATETIME,
    subscriptionEndDate DATETIME,

    PRIMARY KEY (userId)
);

CREATE TABLE Players (
    playerId VARCHAR(20) NOT NULL,
    gender VARCHAR(64),
    age INT,
    playstyle VARCHAR(64), -- This is the player's self-reported player type, e.g. "casual", "hardcore", "explorer", "achiever", etc.
    weeklyHours INT, -- This is the player's self-reported weekly hours of gaming
    experienceYears INT, -- This is the player's self-reported years of gaming experience
    isLeftHanded BOOLEAN, 
    needsGlasses BOOLEAN, 
    needsInputAdaptation BOOLEAN, 
    isColorBlind BOOLEAN, 
    isHearingImpaired BOOLEAN, 
    isAutistic BOOLEAN, 
    isAttentionDeficient BOOLEAN,

    PRIMARY KEY (playerId)
);

CREATE TABLE Games (
    gameId VARCHAR(20) NOT NULL,
    gameName VARCHAR(64), -- This is the game's name, e.g. "Overwatch", "League of Legends", "Fortnite", etc.
    genre VARCHAR(64), -- This is the game's genre, e.g. "FPS", "RPG", "RTS", etc.
    subgenre VARCHAR(64), -- This is the game's subgenre, e.g. "MMO", "MOBA", "Battle Royale", etc.
    isSinglePlayer BOOLEAN,
    isDevelopmentBuild BOOLEAN,
    gameVersion VARCHAR(64),
    gameBuildVersion VARCHAR(64),
    gameBuildDate DATETIME,

    PRIMARY KEY (gameId)
);

CREATE TABLE Setups (
    gameSetupId VARCHAR(20) NOT NULL,
    gameSetupName VARCHAR(64),
    gameSetupDescription VARCHAR(64),
    gameResolutionWidth INT,
    gameResolutionHeight INT,
    gameResolutionRefreshRate INT,
    gameDifficulty VARCHAR(64),
    isResolutionFullscreen BOOLEAN,
    isStandardInputSetup BOOLEAN, -- Was the input device set to mouse and keyboard?
    isKeybindingsSetup BOOLEAN, -- Were the keybindings set to the default?
    isSubtitles BOOLEAN, -- Were the subtitles enabled?
    isAudioDescription BOOLEAN, -- Was the audio description enabled?
    isStandardGraphicsSetup BOOLEAN, -- Were the graphics set to the default?

    PRIMARY KEY (gameSetupId)
);

CREATE TABLE Sessions (
    sessionID VARCHAR(20) NOT NULL,,
    sessionStart DATETIME,
    sessionStart DATETIME,
    locationType VARCHAR(64),
    ownerId INT, -- This is the userId that owns the session and can modify data
    gameId INT,
    gameSetupId INT,
    playerId INT,
    recordingPath VARCHAR(64),
    eventsLogsPath VARCHAR(64),
    systemLogsPath VARCHAR(64),
    othersPath VARCHAR(64), -- path to 'others.txt' listing other files that are part of the session
    comments VARCHAR(64),

    PRIMARY KEY (SessionID),

    FOREIGN KEY (ownerId) REFERENCES Players(playerId),
    FOREIGN KEY (gameId) REFERENCES Games(gameId),
    FOREIGN KEY (gameSetupId) REFERENCES GameSetups(gameSetupId),
    FOREIGN KEY (playerId) REFERENCES Players(playerId)
);