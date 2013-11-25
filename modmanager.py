#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Copyright 2013 Matthew Krohn
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random
from urllib2 import urlopen
from json import load

versions = ["0.15", "0.16", "0.17", "0.18", "0.19", "1.0"]
version = random.choice(versions)

print "Welcome to the FLARE Mods Manager!"
print "You are running FLARE Version", version
print "(Version number set randomly for demonstration)"

done = False
modUrl = ""

while done == False:
    print "Which of the following mods would you like to install?"
    print " (1) Flare Alpha Demo"
    print " (2) Flare Beta Empyrean Campaign"
    print " (3) Wandercall"
    print " (4) Polymorphable"
    print " (5) Valley of Concordia"
    print " (6) Other"
    print " (exit) Exit Manager"
    modChoice = raw_input("Please choose one: ")
    if modChoice == "exit":
        break
    try:
        modChoice = int(modChoice)
        if modChoice == 1:
            modUrl = "https://github.com/clintbellanger/flare-game.git"
        if modChoice == 2:
            modUrl = "https://github.com/clintbellanger/flare-game.git"
            print "Branch:  Empyrean"
        if modChoice == 3:
            modUrl = "https://github.com/clintbellanger/wandercall.git"
        if modChoice == 4:
            modUrl = "https://github.com/makrohn/polymorphable.git"
        if modChoice == 5:
            modUrl = "https://github.com/makrohn/concordia.git"
        if modChoice == 6:
            modUrl = raw_input("Please type a GitHub repository of mod you'd like to install: ")
            if "http" not in modUrl:
                print "Valid URLs must be either http or https."
            else:
                print modUrl
    except:
        print "Invalid Option"
    if modUrl != "":
        apiUrl = modUrl.replace(".git", "")
        apiUrl = apiUrl.replace("github.com", "api.github.com/repos")
        print apiUrl
        tags = load(urlopen(apiUrl + "/tags"))
        versionFound = False
        for tagdata in tags:
            if version in tagdata['name'] and versionFound == False:
                versionFound = True
                download = ""
                while download != "Y" or "N":
                    download = raw_input("Version of mod matches your game version.  Download?")
                    if download == "Y":
                        print "Downloading!"
                        break
                    if download == "N":
                        print "Okay!"
                        break
        if versionFound == False:
            download = ""
            while download != "Y" or "N":
                download = raw_input("Matching version not found.  Download latest?")
                if download == "Y":
                    print "Downloading!"
                    break
                if download == "N":
                    print "Okay!"
                    break
    modUrl = ""
