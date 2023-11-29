# Game Playtest Data Management Project

## Overview

This project aims to streamline the collection, storage, and organization of game playtest data generated during user sessions. It utilizes Azure Cloud services to manage and transform the data into structured formats for analysis and further insights.

## How it Works?

As a playtester engages with the game, the system orchestrates a sequence of events to capture, organize, and transform the generated data:

1. Session Initialization

When the playtester initiates the game, it triggers the start of a session dedicated to the ongoing gameplay experience. Immediately upon the initiation of a session, an automated process is triggered through an in-game script, connected to Azure. This function swiftly creates a dedicated directory within Azure Blob Storage. This directory bears the session ID as its unique identifier, providing a container for the upcoming data influx.

3. Data Capture and Storage

Throughout the course of the session, an array of data points emerges, which are stored on device until the session ends. These metrics encompass diverse elements like gameplay recordings, player forms, session events, logs detailing errors or warnings, and real-time performance. Each of these data components is saved in their raw, original formats. Once the session ends, these raw files find their designated repository within the session's directory, securely nestled within Azure Blob Storage.

4. Daily Data Transformation

At the culmination of each day, a meticulously scheduled routine springs into action within Azure Data Factory. This orchestrated sequence calls upon a Python script that meticulously combs through the session directories. Its mission is to extract the amassed data and mold it into structured formats, often employing CSV as a preferred choice. Once the transformation is complete, the refined data finds its way into pre-defined tables within Azure SQL Database. Here, it is cataloged and organized, poised for deep analytical scrutiny and strategic insights.

[[img]](https://github.com/MichalMSlusarski/Playtest-data-processing/blob/c1062aa860ce9343def93acdebcb7b638623b32d/process_simplified.png)

### Features

- Automatic creation of session directories in Azure Blob Storage.
- Capture and storage of session data in their original form (e.g., gameplay recordings, player forms, session events, logs).
- Daily data transformation process using Azure Data Factory to organize and load data into defined SQL tables.
- Utilization of Python scripts within Azure Data Factory for data extraction and transformation.

