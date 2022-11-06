from jinja2 import Template
template = Template("Hello {{ name }}! Nice to see you!")
print(template.render(name="John Smith"))
