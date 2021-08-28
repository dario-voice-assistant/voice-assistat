from datetime import date
from webbrowser import get
from dario.main import record_audio
from dario import __version__
from dario.main import *

def test_version():
    assert __version__ == '0.1.0'


def test_search():
    assert search(test)==True

def test_youtube():
    assert search_youtube(test)==True

def test_location():
    assert location(test)==True

def test_Jokes():
    assert joke(test)==True

def test_date():
    assert get_date(test)==True

def test_time():
    assert get_time(test)==True

