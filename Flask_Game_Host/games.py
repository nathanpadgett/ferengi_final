'''
Dictionary storing information about games offered on the site

Each key '<game>' is the same as its route string and stores:

    gameDict<game>[0]: Title of game
    gameDict<game>[1]: Name of game's image file
    gameDict<game>[2]: Short description of the game
    gameDict<game>[3]: URL of game's source repository

'''
gameDict = {

            'pinball': ['Pinball',
                        'pinball.png',
                        'Classic pinball',
                        'https://github.com/corehtml5canvas/code/tree/master/ch09/pinball'
                        ],
            '2048' : ['2048',
                      '2048.png',
                      'Classic 2048',
                      'https://github.com/gabrielecirulli/2048'
	                 ],
            'chess': ['Chess',
                            'Chess.jpg',
                            'Chess',
                            'https://cdn.htmlgames.com/Chess/'
                            ],

            'daily-sudoku': ['Daily-Sudoku',
                            'dailysudoku.jpg',
                            'Daily Sudoku',
                            'https://cdn.htmlgames.com/DailySudoku/'
                            ],

            '1010-classic': ['1010-Classic',
                            '1010classic.jpg',
                            '1010 Classic',
                            'https://cdn.htmlgames.com/1010Classic/'
                            ],

            'coloring-mandalas': ['Coloring-Mandalas',
                            'coloring-mandalas.jpg',
                            'Coloring Mandalas',
                            'https://cdn.htmlgames.com/ColoringMandalas/'
                            ],

            'archery-tour': ['Archery',
                            'ArcheryWorldTour.jpg',
                            'Archery World Tour',
                            'https://play.famobi.com/archery-world-tour'
                            ],

            'bowling': ['Bowling',
                            'bowling.jpg',
                            'Bowling',
                            'https://cdn.htmlgames.com/Bowling/'
                            ],
            
            'table-tennis': ['Table-Tennis',
                            'TableTennis.jpg',
                            'Table Tennis World Tour',
                            'https://play.famobi.com/table-tennis-world-tour'
                            ],

            'checkers': ['Checkers',
                            'CheckersClassic.jpg',
                            'Checkers',
                            'https://cdn.htmlgames.com/Checkers/'
                            ],

            'mahjongg': ['Mahjongg',
                            'mahjongg.jpg',
                            'Mahjongg',
                            'https://cdn.htmlgames.com/Mahjongg/'
                            ],

            'ninja-darts': ['Ninja-Darts',
                            'ninjadarts.jpg',
                            'Ninja Darts',
                            'https://cdn.htmlgames.com/NinjaDarts/'
                            ]
            }