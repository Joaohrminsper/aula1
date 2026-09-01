from utils import add_data, load_data, load_template, delete_data

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(
            id=dados['id'],
            title=dados['title'],
            details=dados['content'],
        )
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

def delete(nota_id):
    delete_data(nota_id)
