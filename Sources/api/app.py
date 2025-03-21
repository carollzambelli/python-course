from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_class.db'
db = SQLAlchemy(app)

class Books(db.Model): 
    titulo = db.Column(db.String, primary_key=True)
    autor = db.Column(db.String)
    
@app.route('/', methods=['GET'])
def index():    
    livros = Books.query.all()
    return render_template('index.html', livros=livros)

@app.route('/add', methods=['POST'])
def add_books():
    titulo=request.form.get('titulo'),
    autor=request.form.get('autor')
    if titulo != '' and autor != '' :
        b = Books(titulo=titulo[0], autor=autor)
        db.session.add(b)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<titulo>')
def delete_book(titulo):
    data = Books.query.get(titulo)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
  app.run()