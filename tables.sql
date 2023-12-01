-- Description: Create tables for the Playtest database
-- The database follows the star schema, with the fact table being the Sessions table.

CREATE TABLE IF NOT EXISTS Users (
    userId VARCHAR(20) NOT NULL,,
    username VARCHAR(255),
    secretPath VARCHAR(255),
    email VARCHAR(255),
    country VARCHAR(255),
    city VARCHAR(255),
    paymentInfoPath VARCHAR(255),    
    consentBasic BOOLEAN,
    consentAnalytics BOOLEAN,
    consentCampaings BOOLEAN,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    isActive BOOLEAN,
    subscriptionType VARCHAR(255),
    subscriptionStartDate DATETIME,
    subscriptionEndDate DATETIME,

    PRIMARY KEY (userId)
);

CREATE TABLE IF NOT EXISTS Players (
    playerId VARCHAR(20) NOT NULL,,
    gender VARCHAR(255),
    age INT,
    playstyle VARCHAR(255), -- This is the player's self-reported player type, e.g. "casual", "hardcore", "explorer", "achiever", etc.
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

CREATE TABLE IF NOT EXISTS Games (
    gameId VARCHAR(20) NOT NULL,,
    gameName VARCHAR(255), -- This is the game's name, e.g. "Overwatch", "League of Legends", "Fortnite", etc.
    genre VARCHAR(255), -- This is the game's genre, e.g. "FPS", "RPG", "RTS", etc.
    subgenre VARCHAR(255), -- This is the game's subgenre, e.g. "MMO", "MOBA", "Battle Royale", etc.
    isSinglePlayer BOOLEAN,
    isDevelopmentBuild BOOLEAN,
    gameVersion VARCHAR(255),
    gameBuildVersion VARCHAR(255),
    gameBuildDate DATETIME,

    PRIMARY KEY (gameId)
);

CREATE TABLE IF NOT EXISTS Setups (
    gameSetupId VARCHAR(20) NOT NULL,,
    gameSetupName VARCHAR(255),
    gameSetupDescription VARCHAR(255),
    gameResolutionWidth INT,
    gameResolutionHeight INT,
    gameResolutionRefreshRate INT,
    gameDifficulty VARCHAR(255),
    isResolutionFullscreen BOOLEAN,
    isStandardInputSetup BOOLEAN, -- Was the input device set to mouse and keyboard?
    isKeybindingsSetup BOOLEAN, -- Were the keybindings set to the default?
    isSubtitles BOOLEAN, -- Were the subtitles enabled?
    isAudioDescription BOOLEAN, -- Was the audio description enabled?
    isStandardGraphicsSetup BOOLEAN, -- Were the graphics set to the default?

    PRIMARY KEY (gameSetupId),
);

CREATE TABLE IF NOT EXISTS Sessions (
    sessionID VARCHAR(20) NOT NULL,,
    sessionStart DATETIME,
    sessionStart DATETIME,
    locationType VARCHAR(255),
    ownerId INT,
    gameId INT,
    gameSetupId INT,
    playerId INT,
    recordingPath VARCHAR(255),
    eventsLogsPath VARCHAR(255),
    systemLogsPath VARCHAR(255),
    surveyPath VARCHAR(255),
    comments VARCHAR(255),

    PRIMARY KEY (SessionID),

    FOREIGN KEY (ownerId) REFERENCES Players(playerId),
    FOREIGN KEY (gameId) REFERENCES Games(gameId),
    FOREIGN KEY (gameSetupId) REFERENCES GameSetups(gameSetupId),
    FOREIGN KEY (playerId) REFERENCES Players(playerId)
);