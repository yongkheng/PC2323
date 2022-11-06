from jinja2 import Environment, FileSystemLoader

data={
    'navigation': [
        {'href': '/index.html', 'caption': 'Home'},
        {'href': '/about.html', 'caption': 'About'},
        {'href': '/contact.html', 'caption': 'Contact'},
    ],

    'a_variable': 'A short message',
}


env = Environment(
    loader = FileSystemLoader(['./', '/other/path'], encoding='utf8')
)
template = env.get_template('fa04_jinja2_template.j2')
with open('rendered.html', 'w', encoding='utf8') as f:
    rendered = template.render(data)
    f.write(rendered)
