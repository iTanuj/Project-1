import media
import fresh_tomatoes

# Creating instances of class Movie
toy_story = media.Movie('Toy Story',
                      'A story about a kid and his toys which have come to life.',
                      'http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg',
                      'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie("Avatar",
                   "A marine on an alien planet",
                   "http://cdn1.ntv.com.tr/gorsel/sanat/en-iyi-20-film-posteri/en-iyi-20-film-posteri,YE55TJyxTEyzw02DeH4beQ.jpg?mode=crop&scale=both&v=20110713111331000&maxWidth=620",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")

despicable_m3 = media.Movie('Despicable Me 3',
                          'In the film,Gru teams up with his long lost twin Dru in order to defeat a new enemy named Balthazar Bratt, a 1980s child actor who grows up to become a villain',
                          'http://t1.gstatic.com/images?q=tbn:ANd9GcTg3JQThacqbSPauObMc700jNW_GTAd-e9DAV_QIWvMYq8v3mVx',
                          'https://www.youtube.com/watch?v=oagwBHoh6Rs')

wonder_woman = media.Movie('Wonder Woman',
                         'The story of Princess Diana, who grows up on the Amazon island of Themyscira.',
                         'http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H',
                         'https://www.youtube.com/watch?v=VSB4wGIdDwo')

hachiko = media.Movie("Hachi: A Dog's Tale",
                    "A professor finds an abandoned dog and takes him home. Over a period of time, he forms an unbreakable bond with the dog.",
                    "http://www.gstatic.com/tv/thumb/dvdboxart/8051212/p8051212_d_v8_aa.jpg",
                    "https://www.youtube.com/watch?v=inmEtmb3bKM")

minions = media.Movie("Minions",
                    "Minions Kevin, Stuart and Bob decide to find a new master.",
                    "http://cdn.collider.com/wp-content/uploads/minions-poster.jpg",
                    "https://www.youtube.com/watch?v=P9-FCC6I7u0")

# List of movies to be rendered in webpage
movies = [toy_story, avatar, despicable_m3, wonder_woman, hachiko,minions]

# Open a new tab of default web browser to show rendered HTML page
fresh_tomatoes.open_movies_page(movies)
