from flask import flask
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
import week1_proj

app = Flask(__name__)
proxied = FlaskBehindProxy(app) # why do we need this line?
app.config['SECRET_KEY'] = 'feb1c9e8ea9fdddc02f87be734929c35'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///youtube-data.db'
db = SQLAlchemy(app)


# want a home page
@app.route('/')
def home_page():
    return render_template('home.html', title='Home Page--Playlist Display', page_title='Home Page')

# want something to get the playlist, like a url with the playlist id in it
@app.route(f'/api/list={playlist_id}')
def return_playlist():
    # want to get something like json or a list of dicts (or that but enclosed in JSON?) to put into the <main> tag in output.html
    # probsbly requires some data transformation, either here or in test_week1_proj
    # don't know how to stick that into an HTML page

    # or maybe split into two functions? one gets the data in its proper format and the other returns a rendered output.html template?


# want to call return_playlist() on submitting a text area 