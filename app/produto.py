
from flask import Flask, request, jsonify, make_response
from typing import List
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='quickstore',
)

class Produto:
    def __init__(self, nomeProduto, idProduto: int, preco: float, quantidade: int):
        self.nomeProduto = nomeProduto
        self.idProduto = idProduto
        self.preco = preco
        self.quantidade = quantidade

def get_produtos():

   mycursor = mydb.cursor()
   mycursor.execute('SELECT * FROM Produto')
   meus_produtos = mycursor.fetchall()
   print(meus_produtos)
   
   return make_response(
       jsonify(
           mensagem='Lista de produtos',
           dados=meus_produtos
       )
   )


# Criar um novo produto POST
def criar():
    data = request.json
    mycursor = mydb.cursor()
    sql = f"insert into produto(nomeProduto, id, preco, qtd) values  ('{data['nome']}',{data['id']},{data['preco']},{data['qtd']});"
    mycursor.execute(sql)
    mydb.commit()
    return make_response(
       jsonify(
           mensagem='Feito com sucesso',
       )
   )

# Descrescer quantidade POST
def retirar():
    data = request.json
    qtd = data['qtd']
    id = data['id']
    mycursor = mydb.cursor()
    sql = f"SELECT qtd FROM produto WHERE id =('{data['id']}');"
    mycursor.execute(sql)
    qtdAtual = mycursor.fetchall()

    if(qtdAtual < qtd):
            return jsonify({'message': 'Quantidade não suficiente.'}), 404
    else:
            qtdfinal=qtdAtual-qtd
            mycursor1 = mydb.cursor()
            sql1 = f"UPDATE produto SET qtd = ('{qtdfinal}') WHERE id = ('{data['id']}');"
            mycursor1.execute(sql1)
            mydb.commit()
            return make_response


# Atualizar um produto existente POST
def atualizar():
    data = request.json
    nomeProduto = data['nome']
    id = data['id']
    preco = data['preco']
    qtd=data['qtd']
    mycursor1 = mydb.cursor()
    sql1 = f"UPDATE produto SET nome, preco, id, qtdI = ('{data['nome']}',{data['id']},{data['preco']},{data['qtd']})  WHERE id = ('{data['id']}');"
    mycursor1.execute(sql1)
    mydb.commit()    
    return make_response


# Deletar um pedido existente POST
def deletar():
    data = request.json
    id = data['id']
    mycursor = mydb.cursor()
    sql = f"DELETE FROM produto WHERE id = ('{data['id']}')"
    mycursor.execute(sql)
    mydb.commit()   
    return make_response()