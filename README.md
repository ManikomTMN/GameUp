
# Gameup

this tool allows you to store games locally and download them

# How To Use

First, install python and flask if they aren't already.

Put all your game folders in a folder, then put the folder's full path in the LOCATION.txt.

Every game's folder should have this structure:
- a .ZIP file containing the game content
- a file called INFO.txt where the first line is the game's name and the 2nd line is the game's description
- a THUMBNAIL.png

Then, run the app using python app.py, and you'll be able to access your library on other PC's by entering your host's IP address : 5000.