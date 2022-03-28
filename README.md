# MC Server Scraper
A simple script to filter Minecraft servers by their current online players.

## How it works
Basically, this script will make a request to the Minecraft-MP website (changing pages) and then it will check those servers with the mcsrvstatus API using some threading to make it faster.

## Why this script?
This script could be useful for Minecraft griefers, so as said before, this filters servers by their connected players.
Also (but uncommon) it could be used if you're searching a server to play-in with your friends but don't know where to join lmao.

## Installation & Configuration
***This script was written with Python 3.9.9***
```
pip install -r requirements.txt
```
```
PAGES = 5 => This is the max pages that the script will request for Minecraft-MP website.
MIN_PLAYERS = 50 => Here are the minimum required players to validate the requested server.
```
