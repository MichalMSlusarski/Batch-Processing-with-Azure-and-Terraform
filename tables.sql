CREATE TABLE Users (
    userId VARCHAR(20) NOT NULL,
    username VARCHAR(64),
    secretPath VARCHAR(64),
    email VARCHAR(64),
    country VARCHAR(64),
    city VARCHAR(64),
    paymentInfoPath VARCHAR(64),    
    consentBasic BIT,
    consentAnalytics BIT,
    consentCampaings BIT,
    firstName VARCHAR(64),
    lastName VARCHAR(64),
    isActive BIT,
    subscriptionType VARCHAR(64),
    subscriptionStartDate DATETIME2,
    subscriptionEndDate DATETIME2,

    PRIMARY KEY (userId)
);

CREATE TABLE Players (
    playerId VARCHAR(20) NOT NULL,
    gender VARCHAR(64),
    age INT,
    playstyle VARCHAR(64),
    weeklyHours INT,
    experienceYears INT,
    isLeftHanded BIT, 
    needsGlasses BIT, 
    needsInputAdaptation BIT, 
    isColorBlind BIT, 
    isHearingImpaired BIT, 
    isAutistic BIT, 
    isAttentionDeficient BIT,

    PRIMARY KEY (playerId)
);

CREATE TABLE Games (
    gameId VARCHAR(20) NOT NULL,
    gameName VARCHAR(64),
    genre VARCHAR(64),
    subgenre VARCHAR(64),
    isSinglePlayer BIT,
    isDevelopmentBuild BIT,
    gameVersion VARCHAR(64),
    gameBuildVersion VARCHAR(64),
    gameBuildDate DATETIME2,

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
    isResolutionFullscreen BIT,
    isStandardInputSetup BIT,
    isKeybindingsSetup BIT,
    isSubtitles BIT,
    isAudioDescription BIT,
    isStandardGraphicsSetup BIT,

    PRIMARY KEY (gameSetupId)
);

CREATE TABLE Sessions (
    sessionID VARCHAR(20) NOT NULL,
    sessionStart DATETIME2,
    sessionEnd DATETIME2,
    locationType VARCHAR(64),
    ownerId VARCHAR(20),
    gameId VARCHAR(20),
    gameSetupId VARCHAR(20),
    playerId VARCHAR(20),
    recordingPath VARCHAR(64),
    eventsLogsPath VARCHAR(64),
    systemLogsPath VARCHAR(64),
    othersPath VARCHAR(64),
    comments VARCHAR(64),

    PRIMARY KEY (sessionID),

    FOREIGN KEY (ownerId) REFERENCES Players(playerId),
    FOREIGN KEY (gameId) REFERENCES Games(gameId),
    FOREIGN KEY (gameSetupId) REFERENCES Setups(gameSetupId),
    FOREIGN KEY (playerId) REFERENCES Players(playerId)
);

CREATE TABLE Permissions (
    userId VARCHAR(20) NOT NULL,
    sessioId VARCHAR(20) NOT NULL,
    permissionType VARCHAR(64),
)