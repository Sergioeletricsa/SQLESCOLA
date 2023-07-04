import sqlite3
from sqlite3 import Error

########## Criar Conexão
def ConexaoBanco():
    caminho="C:\\Users\\SERGIO-1\\Desktop\\escola-db\\escola.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()
########## Criar tabela
vsql="""CREATE TABLE tb_aluno(
            N_IDALUNO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMEALUNO VARCHAR(30),
            T_EMAILALUNO VARCHAR(30),
            T_ENDALUNO VARCHAR(30)
      );"""
def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as ex:
        print(ex)

criarTabela(vcon,vsql)

vcon.close()
