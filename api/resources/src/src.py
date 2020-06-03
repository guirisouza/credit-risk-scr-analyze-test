import falcon
from decimal import Decimal
from datetime import datetime
import json
import os
import requests

def src_data_request():
    data = requests.get('http://www.mocky.io/v2/5ed468883300007900f7a182')
    return data.json()


class Src:
    def on_get(self, req, res):
        res.status = falcon.get_http_status(status_code=200)
        data = falcon.uri.parse_query_string(req.query_string)
        bodyj = req.stream.read()
        print('aaaaaaaaaaaa',data)
        print('aaaaaaaaaaaa',bodyj)
        print("Recebido POST em {}".format(datetime.utcnow().isoformat()))
        data_dict = src_data_request()
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',data_dict['subjudice_operations_count'])
        res.body = json.dumps(data_dict)
