from datetime import date
from webbrowser import get
from dario.main import record_audio
from dario import __version__
from dario.main import *

def test_version():
    assert __version__ == '0.1.0'


def test_search():
    assert search(test)=='https://google.com/search?q=test'

def test_youtube():
    assert search_youtube(test)=="https://www.youtube.com/results?search_query=test"

def test_location():
    assert location(test)=='https://google.nl/maps/place/test/&amp;'

def test_weather(): 
    assert get_weather(test)=="https://api.weatherbit.io/v2.0/forecast/daily?city=test&key=39577f16323c466893c05341fcc378c6"



