import falcon
from decimal import Decimal
from datetime import datetime
import json
import os
import requests

def src_data_request():
    data = requests.get('http://www.mocky.io/v2/5ed468883300007900f7a182')
    return data.json()


class Report:
    def on_get(self, req, res):
        data = falcon.uri.parse_query_string(req.query_string)
        bodyj = req.stream.read()
        print('aaaaaaaaaaaa',data)
        print('aaaaaaaaaaaa',bodyj)
