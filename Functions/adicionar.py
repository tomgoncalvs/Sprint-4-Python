import cx_Oracle
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Connection.oracle_db import conn

def adicionar_membro():

    url_image = input("Digite a URL da imagem: ")
    nome = input("Digite o nome do integrante: ")
    descricao = input("Digite a descrição do integrante: ")
    url_linkedin = input("Digite a URL do LinkedIn: ")
    url_github = input("Digite a URL do GitHub: ")

    connection = conn()
    cursor = connection.cursor()

    try:
        sql = '''INSERT INTO tb_site_time (url_image, nome, descricao, url_linkedin, url_github)
                 VALUES (:url_image, :nome, :descricao, :url_linkedin, :url_github)'''

        cursor.execute(sql, [url_image, nome, descricao, url_linkedin, url_github])

        connection.commit()

        print("O membro " + nome + " foi adicionado com sucesso.")
    except cx_Oracle.DatabaseError as e:
        print("Erro ao adicionar membro:", e)
    finally:
        cursor.close()
        connection.close()

#adicionar_membro()


def adicionar_cases():
    url_logo = input("Digite a URL do logo: ")
    titulo = input("Digite o título do case: ")
    descricao = input("Digite a descrição do case: ")
    botao = input("Digite o texto do botão: ")

    connection = conn()
    cursor = connection.cursor()

    try:
        sql = '''INSERT INTO tb_site_cases (url_logo, titulo, descricao, botao)
                 VALUES (:url_logo, :titulo, :descricao, :botao)'''

        cursor.execute(sql, [url_logo, titulo, descricao, botao])

        connection.commit()

        print("Case adicionado com sucesso.")
    except cx_Oracle.DatabaseError as e:
        print("Erro ao adicionar o case:", e)
    finally:
        cursor.close()
        connection.close()

#adicionar_cases()

def adicionar_disciplinas():
    url_img = input("Digite a URL da imagem da disciplina: ")
    titulo = input("Digite o título da disciplina: ")
    descricao = input("Digite a descrição da disciplina: ")

    connection = conn()
    cursor = connection.cursor()

    try:
        sql = '''INSERT INTO tb_site_disciplinas (url_img, titulo, descricao)
                 VALUES (:url_img, :titulo, :descricao)'''

        cursor.execute(sql, [url_img, titulo, descricao])

        connection.commit()

        print("Disciplina adicionada com sucesso.")
    except cx_Oracle.DatabaseError as e:
        print("Erro ao adicionar a disciplina:", e)
    finally:
        cursor.close()
        connection.close()

#adicionar_disciplinas()