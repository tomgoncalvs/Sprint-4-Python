import cx_Oracle
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Connection.oracle_db import conn
from Functions.listar import listar_membros, listar_disciplinas, listar_cases


def deletar_membro():
    listar_membros()
    id = input("Digite o ID do membro a ser deletado: ")

    connection = conn()
    cursor = connection.cursor()

    # Verificar se o ID existe
    cursor.execute("SELECT COUNT(*) FROM tb_site_time WHERE id = :id", [id])
    (count,) = cursor.fetchone()
    if count == 0:
        print("Nenhum membro encontrado com o ID fornecido.")
        return

    # Confirmar a exclusão
    confirmacao = input(f"Tem certeza que deseja deletar o membro com ID {id}? (sim/não): ")
    if confirmacao.lower() != 'sim':
        print("Operação cancelada.")
        return

    try:
        sql = "DELETE FROM tb_site_time WHERE id = :id"
        cursor.execute(sql, [id])

        connection.commit()
        print(f"O membro com ID {id} foi deletado com sucesso.")

    except cx_Oracle.DatabaseError as e:
        print("Erro ao deletar o membro:", e)
    except Exception as e:
        print("Um erro ocorreu:", e)
    finally:
        cursor.close()
        connection.close()

def deletar_disciplina():
    listar_disciplinas()
    id_disciplina = input("Digite o ID da disciplina a ser deletada: ")

    connection = conn()
    cursor = connection.cursor()

    # Verificar se o ID existe
    cursor.execute("SELECT COUNT(*) FROM tb_site_disciplinas WHERE id = :id", [id_disciplina])
    (count,) = cursor.fetchone()
    if count == 0:
        print("Nenhuma disciplina encontrada com o ID fornecido.")
        return

    # Confirmar a exclusão
    confirmacao = input(f"Tem certeza que deseja deletar a disciplina com ID {id_disciplina}? (sim/não): ")
    if confirmacao.lower() != 'sim':
        print("Operação cancelada.")
        return

    try:
        sql = "DELETE FROM tb_site_disciplinas WHERE id = :id"
        cursor.execute(sql, [id_disciplina])

        connection.commit()
        print(f"A disciplina com ID {id_disciplina} foi deletada com sucesso.")

    except cx_Oracle.DatabaseError as e:
        print("Erro ao deletar a disciplina:", e)
    except Exception as e:
        print("Um erro ocorreu:", e)
    finally:
        cursor.close()
        connection.close()

def deletar_case():
    listar_cases()
    id_case = input("Digite o ID do case a ser deletado: ")

    connection = conn()
    cursor = connection.cursor()

    # Verificar se o ID existe
    cursor.execute("SELECT COUNT(*) FROM tb_site_cases WHERE id = :id", [id_case])
    (count,) = cursor.fetchone()
    if count == 0:
        print("Nenhum case encontrado com o ID fornecido.")
        return

    # Confirmar a exclusão
    confirmacao = input(f"Tem certeza que deseja deletar o case com ID {id_case}? (sim/não): ")
    if confirmacao.lower() != 'sim':
        print("Operação cancelada.")
        return

    try:
        sql = "DELETE FROM tb_site_cases WHERE id = :id"
        cursor.execute(sql, [id_case])

        connection.commit()
        print(f"O case com ID {id_case} foi deletado com sucesso.")

    except cx_Oracle.DatabaseError as e:
        print("Erro ao deletar o case:", e)
    except Exception as e:
        print("Um erro ocorreu:", e)
    finally:
        cursor.close()
        connection.close()
