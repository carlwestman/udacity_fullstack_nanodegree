# Movie Trailer Website

## Project Overview

This project creates a simple one-page website with Movie and Tv-Show
posters from a data structure stored in classes defined in media.py.
The data for each class instance is stored in entertainment_center.py.

From the webpage it is possible to click on the poster to view a
trailer of the Movie or TV-show and to see more information about
the Movie or TV show by clicking on th (i). The extra information
is presented in a modal.

## Data structure
### Media
 The Media class is the parent-class of Movie and TvShow.
 Media contains data that is general for both Movie and TvShow.
 Media contains and is initiated with the following attributes:

 |Attribute Name     | Type          |    Example    |
 |-------------------|---------------|---------------|
 |title              |STRING         |Platoon        |
 |storyline          |STRING         |"Chris Taylor is a young, naive American who gives upcollege and volunteers for combat in Vietnam. Upon arrival, he quickly discovers that his presence is quite nonessential, and is considered insignificant to the other soldiers, as he has not fought for as long as the rest of them and felt the effects of combat. Chris has two non-commissioned officers, the ill-tempered and indestructible Staff Sergeant Robert Barnes and the more pleasant and cooperative Sergeant Elias Grodin. A line is drawn between the two NCOs and a number of men in the platoon when an illegal killing occurs during a village raid. As the war continues, Chris himself draws towards psychological meltdown. And as he struggles for survival, he soon realizes he is fighting two battles, the conflict with the enemy and the conflict between the men within his platoon."|
 |trailer_youtube_url| STRING        | https://www.youtube.com/watch?v=AykiF9YYF2U|
 |actors             |LIST of STRINGs| ["Charlie Sheen", "Tom Berenger", "Willem Dafoe"]|
 |imdb_rating        |FLOAT          | 8.1            |
 |genre              |LIST of STRINGs|["Drama", "War"]|
 |poster_img_url     |STRING         |https://upload.wikimedia.org/wikipedia/en/a/a9/Platoon_posters_86.jpg|

### Movie
Movie is a child class to Media. Movie contains data that is
mostly specific for Movies.
Movie contains the followg attributes:

 |Attribute Name     | Type          |    Example    |
 |-------------------|---------------|---------------|
 |title              |STRING         |Platoon        |
 |storyline          |STRING         |"Chris Taylor is a young, naive American who gives upcollege and volunteers for combat in Vietnam. Upon arrival, he quickly discovers that his presence is quite nonessential, and is considered insignificant to the other soldiers, as he has not fought for as long as the rest of them and felt the effects of combat. Chris has two non-commissioned officers, the ill-tempered and indestructible Staff Sergeant Robert Barnes and the more pleasant and cooperative Sergeant Elias Grodin. A line is drawn between the two NCOs and a number of men in the platoon when an illegal killing occurs during a village raid. As the war continues, Chris himself draws towards psychological meltdown. And as he struggles for survival, he soon realizes he is fighting two battles, the conflict with the enemy and the conflict between the men within his platoon."|
 |trailer_youtube_url| STRING        | https://www.youtube.com/watch?v=AykiF9YYF2U|
 |actors             |LIST of STRINGs| ["Charlie Sheen", "Tom Berenger", "Willem Dafoe"]|
 |imdb_rating        |FLOAT          | 8.1            |
 |genre              |LIST of STRINGs|["Drama", "War"]|
 |poster_img_url     |STRING         |https://upload.wikimedia.org/wikipedia/en/a/a9/Platoon_posters_86.jpg|
 |year               |INT            | 1986           |
 |director           |STRING         |Oliver Stone|
 |type (auto)        |STRING         |Default="Movie"|

 The type attribute is automatically set to Movie upon instance init.
 This attribute is used when rendering the website in order to know
 what information structure template to use.

### TvShow
The TvShow class is a child class to Media. TvShow contains data that is
mostly specific to TvShows.
TvShow contains the following attributes:

 |Attribute Name     | Type          |    Example    |
 |-------------------|---------------|---------------|
 |title              |STRING         |Silicon Vally  |
 |storyline          |STRING         |"In the high-tech gold rush of modern Silicon Valley, the people most qualified to succeed are the least capable of handling success. A comedy partially inspired by Mike Judge's own experiences as a Silicon Valley engineer in the late 1980s."|
 |trailer_youtube_url| STRING        | https://www.youtube.com/watch?v=r8sCCf82Nf8|
 |actors             |LIST of STRINGs| ["Thomas Middleditch", "T.J. Miller", "Josh Brener", "Martin Starr", "Kumail Nanjiani", "Amanda Crew"]|
 |imdb_rating        |FLOAT          | 8.5            |
 |genre              |LIST of STRINGs|["Comedy"]|
 |poster_img_url     |STRING         |https://images-na.ssl-images-amazon.com/images/M/MV5BMTgwNTUzNzIxM15BMl5BanBnXkFtZTgwMzQ1NTk2ODE@._V1_UX182_CR0,0,182,268_AL_.jpg|
 |start_year         |STRING         |'2014'|
 |end_year (optional)|STRING         |'2019', if not supplied, ie. still running attibute value is set to None|
 |seasons            |INT            |4|
 |type  (auto)       |STRING         |Default="TV Show"|

 The type attribute is automatically set to Tv Show upon instance init.
 This attribute is used when rendering the website in order to know
 what information structure template to use.

## Running the project
1. Added data to entertainment_center.py using the appropriate class
defined in media.py.
2. Call fresh_tomatoes.py from terminal:
`python fresh_tomatoes.py`
3. default browser will open with the website rendered with the data
from entertainment_center.py