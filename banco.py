import pymysql

from config import BANCO


def conectar(com_banco=True):
    dados = dict(BANCO)
    if not com_banco:
        dados.pop("database", None)
    return pymysql.connect(**dados)
