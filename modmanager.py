print "Welcome to the FLARE Mods Manager!"
done = False
while done == False:
    print "Which of the following mods would you like to install?"
    print " (1) Flare Alpha Demo"
    print " (2) Flare Beta Empyrean Campaign"
    print " (3) Wandercall"
    print " (4) Polymorphable"
    print " (5) Valley of Concordia"
    print " (6) Other"
    modChoice = raw_input("Please choose one: ")
    try:
        modChoice = int(modChoice)
        if modChoice == 1:
            print "https://github.com/clintbellanger/flare-game.git"
        if modChoice == 2:
            print "https://github.com/clintbellanger/flare-game.git"
            print "Branch:  Empyrean"
        if modChoice == 3:
            print "https://github.com/clintbellanger/wandercall.git"
        if modChoice == 4:
            print "https://github.com/makrohn/polymorphable.git"
        if modChoice == 5:
            print "https://github.com/makrohn/concordia.git"
        if modChoice == 6:
            modUrl = raw_input("Please type a GitHub repository of mod you'd like to install: ")
            if "http" not in modUrl:
                print "Valid URLs must be either http or https."
            else:
                print modUrl
        else:
            print "Invalid option"
    except:
        print "Invalid Option"
