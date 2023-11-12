import cx_Oracle
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Connection.oracle_db import conn

def listar_membros():
    connection = conn()
    cursor = connection.cursor()

    try:
        sql = "SELECT id, nome FROM tb_site_time"
        cursor.execute(sql)

        print("Membros disponíveis:")
        for id, nome in cursor:
            print(f"ID: {id}, Nome: {nome}")

    except cx_Oracle.DatabaseError as e:
        print("Erro ao acessar a base de dados:", e)
    finally:
        cursor.close()
        connection.close()

def listar_disciplinas():
    connection = conn()
    cursor = connection.cursor()

    try:
        sql = "SELECT id, titulo, descricao FROM tb_site_disciplinas"
        cursor.execute(sql)

        print("Disciplinas disponíveis:")
        for id, nome, descricao in cursor:
            print("===============================================")
            print(f" ID: {id}\n Nome: {nome}\n Descrição: {descricao}")
            print("===============================================\n")

    except cx_Oracle.DatabaseError as e:
        print("Erro ao acessar a base de dados:", e)
    finally:
        cursor.close()
        connection.close()

def listar_cases():
    connection = conn()
    cursor = connection.cursor()

    try:
        sql = "SELECT id, titulo, descricao FROM tb_site_cases"
        cursor.execute(sql)

        print("Cases disponíveis:")
        for id, nome, descricao in cursor:
            print("===============================================")
            print(f" ID: {id}\n Nome: {nome}\n Descrição: {descricao}")
            print("===============================================\n")

    except cx_Oracle.DatabaseError as e:
        print("Erro ao acessar a base de dados:", e)
    finally:
        cursor.close()
        connection.close()