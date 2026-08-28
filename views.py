from utils import add_data, load_data, load_template

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['title'], details=dados['content'])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    params = {
        'title': titulo,
        'content': detalhes,
    }
    add_data(params)
