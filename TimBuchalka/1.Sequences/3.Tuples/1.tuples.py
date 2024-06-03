albums = [('Welcome to my Nightmare', "Allice Cooper", 1975),
           ("Bad Company", "Bad Company", 1974),
           ("Nightflight", "Budgie", 1981),
           ("More Mayhem", "Emilda May", 2011),
           ("Ride the Lightning", "Metallica", 1984),
           ]

for album in albums:
    print("\"{}\" was published by \"{}\" in the year {}".format(album[0], album[1], album[2]))
print()

# UNPACKING THE TUPLE
albums = [('Welcome to my Nightmare', "Allice Cooper", 1975),
           ("Bad Company", "Bad Company", 1974),
           ("Nightflight", "Budgie", 1981),
           ("More Mayhem", "Emilda May", 2011),
           ("Ride the Lightning", "Metallica", 1984),
           ]

for albumname, artist, year in albums:
    print("\'{}\' was published by \'{}\' in the year {}".format(albumname, artist, year))