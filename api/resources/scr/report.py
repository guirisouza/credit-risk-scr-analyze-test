import falcon
import json
import requests
from utils.reporter_generator import reporter_generator

def calculate_risk(risks):
    risk = {}

    for i in risks:
        risk.update(i)

    total_risk = risk['h']
    credit = risk['a']
    total_responsibility = risk['a']
    
    risk = {
        'total_risk': total_risk,
        'credit': credit,
        'total': round((credit / total_risk), 2),
        'total_responsability': total_responsibility
    }

    return risk
    
def reverse_data(date):
    date = date.split('-')
    date.reverse()
    new_date = '/'.join(date)
    return new_date
    

def src_data_request():
    try:
        data = requests.get('http://www.mocky.io/v2/5ed468883300007900f7a182')
        return data.json()
    except:
        data = {}
        return data


def sorted_due(due_operations, operation_code):

    risk = {}

    ordered_operations = []
    if operation_code == 'a':
        due_lst = list(filter(lambda el: el['due_type']['due_code'] >= 110, due_operations))
        risk[operation_code] = 0
    if operation_code == 'h':
        due_lst = list(filter(lambda el: el['due_type']['due_code'] < 110, due_operations))
        risk[operation_code] = 0
    
    dues_lst = list(set(due['due_type']['due_code'] for due in due_lst))

    total_value_dues = 0

    for due_type in dues_lst:
        dct_due = {
            'due_type_group': '',
            'due_description': '',
            'category_description': '',
            'dues': [],
            'total_value': 0,
        }
        for due in due_operations:
            if due_type == due['due_type']['due_code']:
                dct_due['dues'].append(due)
                dct_due['due_type_group'] = due['due_type']['due_type_group']
                dct_due['due_description'] = due['due_type']['description']
                dct_due['category_description'] = due['category_sub']['description']
                dct_due['total_value'] += round(due['due_value'], 2)
                dct_due['word_identifier'] = operation_code
        total_value_dues += round(dct_due['total_value'], 2)
        dct_due['total_value_dues'] = round(total_value_dues,2)
        risk[operation_code] = round(dct_due['total_value_dues'], 2)
        ordered_operations.append(dct_due)

    return {
        'data': sorted(
                ordered_operations,
                key=lambda due: due['dues'][0]['due_type']['due_code'],
                reverse=False
            ),
        'risk': risk
    }


class Report:
    def on_get(self, req, res):
        try:
            data = src_data_request()
            data_operations = []
            operations_items = data['operation_items']
            a_operations = sorted_due(operations_items, 'a')
            b_operations = sorted_due(operations_items, 'h')
            infos = {
                'reference_data': reverse_data(data['reference_date']),
                'start_relationship': reverse_data(data['start_relationship']),
                'financial_institution_count': data['financial_institution_count'],
            }
            a_operations['data'][0]['total_value_dues'] = a_operations['risk']['a']
            data_operations.append(a_operations['data'])
            data_operations.append(b_operations['data'])
            scr_stats = calculate_risk([a_operations['risk'], b_operations['risk']])
            reporter_generator(data_operations, scr_stats, infos)

            filename="./report.pdf"
            res.downloadable_as = filename
            res.content_type = 'application/pdf'
            res.stream= open(filename, 'rb')
            res.status = falcon.HTTP_200
        
        except:
            res.status = falcon.HTTP_400
            res.body = json.dumps({"message":"Não foi possível gerar o relatório"})
