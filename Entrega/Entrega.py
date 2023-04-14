from flask import Flask, request, jsonify

app = Flask(__name__)

class Entrega:
    def __init__(self, endereco, data, tipo):
        self.endereco = endereco
        self.data = data
        self.tipo = tipo

    def adicionar_entrega(self, endereco, data, tipo):
        self.entrega = Entrega(endereco, data, tipo)

    def calcular_preco_entrega(self):
        if self.entrega is None:
            raise Exception("As informações de entrega não foram fornecidas.")

        preco_entrega = 0.0
        if self.entrega.tipo == 'expresso':
            preco_entrega = 10.0
        elif self.entrega.tipo == 'normal':
            preco_entrega = 5.0

        if self.total > 100.0:
            preco_entrega = preco_entrega * 0.5  # Desconto de 50% na entrega para pedidos acima de R$ 100,00

        return preco_entrega


@app.route('/adicionar_entrega', methods=['POST'])
def adicionar_entrega():
    endereco = request.json['endereco']
    data = request.json['data']
    tipo = request.json['tipo']
    entrega = Entrega(endereco, data, tipo)
    return jsonify({"mensagem": "Entrega adicionada com sucesso!"}), 201

@app.route('/calcular_preco_entrega', methods=['POST'])
def calcular_preco_entrega():
    endereco = request.json['endereco']
    data = request.json['data']
    tipo = request.json['tipo']
    entrega = Entrega(endereco, data, tipo)
    try:
        preco = entrega.calcular_preco_entrega()
        return jsonify({"preco": preco}), 200
    except Exception as e:
        return jsonify({"mensagem": str(e)}), 400