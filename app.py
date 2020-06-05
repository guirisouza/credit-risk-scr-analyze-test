import falcon
from api.resources.home import Home
from api.resources.scr.scr import Scr
from api.resources.scr.report import Report


def create():
    api = falcon.API()
    api.add_route('/', Home())
    api.add_route('/api/scr', Scr())
    api.add_route('/api/scr/report', Report())
    return api


app = application = create()
