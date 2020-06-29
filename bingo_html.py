from jinja2 import Template
from src.funciones import generar_carton

x = generar_carton()

template = Template(open('HTML/template.j2').read())

print(template.render(carton = x))
