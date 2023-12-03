# Game Playtest Data Management Project (work in progress)

## What?

This project revolves around efficiently managing and organizing game playtest data generated during user sessions, leveraging Azure Cloud services to handle both structured and unstructured data effectively.

## Why?

As a game developer, playtests are a pivotal part of our journey. They offer an invaluable peek into players' experiences with our creations, but they also present a formidable challenge in managing the data deluge they generate.

### Taming the Data Tsunami

Playtest sessions churn out staggering amounts of unstructured data, particularly in the form of gameplay recordings. If you ever took part in a playtest session organized by a large studio, you know that it usually comes down to exactly that - **they record you playing their game**. Even with a moderate group of 20 playtesters, each gaming for 8 hours a day, it results in 160 hours of gameplay footage. Automatically associating recordings with the right session and tying them to detailed player feedback is crucial. Establishing clear connections between sessions, player data, and gameplay footage is pivotal for us to glean meaningful insights.

Believe me, ***I've seen triple A studios manually extracting*** data from their playtest devices. This is not a solved problem yet.

### The Diversity of Data Streams

Beyond the gameplay recordings, playtest sessions yield various semi-structured data like system logs, event logs, and performance metrics. Centralizing these alongside the gameplay recordings within Azure Blob Storage offers us a comprehensive repository, potentially beneficial for deeper analysis and insights. The goal of our final SQL database is not to actually store everything, as it is to act as a central knowlege hub, organizing our blob storage.

## How?

### Overview

![img](https://github.com/MichalMSlusarski/Playtest-data-processing/blob/b366a196fb7bb0c477984fdf0376ce50ab6216e5/overview.png)

### The components

**1. Playtest Session Manager
2. Blob Storage
3. Data Factory
4. Azure SQL database
5. Access point**

### Scenario

In this example scenario the Playtest session generates the following data:
- user credentials string [user.txt]
- player info [player.json]
- post-gameplay form [form.json]
- hardware data [hardware.json]
- gameplay setup data [setup.json]
- event logs [events.csv]
- system logs [system.csv]


