from flask import Flask, request, jsonify

app = Flask(__name__)

clientes = []

class Cliente:
    def __init__(self, nome, endereco, email, telefone):
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

@app.route('/clientes', methods=['POST'])
def cadastrar_cliente():
    nome = request.json['nome']
    endereco = request.json['endereco']
    email = request.json['email']
    telefone = request.json['telefone']
    novo_cliente = Cliente(nome, endereco, email, telefone)
    clientes.append(novo_cliente)
    return jsonify({'message': 'Cliente cadastrado com sucesso!'})

@app.route('/clientes/<email>', methods=['GET'])
def exibir_cliente(email):
    for cliente in clientes:
        if cliente.email == email:
            return jsonify({
                'nome': cliente.nome,
                'endereco': cliente.endereco,
                'telefone': cliente.telefone
            })
    return jsonify({'message': 'Cliente não encontrado.'})

@app.route('/clientes/<email>', methods=['PUT'])
def atualizar_cliente(email):
    for cliente in clientes:
        if cliente.email == email:
            cliente.nome = request.json['nome']
            cliente.endereco = request.json['endereco']
            cliente.telefone = request.json['telefone']
            return jsonify({'message': 'Cliente atualizado com sucesso!'})
    return jsonify({'message': 'Cliente não encontrado.'})

@app.route('/clientes/<email>', methods=['DELETE'])
def excluir_cliente(email):
    for cliente in clientes:
        if cliente.email == email:
            clientes.remove(cliente)
            return jsonify({'message': 'Cliente excluído com sucesso!'})
    return jsonify({'message': 'Cliente não encontrado.'})

if __name__ == '__main__':
    app.run()
