import webbrowser


# This class creates movie objects which will be rendered in the website.
class Movie():
    """ This class create movie objects having some details about it. """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # This is a constructor which allocates some memory for it's objects.
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Open default web browser and goto provided YouTube URL
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
