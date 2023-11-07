from flask import Flask, request, jsonify
import mysql.connector

db_config = mysql.connector.connect(
    user = 'root',
    password = '123456',
    host = 'localhost',
    database = 'banco_de_dados',
)

cursor = db_config.cursor()

app = Flask(__name__)

@app.route('/salvar_usuario', methods = ['POST'])
def salvar_usuario():
    dados_usuarios = request.json
    nome = dados_usuarios['nome']
    telefone = dados_usuarios['telefone']
    insert_query = 'INSERT INTO usuarios (nome, telefone) VALUES (%s, %s)'
    cursor.execute(insert_query, (nome, telefone))
    db_config.commit()
    return jsonify({'message': 'Usuário salvo com sucesso!'})


@app.route('/buscar', methods = ['GET'])
def buscar():
    insert_query = 'SELECT * FROM usuarios'
    cursor.execute(insert_query)
    usuarios = cursor.fetchall()
    lista_usuarios = [{'id': usuario[0], 'nome': usuario[1], 'telefone': usuario[2]} for usuario in usuarios]
    return jsonify(lista_usuarios)

@app.route('/deletar/<id>', methods = ['DELETE'])
def deletar(id):
    query = "DELETE FROM usuarios WHERE idusuarios = %s"
    cursor.execute(query, (id,))
    db_config.commit()
    return jsonify({'message': 'Usuário morto com sucesso!'})



if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)

cursor.close()
db_config.close()