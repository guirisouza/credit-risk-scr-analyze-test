import falcon
from decimal import Decimal
from datetime import datetime
import json
import os


class Home:
    def __init__(self):
        pass

    def on_get(self, req, res):
        res.status = falcon.get_http_status(status_code=200)
        print("Recebido GET em {}".format(datetime.utcnow().isoformat()))
        response_dict = {
            "company": "qi_tech",
            "proccess_id": str(os.getpid())
        }
        res.body = json.dumps(response_dict)

    def on_post(self, req, res):
        body = req.stream.read(req.content_length or 0)
        body = json.loads(body.decode('utf-8'), parse_float=Decimal)
        print("Recebido POST em {}".format(datetime.utcnow().isoformat()))
        res.status = falcon.get_http_status(status_code=200)
        response_dict = {
            "company": "qi_tech",
            "proccess_id": str(os.getpid()),
            "body": body
        }
        res.body = json.dumps(response_dict)
