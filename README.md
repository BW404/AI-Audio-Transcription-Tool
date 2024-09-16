# AI Audio Transcription Tool
=====================================

## Overview
This is a Python script that uses the Groq API to transcribe audio files and save the transcription as a subtitle file.

## Requirements
### Python
* Python 3
### Groq API
* Groq API key (sign up for free at [console.groq.com](http://console.groq.com))

## Setup
### Clone Repository
Clone this repository to your local machine.
### Replace API Key
Replace `YOUR_API_KEY` in the script with your actual Groq API key.
### Install Dependencies
Install the required Python libraries by running `pip install groq`.

## Usage
### Run Script
Run the script using `python main.py`.
### Enter Audio File Path
Enter the path to the audio file you want to transcribe when prompted.
### Output File
The transcription will be saved to a file named `output.str` in the same directory.

## How it Works
### Initialize Groq Client
The script initializes the Groq client using your API key.
### Read Audio File
It reads the audio file and performs transcription using the Groq API.
### Write Transcription
The transcription results are written to a file in subtitle format.

## Example Output
The output file will contain the transcription in the following format:

    1 00:00:00.000 --> 00:00:01.000 Hello world!

    2 00:00:01.000 --> 00:00:02.000 This is a test.


## Troubleshooting
### Check API Key
Make sure you have replaced `YOUR_API_KEY` with your actual Groq API key.
### Check Audio File Path
Ensure that the audio file path is correct and the file is in a format supported by the Groq API.
### Check Groq API Docs
Check the Groq API [documentation](https://console.groq.com/settings/limits)  for any usage limits or restrictions.

## License
This script is released under the MIT License. See [LICENSE.txt](https://github.com/BW404/AI-Audio-Transcription-Tool/blob/main/License.txt) for details.