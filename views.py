from utils import add_data, load_data, load_template

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    params = {
        'titulo': titulo,
        'detalhes': detalhes,
    }
    add_data('notes.json', params)
