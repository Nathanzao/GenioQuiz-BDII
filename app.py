import os
import sqlite3
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

DB_PATH = os.path.join(app.root_path, 'prompts.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute('''
        CREATE TABLE IF NOT EXISTS prompts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            image_path TEXT,
            parent_id INTEGER DEFAULT NULL
        )
    ''')
    try:
        conn.execute('ALTER TABLE prompts ADD COLUMN parent_id INTEGER DEFAULT NULL')
        conn.commit()
    except sqlite3.OperationalError:
        pass
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        image = request.files.get('image')
        img_path = ''
        if image and image.filename:
            img_path = os.path.join('uploads', image.filename)
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(full_path)
        conn = get_db()
        conn.execute('INSERT INTO prompts (text, image_path) VALUES (?, ?)', (prompt, img_path))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    conn = get_db()
    rows = conn.execute('SELECT * FROM prompts ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', prompts=rows)

@app.route('/edit/<int:pid>', methods=['GET', 'POST'])
def edit_prompt(pid):
    conn = get_db()
    if request.method == 'POST':
        new_prompt = request.form.get('prompt', '')
        image = request.files.get('image')
        img_path = ''
        if image and image.filename:
            img_path = os.path.join('uploads', image.filename)
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(full_path)
        if img_path:
            conn.execute('UPDATE prompts SET text = ?, image_path = ? WHERE id = ?', (new_prompt, img_path, pid))
        else:
            conn.execute('UPDATE prompts SET text = ? WHERE id = ?', (new_prompt, pid))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    row = conn.execute('SELECT * FROM prompts WHERE id = ?', (pid,)).fetchone()
    conn.close()
    if not row:
        return 'Prompt nao encontrado', 404
    return render_template('edit.html', prompt=row)

@app.route('/evolve/<int:pid>', methods=['GET'])
def evolve_prompt(pid):
    conn = get_db()
    row = conn.execute('SELECT * FROM prompts WHERE id = ?', (pid,)).fetchone()
    if not row:
        conn.close()
        return 'Prompt nao encontrado', 404
    conn.execute(
        'INSERT INTO prompts (text, image_path, parent_id) VALUES (?, ?, ?)',
        (row['text'], row['image_path'], pid)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
