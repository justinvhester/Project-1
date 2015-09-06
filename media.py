import webbrowser
# define a Movie class which contains all the characteristics 
class Movie():
    """ This class provides a way to store movie related information.

    Passing the class five arguments will generate an instance of the
    movie with these five attributes;
     - Movie Title
     - A brief synopsis of the storyline
     - a URL to an image of the movie poster
     - a URL to the the movies trailer on Youtube
     - The MPAA film rating
    """
    # class dictionary defining mpaa ratings as keys set to an image URL
    MPAA_RATING_IMGS = {
        "G": "https://upload.wikimedia.org/wikipedia/commons/0/05/RATED_G.svg",
        "PG": "https://upload.wikimedia.org/wikipedia/commons/b/bc/RATED_PG.svg",
        "PG-13": "https://upload.wikimedia.org/wikipedia/commons/c/c0/RATED_PG-13.svg",
        "R": "https://upload.wikimedia.org/wikipedia/commons/7/7e/RATED_R.svg"
    }
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, film_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        # Validate film_rating value against keys in the MPAA_RATING_IMGS class dict
        if film_rating in self.MPAA_RATING_IMGS.keys():
            # if the value is valid, set self.film_rating to the URL value
            self.film_rating = self.MPAA_RATING_IMGS[film_rating]
        else:
            # if not, use a not available image
            self.film_rating = "https://upload.wikimedia.org/wikipedia/commons/e/e7/Not-available.svg"
