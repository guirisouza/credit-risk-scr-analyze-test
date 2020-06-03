import falcon
from api.resources.home import Home
from api.resources.src.src import Src
from api.resources.src.report import Report


def create():
    api = falcon.API()
    api.add_route('/', Home())
    api.add_route('/src', Src())
    api.add_route('/src/report', Report())
    return api


app = application = create()
