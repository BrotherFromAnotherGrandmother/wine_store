from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def str_years(digit:int):
    if digit % 100 in [10,11,12,13,14,15,16,17,18,19,20]:
        return 'лет'
    if digit % 10 == 1:
        return 'год'
    elif digit % 10 in [2,3,4]:
        return 'года'
    if digit % 10 in [5,6,7,8,9,0]:
        return 'лет'

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

based = 1920
now = datetime.now().year
delta = now - based

string = str_years(delta)

rendered_page = template.render(
    years_counter=delta,
    string_years=string,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8002), SimpleHTTPRequestHandler)
server.serve_forever()