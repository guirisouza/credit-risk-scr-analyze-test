import falcon
from api.resources.home import Home


def create():
    api = falcon.API()
    api.add_route('/', Home())
    return api


app = application = create()
