import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = open("html/main_page_head.html").read()

# The main page layout and title bar
main_page_content = open("html/main_page_content.html").read()

# A single movie entry html template
movie_tile_content = open("html/movie_title_content.html").read()


def create_media_tiles_content(media):
    # The HTML content for this section of the page
    content = ''
    for media_item in media:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+',
                                     media_item.trailer_youtube_url)
        youtube_id_match = youtube_id_match \
                           or re.search(r'(?<=be/)[^&#]+',
                                        media_item.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) \
            if youtube_id_match else None

        if media_item.__class__.__name__ == 'TvShow':
            seasons = media_item.seasons
            if media_item.end_year:
                year = media_item.start_year + "-" + media_item.end_year
            else:
                year = media_item.start_year + "-"
        else:
            seasons = "N/A"
            year = media_item.year

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=media_item.title,
            poster_image_url=media_item.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            type=media_item.type,
            storyline=media_item.storyline,
            actors=list2str(media_item.actors),
            imdb_rating=media_item.imdb_rating,
            genre=list2str(media_item.genre),
            year=year,
            seasons=seasons,
            modalid=create_modal_id(media_item.title)
        )
    return content


def open_movies_page(media):

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with
    # the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_media_tiles_content(media))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible

def list2str(list):
    """Takes in a list and returns a comma separated string of list items"""
    string = ''
    for i, item in enumerate(list):
        string += item
        if i < len(list)-1:
            string += ", "
    return string

def create_modal_id(title):
    """Returns string of title where blankspace is replaced with _ """
    return title.replace(" ", "_")