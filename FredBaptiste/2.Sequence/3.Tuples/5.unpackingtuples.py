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
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1


while True:
    print("Please chosse your album. Invalid choice exists: ")
    # for index, value in enumerate(albums):
    #     title, artist, year, song = value
    #     print("{}: {}, {}, {}, {}".format(index + 1, title, artist, year, song))
    # break
    for index, (title, artist, year, song) in enumerate(albums):
        print("{}: {}".format(index + 1, title))
    choice = int(input())
    # if 1 <= choice <= len(albums):
    if choice >= 1 and choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break
    print("Please chooce your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if choice >= 1 and choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Now Playing: {}".format(title))
    # else:
    #     break
    # print("Now Playing: {}".format(title))
    print("=" * 40)