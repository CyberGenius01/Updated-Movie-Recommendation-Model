import json

default_movies = [[211672, 'Minions', 'tt2293640', 'https://m.media-amazon.com/images/M/MV5BMTUwNjcxNzAwOF5BMl5BanBnXkFtZTgwNzEzMzIzNDE@._V1_SX300.jpg'], 
                  [366142, 'Minions: The Competition', 'tt5223342', 'https://m.media-amazon.com/images/M/MV5BZmViZTYxYzYtYzAyYi00NTY2LTkxNWItZjRiNzE4MDE3MmRjXkEyXkFqcGdeQXVyNjA3OTI5MjA@._V1_SX300.jpg'], 
                  [93456, 'Despicable Me 2', 'tt1690953', 'https://m.media-amazon.com/images/M/MV5BMTQxNzY1MjI5NF5BMl5BanBnXkFtZTcwNTI0MDY1OQ@@._V1_SX300.jpg'], 
                  [817, 'Austin Powers: The Spy Who Shagged Me', 'tt0145660', 'https://m.media-amazon.com/images/M/MV5BMmFkZGQxN2YtODNlYS00MzM5LTk3NjQtNTUxYmQ1YzkwMDhmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg'], 
                  [19585, 'G-Force', 'tt0436339', 'https://m.media-amazon.com/images/M/MV5BMTM4NTY3MzY2MV5BMl5BanBnXkFtZTcwMDQ1NTM2Mg@@._V1_SX300.jpg'], 
                  [14248, 'Igor', 'tt0465502', 'https://m.media-amazon.com/images/M/MV5BMTY2OTMzMjQ3Ml5BMl5BanBnXkFtZTcwNDUxMTE3MQ@@._V1_SX300.jpg'], 
                  [89325, 'Darling Companion', 'tt1730687', 'https://m.media-amazon.com/images/M/MV5BMjA5NTQ3MDExMl5BMl5BanBnXkFtZTcwNjU1MTc2Nw@@._V1_SX300.jpg'], 
                  [18162, 'Land of the Lost', 'tt0457400', 'https://m.media-amazon.com/images/M/MV5BOTkzNDg2OTc1NF5BMl5BanBnXkFtZTcwNDcxODE2Mg@@._V1_SX300.jpg'], 
                  [9928, 'Robots', 'tt0358082', 'https://m.media-amazon.com/images/M/MV5BNDYyNjY1NjY1M15BMl5BanBnXkFtZTcwNjk5MDczMw@@._V1_SX300.jpg'], 
                  [9070, 'Mighty Morphin Power Rangers: The Movie', 'tt0113820', 'https://m.media-amazon.com/images/M/MV5BN2I2Y2I5N2MtMzJhMy00NzE2LThlMzEtNGE0ODA4M2JhOWNiXkEyXkFqcGdeQXVyNTI4MjkwNjA@._V1_SX300.jpg'], 
                  [11052, 'YAgiA Dyueru MonsutAzu Hikari no Piramiddo', 'tt0403703', 'https://m.media-amazon.com/images/M/MV5BNTQ4NzM0NTAyMF5BMl5BanBnXkFtZTYwOTc2MTg3._V1_SX300.jpg'], 
                  [13908, 'The Master of Disguise', 'tt0295427', 'https://m.media-amazon.com/images/M/MV5BODYzNjdmZTgtNzkyZS00NWJjLTlkOGQtZmEzZTI3ZTg2MzNkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg'], 
                  [89874, 'First Position', 'tt2008513', 'https://m.media-amazon.com/images/M/MV5BNDcxMzYyNzI2Ml5BMl5BanBnXkFtZTcwNjAzODg2Nw@@._V1_SX300.jpg'], 
                  [8698, 'The League of Extraordinary Gentlemen', 'tt0311429', 'https://m.media-amazon.com/images/M/MV5BZTFlOTdkMjEtNGVmMS00YTA3LThlNjQtMjAzZmFjZDAzNjllL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg'], 
                  [54013, 'Stridulum', 'tt0080100', 'https://m.media-amazon.com/images/M/MV5BYjk2YWFkY2UtNGNjMy00ODRjLThkMTYtYjFkODM0MDU3ZmJjL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg'], 
                  [17577, "The Devil's Tomb", 'tt1147687', 'https://m.media-amazon.com/images/M/MV5BYTM4N2Y3NWQtMDliMi00YzgzLWFlMmEtZmJhOTI5ZjlkZDY4XkEyXkFqcGdeQXVyMjQwMjk0NjI@._V1_SX300.jpg'], 
                  [328425, 'The Gift', 'tt4178092', 'https://m.media-amazon.com/images/M/MV5BNGFmY2UyMmYtNDY1Yi00NTIwLTk1ZDktOGM2OTQwZDk0NjU5XkEyXkFqcGdeQXVyMjQwMjk0NjI@._V1_SX300.jpg'], 
                  [50374, 'Black Sunday', 'tt0075765', 'https://m.media-amazon.com/images/M/MV5BMDIzMWNlMDEtNDllYi00YmZlLWE2ZGQtMTJlMDgyZDY2YzM2XkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SX300.jpg'], 
                  [14923, 'Run Ronnie Run', 'tt0258100', 'https://m.media-amazon.com/images/M/MV5BMTM1MjAxNzEyMV5BMl5BanBnXkFtZTYwMTA5ODE3._V1_SX300.jpg'], 
                  [229405, 'Panic in the Mailroom', 'tt3425332', 'https://m.media-amazon.com/images/M/MV5BZmViMzFlYTUtNTg2OC00YzJhLWFkNTctMTQwZTQ2Mjg1ODQ0XkEyXkFqcGdeQXVyMzE4MDE1Mw@@._V1_SX300.jpg'], 
                  [15258, 'The Aristocrats', 'tt0436078', 'https://m.media-amazon.com/images/M/MV5BZGQ0NmI1N2EtYzdkYy00NzFmLThlYTMtOWViYjQyOGQ2OWVlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg'], 
                  [58574, 'Sherlock Holmes: A Game of Shadows', 'tt1515091', 'https://m.media-amazon.com/images/M/MV5BMTQwMzQ5Njk1MF5BMl5BanBnXkFtZTcwNjIxNzIxNw@@._V1_SX300.jpg'], 
                  [14239, 'Cool World', 'tt0104009', 'https://m.media-amazon.com/images/M/MV5BODg1YWNjNjctOGJiYi00YzRjLWI2ZWYtMTAxZGM5ODY1Yzc4XkEyXkFqcGdeQXVyMTY5Nzc4MDY@._V1_SX300.jpg'], 
                  [17653, 'Fong Sai Yuk', 'tt0106936', 'https://m.media-amazon.com/images/M/MV5BYzU0OTY5NDYtMjJlMC00MzE4LWI4N2EtZjBhOGRhMGNkYzIzXkEyXkFqcGdeQXVyMjQwMjk0NjI@._V1_SX300.jpg']
]

movies = [{
    'id': movie[0],
    'title': movie[1],
    'imdb_id': movie[2],
    'image': movie[3]
} for movie in default_movies]

with open('default-movies.json', 'w') as f:
    json.dump(movies, f, indent=4)