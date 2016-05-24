import webbrowser
import os
import re

# function for return file current position
def get_current_pos():
    return os.path.dirname(os.path.realpath(__file__))

# function for return an specific template
def get_template_path(template):
    return get_current_pos() + os.sep + "templates" + os.sep + template

# function for read a file and return content
def read_file(path):
    file = open(path)
    content = file.read()
    file.close()
    return content

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    movie_tile_content = read_file(get_template_path("media_template.html"))
    
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.name,
            poster_image_url=movie.poster,
            trailer_youtube_id=trailer_youtube_id,
            param1=(movie.year if hasattr(movie, 'year') else movie.seasons),
            param2=(movie.duration if hasattr(movie, 'duration') else movie.tv)
        )
    return content

def startSite(content):
    movies = content['movies']
    series = content['series']

    # Create or overwrite the output file
    output_file = open('movies_site.html', 'w')

    # Load the base html template
    base_path = get_template_path("base.html")
    base_html = read_file(base_path)
    rendered_content = base_html.format(
        movie_tiles=create_movie_tiles_content(movies),
        serie_tiles=create_movie_tiles_content(series),
        header=read_file(get_template_path("header_template.html")))

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
