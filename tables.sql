-- Description: Create tables for the Playtest database
-- The database follows the star schema, with the fact table being the Sessions table.

CREATE TABLE IF NOT EXISTS Players (
    playerId INT NOT NULL AUTO_INCREMENT,
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
    gameId INT NOT NULL AUTO_INCREMENT,
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
    gameSetupId INT NOT NULL AUTO_INCREMENT,
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
    sessionID INT NOT NULL AUTO_INCREMENT,
    sessionStart DATETIME,
    sessionStart DATETIME,
    locationType VARCHAR(255),
    gameId INT,
    gameSetupId INT,
    playerId INT,
    recordingPath VARCHAR(255),
    eventsLogsPath VARCHAR(255),
    systemLogsPath VARCHAR(255),
    surveyPath VARCHAR(255),
    comments VARCHAR(255),

    PRIMARY KEY (SessionID),
    FOREIGN KEY (gameId) REFERENCES Games(gameId),
    FOREIGN KEY (gameSetupId) REFERENCES GameSetups(gameSetupId),
    FOREIGN KEY (playerId) REFERENCES Players(playerId)
);