
# Listening Party BOT - README

This bot has been initially created for the Listening Party of Anne-Marie her latest album 'Unhealthy (Deluxe)', but can be used for other servers that are managed by Levellr Ltd.

This README will explain how the bot works and how to install it to be able to use it.

If any questions arise, please feel free to contact me throught Discord (neliglesias) and/or by mail (neliglesiasperez@hotmail.com).
## Installation

This bot has been written in Python and uses Discord.py, FFmpeg and PyNaCl libraries.

First you will have to set up a Discord Bot in the Discord Developer Portal: https://discord.com/developers/applications

#### Creating the environment
Now create bot environment
```bash
  python3 -m venv bot-env
```
Activate virtual environment
- On Windows:
```bash
  bot-env\Scripts\activate.bat
```
- On macOS/Linux:
```bash
  source bot-env/bin/activate
```
#### Installing Discord.py
Install the Discord.py library
```bash
  pip install discord.py
```
#### Installing FFmpeg
Now you have to install FFmpeg. Depening on the OS the bot is being run on, these are the steps you have to take to install FFmpeg:
- Windows:
Download a static build of ffmpeg from the official website: https://ffmpeg.org/download.html#build-windows
Extract the downloaded ZIP file.
Add the path to the extracted ffmpeg folder to your system's PATH environment variable.

- For Linux (Ubuntu/Debian)
Open a terminal and Run the following command to install ffmpeg:
```bash
  sudo apt update
  sudo apt install ffmpeg
```
- For macOS (Homebrew):
Open a terminal.
Run the following command to install ffmpeg using Homebrew:
```bash
  brew install ffmpeg
```
#### Lastly, install PyNaCl
```bash
  pip install pynacl
```

Add bot.py code to the main folder once everytghing is installed properly, don't forget to add your BOT TOKEN in the script and to add/change the text-channel ID in the speaking_now const.

Also add the songs in a map called "Album" and in that map create another map called "Unhealthy" so you can internally store the album mp3 songs in there. These will have to be manually added to the mp3_list that you can find in the code.
## How does the bot work?

#### Prefix of the bot
The bot has a command prefix, which means all commands issued to the bot must start with this prefix. 
```
  !lpb 
```
#### Commands of the bot
Here you can find all the commands of the bot and how they work and what they're supposed to do. Keep in mind that ONLY the moderators can use these commands and not the normal users of the server.
| Parameter | Command     | Description                |
| :-------- | :------- | :------------------------- |
| `join` | `!lpb join` | Allows the bot join the voice channel they are currently in. If the user is not in a voice channel, the bot instructs them to join one first. |
| `leave` | `!lpb leave` | Allows the bot to leave the voice channel it is currently connected to. |
| `publiclist` | `!lpb publiclist` | Displays the new album songlist in the public voice channel. |
| `privatelist` | `!lpb privatelist` | Sends a message in the current channel with the songs that are available in the list and their song ID's. |
| `play` | `!lpb play [Song ID]` | Plays the mp3 file corresponding to the provided song ID in the voice channel. If the song ID is invalid or the bot is not in a voice channel, appropriate messages are sent. |
| `stop` | `!lpb stop` | Stops the currently playing mp3 file in the voice channel. If there is no song playing or the bot is not in a voice channel, appropriate messages are sent. |
| `mute` | `!lpb mute` | Selfmutes the bot. |
| `unmute` | `!lpb unmute` | Unselfmutes the bot. |



## Demo

For a demo, please feel free to send me a message on Discord (neliglesias), I will gladly give you a demo of how the bot works. Currently do not have a bot/server where it is running 24/7.
## Authors

- [@neliglesias](https://www.github.com/neliglesias)


## License

[CC0](https://choosealicense.com/licenses/cc0-1.0/)

