-- Description: Create tables for the Playtest database
-- The database follows the star schema, with the fact table being the Sessions table.

CREATE TABLE IF NOT EXISTS Sessions (
    sessionID INT NOT NULL AUTO_INCREMENT,
    sessionStart DATETIME NOT NULL,
    sessionStart DATETIME NOT NULL,
    locationType VARCHAR(255) NOT NULL,
    gameId VARCHAR(255) NOT NULL,
    gameBuildId VARCHAR(255) NOT NULL,
    gameSetupId VARCHAR(255) NOT NULL,
    playerId INT NOT NULL,
    recordingPath VARCHAR(255) NOT NULL,
    playerLogsPath VARCHAR(255) NOT NULL,
    systemLogsPath VARCHAR(255) NOT NULL,
    surveyPath VARCHAR(255) NOT NULL,
    comments VARCHAR(255) NOT NULL,
    PRIMARY KEY (SessionID)
);

CREATE TABLE IF NOT EXISTS Players (
    playerId INT NOT NULL AUTO_INCREMENT,
    gender VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    playstyle VARCHAR(255) NOT NULL, -- This is the player's self-reported player type, e.g. "casual", "hardcore", "explorer", "achiever", etc.
    weeklyHours INT NOT NULL, -- This is the player's self-reported weekly hours of gaming
    experienceYears INT NOT NULL, -- This is the player's self-reported years of gaming experience
    isLeftHanded BOOLEAN NOT NULL, -- This is the player's self-reported handedness
    needsGlasses BOOLEAN NOT NULL, -- This is the player's self-reported need for glasses
    needsInputAdaptation BOOLEAN NOT NULL, -- This is the player's self-reported need for input adaptation
    isColorBlind BOOLEAN NOT NULL, -- This is the player's self-reported color blindness
    isHearingImpaired BOOLEAN NOT NULL, -- This is the player's self-reported hearing impairment
    isAutistic BOOLEAN NOT NULL, -- This is the player's self-reported autism
    isAttentionDeficient BOOLEAN NOT NULL, -- This is the player's self-reported attention deficit

    PRIMARY KEY (playerId)
);

CREATE TABLE IF NOT EXISTS GameBuilds (
    gameBuildId INT NOT NULL AUTO_INCREMENT,
    gameName VARCHAR(255) NOT NULL,
    gameVersion VARCHAR(255) NOT NULL,
    gameBuildVersion VARCHAR(255) NOT NULL,
    gameBuildDate DATETIME NOT NULL,
    gameBuildPath VARCHAR(255) NOT NULL,
    PRIMARY KEY (gameBuildId)
);

CREATE TABLE IF NOT EXISTS GameSetups (
    gameSetupId INT NOT NULL AUTO_INCREMENT,
    gameBuildId INT NOT NULL,
    gameSetupName VARCHAR(255) NOT NULL,
    gameSetupDescription VARCHAR(255) NOT NULL,
    gameResolutionWidth INT NOT NULL,
    gameResolutionHeight INT NOT NULL,
    gameResolutionRefreshRate INT NOT NULL,
    gameResolutionFullscreen BOOLEAN NOT NULL,
    isStandardInputSetup BOOLEAN NOT NULL, -- Was the input device set to mouse and keyboard?
    isKeybindingsSetup BOOLEAN NOT NULL, -- Were the keybindings set to the default?
    isStandardResolutionSetup BOOLEAN NOT NULL, -- Was the monitor set to 1920x1080?
    isStandardAudioSetup BOOLEAN NOT NULL, -- Was the audio set to 100% volume?
    isStandardGraphicsSetup BOOLEAN NOT NULL, -- Were the graphics set to the default?
    isStandardGameplaySetup BOOLEAN NOT NULL, -- Was the gameplay set to the default?
    isStandardDifficultySetup BOOLEAN NOT NULL, -- Was the difficulty set to the default?
    PRIMARY KEY (gameSetupId),
    FOREIGN KEY (gameBuildId) REFERENCES GameBuilds(gameBuildId)
);