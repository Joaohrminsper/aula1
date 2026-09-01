import sqlite3
from dataclasses import dataclass
from pathlib import Path


BASE_DIR = Path(__file__).parent
DATABASE = BASE_DIR / 'banco.db'


@dataclass
class Note:
    id: int
    title: str
    content: str


def create_table():
    connection = sqlite3.connect(DATABASE)
    try:
        connection.execute('''
            CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
        ''')
        connection.commit()
    finally:
        connection.close()


def load_data():
    create_table()
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute(
            'SELECT id, title, content FROM note ORDER BY id'
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        connection.close()


def add_data(nova_anotacao):
    create_table()
    connection = sqlite3.connect(DATABASE)
    try:
        connection.execute(
            'INSERT INTO note (title, content) VALUES (?, ?)',
            (nova_anotacao['title'], nova_anotacao['content']),
        )
        connection.commit()
    finally:
        connection.close()

def load_template(arquivo):
    caminho_completo = BASE_DIR / 'static' / 'templates' / arquivo
    with open(caminho_completo, 'r', encoding='utf-8') as arquivo_template:
        return arquivo_template.read()

def delete_data(nota_id):
    connection = sqlite3.connect(DATABASE)
    try:
        connection.execute('DELETE FROM note WHERE id = ?', (nota_id,))
        connection.commit()
    finally:
        connection.close()

def edit_data(nota_id):
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    try:
        row = connection.execute(
            'SELECT id, title, content FROM note WHERE id = ?',
            (nota_id,),
        ).fetchone()

        if row is None:
            return None

        return Note(
            id=row['id'],
            title=row['title'],
            content=row['content'],
        )
    finally:
        connection.close()

def update_data(nota_id, titulo, detalhes):
    connection = sqlite3.connect(DATABASE)
    try:
        connection.execute(
            'UPDATE note SET title = ?, content = ? WHERE id = ?',
            (titulo, detalhes, nota_id),
        )
        connection.commit()
    finally:
        connection.close()
