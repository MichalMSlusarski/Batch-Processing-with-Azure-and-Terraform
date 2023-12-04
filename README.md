# Game Playtest Data Management Project (work in progress)

## What?

This project revolves around efficiently managing and organizing game playtest data generated during user sessions, leveraging Azure Cloud services to handle both structured and unstructured data effectively.

## Why?

In 2009 Mike Ambinder spoke at GDC highlighting Valve's extensive approach to playtesting:

✔️ We want to make informed decisions  
✔️ We don’t know what’s best (players do)    
✔️ We should aim to create a feedback loop between design and playtest  

Valve revolutionized the game development landscape by integrating playtesting as a fundamental part of the design process. They emphasized that it's not just a last-minute tweak for polishing; it's a core element from the very start. This approach was an early showcase of embracing data-driven design, and it turned out to be a massive success.

However, within the realm of game development, establishing standardized playtesting methodologies and a single commonly used software remains a challenge. I've participated in numerous playtesting sessions across different studios, and each one had its own unique approach. Yet, there were underlying similarities.

### Taming the Data Tsunami

Playtest sessions churn out staggering amounts of unstructured data, particularly in the form of gameplay recordings. If you ever took part in a playtest session organized by a large studio, you know that it usually comes down to exactly that - **they record you playing their game**. Even with a moderate group of 20 playtesters, each gaming for 8 hours a day, it results in 160 hours of gameplay footage. Automatically associating recordings with the right session and tying them to detailed player feedback is crucial. Establishing clear connections between sessions, player data, and gameplay footage is pivotal for us to glean meaningful insights.

Believe me, ***I've seen triple A studios manually extracting*** data from their playtest devices. This is not a solved problem yet.

### The Diversity of Data Streams

During playtest sessions, we gather lots of different data like system logs, event logs, and how well the game performs. Centralizing these alongside the gameplay recordings within Azure Blob Storage offers us a comprehensive repository, potentially beneficial for deeper analysis and insights. The goal of our final SQL database is not to actually store everything, as it is to act as a central knowlege hub, organizing our blob storage.

## How?

### Overview

![img](https://github.com/MichalMSlusarski/Playtest-data-processing/blob/b366a196fb7bb0c477984fdf0376ce50ab6216e5/overview.png)

### Components

**1. Playtest Session Manager
2. Blob Storage
3. Data Factory
4. Azure SQL database
5. Access point**

### Scenario

In this example scenario the playtest session generates the following data:
- user info [user.txt]
- player info [player.txt]
- hardware data [hardware.txt]
- gameplay setup data [setup.txt]
- event logs [events.csv]
- system logs [system.csv]
- gameplay footage [recording.mp4]

*In the final app each generated file should be proceeded by the session_id*

#### Upload
The upload.py script helps move playtest session data to Azure Blob Storage (ABS). It looks for the right session folder created by the Playtest Session Manager. Before sending the data, it checks how big the files are and what type they are. If all the files together are larger than 2 GB or if there are some odd types of files, it stops and tells you about the problem. It also checks if the most important files for a database are there. If any of these important files are missing, it asks if it's okay to continue without them. If anything goes wrong while sending the data, it will let you know and stop to keep things safe. The script tries to sort out which files are really important. If the important ones aren't too big, it might upload other files too. It keeps track of these extra files in a file called 'others.txt'. This way, it makes sure to handle the playtest session data carefully and make the important parts safe before doing anything else.

#### Storage
All data is stored as blobs, in Azure Blob Storage. For each session, there's an appropriate container.


