albums = [
    ('Welcome to my Nightmare', "Allice Cooper", 1975,
    [
        (1, 'Welcome to my Nightmare'),
        (2, 'Devil\'s Food'),
        (3, 'The Black Widow'),
        (4, 'Only Women Bleed')
    ]
    ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, 'Can\'t Get Enogh'),
         (2, 'Rock Steady'),
         (3, 'Ready For Love'),
         (4, 'Don\'t Let Me Down'),
         (5, 'Bad Company'),
         (6, 'The Way I Choose'),
         (7, 'Seagull')
     ]),
     ("Nightflight", "Budgie", 1981,
      [
        (1, 'I Turned to Stone'),
        (2, 'Keeping a Rendezvous'),
        (3, 'Reaper of The Glory'),
        (4, 'She used Me Up')  
      ]
      ),
      ("More Mayhem", "Emilda May", 2011,
       [
           (1, 'Pulling The Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')
       ]
      ),
]

for name, artist, year, song in albums:
    print("Album Name: {}, Artist: {}, Year: {}, Songs: {}".format(name, artist, year, song))

album = albums[2]
print(f'Album: {album}')

songs = album[3]
print(f'Songs: {song}')

song = songs[1][1]
print(f'Song without index: {song}')

mayhem = albums[3][3][2][1]
print(f'Mayhem Song Name: {mayhem}')

budgie = albums[2][3][1][1]
print(f'Budgie Song Name: {budgie}')