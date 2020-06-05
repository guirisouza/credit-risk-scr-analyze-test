from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf8')


def currencyformat(value):
    return locale.currency(value, grouping=True)

env = Environment(loader=FileSystemLoader('.'))
env.filters['currencyformat'] = currencyformat
template = env.get_template("./templates/src-full-template.html")

def reporter_generator(data, scr_status, infos):
    html_out = template.render(data=data, scr_stats=scr_status, infos=infos)
    HTML(string=html_out).write_pdf("report.pdf")