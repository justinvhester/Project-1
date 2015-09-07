import fresh_tomatoes
import media

# Several instances of the class Movie defining Title, synopsis, movie poster URL, and trailer URL
# added a sixth value to each for the MPAA rating
the_avengers= media.Movie("The Avengers",
    "Marvel's greatest heroes come together to watch the Incredible Hulk smash.",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://youtu.be/NPoHPNeU9fc",
    "PG-13")

aliens = media.Movie("Aliens",
    "A team of rough and tumble marines go on a bug hunt.",
    "https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg",
    "https://youtu.be/zNE0dlHcmgA",
    "R")

tropic_thunder = media.Movie("Tropic Thunder",
    "Fictional frame war epic starring Nick Nolte and Tom Cruise.",
    "https://upload.wikimedia.org/wikipedia/en/d/d6/Tropic_thunder_ver3.jpg",
    "https://youtu.be/T-6YhRZowgc",
    "R")

guardians_galaxy = media.Movie("Guardians of the Galaxy",
    "A story about the power of true love between a circle of friends.",
    "http://ia.media-imdb.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_SX640_SY720_.jpg",
    "https://youtu.be/d96cjJhvlMA",
    "PG-13")

brave = media.Movie("Brave",
    "Epic set in (probably) Ireland about a daughter learning the importance of a mother's wisdom.",
    "https://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg",
    "https://youtu.be/TEHWDA_6e3M",
    "G")

big_hero_six = media.Movie("Big Hero Six",
    "A story about a boy and his robot. Tears guaranteed.",
    "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
    "https://youtu.be/z3biFxZIJOQ",
    "G")

# Build a list of the movies defined higher in the file.
movies = [the_avengers, aliens, tropic_thunder, guardians_galaxy, brave, big_hero_six]
# Call the open_movies_page method from the fresh tomatoes module on the movies list.
fresh_tomatoes.open_movies_page(movies)
