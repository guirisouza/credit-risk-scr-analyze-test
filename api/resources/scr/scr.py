import falcon
import json
import requests

def src_data_request():
    data = requests.get('http://www.mocky.io/v2/5ed468883300007900f7a182')
    return data.json()


class Scr:
    def on_get(self, req, res):
        try:
            data = src_data_request()
            due_lst = []
            for due in data['operation_items']:
                due_blueprint = {}
                due_blueprint['category_description'] = due['category_sub']['category']['category_description']
                due_blueprint['category_sub_description'] = due['category_sub']['description']
                due_blueprint['due_description'] = due['due_type']['description']
                due_blueprint['due_type_group'] = due['due_type']['due_type_group'] 
                due_blueprint['due_value'] = due['due_value']
                due_blueprint['due_code'] = due['due_type']['due_code']
                due_lst.append(due_blueprint)
            data['operation_items'] = due_lst

            res.body = json.dumps(data)
        except:
            res.status = falcon.HTTP_400
            res.body = json.dumps({"message":"Não foi possível gerar o consolidado SCR"})
        