from flask import Flask, abort, redirect, render_template_string, request
import views
from utils import load_data, load_template


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_note():
    nota_id = request.form.get('id')
    views.delete(nota_id)
    return redirect('/')

@app.route('/update/<nota_id>', methods=['GET'])
def edit_note(nota_id):
    edit_page = views.edit(nota_id)
    if edit_page is None:
        abort(404)
    return render_template_string(edit_page)

@app.route('/update', methods=['POST'])
def update_note():
    nota_id = request.form.get('id')
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')

    views.update(nota_id, titulo, detalhes)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
