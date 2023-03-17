from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
  {
    'id': 1,
    'título': '1984',
    'autor': 'George Orwell'
  },
  {
    'id': 2,
    'título': 'A Revolução dos Bichos',
    'autor': 'George Orwell'
  },
  {
    'id': 3,
    'título': 'Dentro da Baleia e Outros Ensaios',
    'autor': 'George Orwell'
  }, 
]

# Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
  return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)