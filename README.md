MfFlareM
========

Manager for Flare Mods

I wrote a VERY basic and messy Python 2.7 script to demonstrate how I think mods management could work:

https://github.com/makrohn/MfFlareM
(doesn't actually download, some stuff should be moved to their own methods, default options should be stored in a text file and loaded into a dictionary and iterated over, blah blah blah. Really just a demo of how I think the workflow could go that I hacked up in about an hour.)

The GitHub API returns results in JSON, and is pretty easy to parse. By having some pre-selected mods in a .txt file with their github URLs for ease of maintenance (the script translates download urls to api urls on it's own), a program could easily check the installed version of FLARE against the tags, and the offer to download and move the mod to the correct place.

Lastly, I think modders could put a "modsmanager.txt" file into their mod to list dependencies or other info that a player might want to be aware of, and the manager could just display the contents of that mod after installing it.