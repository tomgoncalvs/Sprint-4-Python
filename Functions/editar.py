import cx_Oracle
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Connection.oracle_db import conn
from Functions.listar import listar_membros, listar_disciplinas, listar_cases

def editar_membro():
    listar_membros()
    id = input("Digite o ID do membro a ser editado: ")

    connection = conn()
    cursor = connection.cursor()

    # Verificar se o ID existe
    cursor.execute("SELECT COUNT(*) FROM tb_site_time WHERE id = :id", [id])
    (count,) = cursor.fetchone()
    if count == 0:
        print("Nenhum membro encontrado com o ID fornecido.")
        return

    atualizacoes = {}
    campos_atualizados = []

    url_image = input("Digite a nova URL da imagem (deixe em branco para manter a atual): ")
    if url_image:
        atualizacoes["url_image"] = url_image
        campos_atualizados.append("url_image")

    nome = input("Digite o novo nome do integrante (deixe em branco para manter o atual): ")
    if nome:
        atualizacoes["nome"] = nome
        campos_atualizados.append("nome")

    descricao = input("Digite a nova descrição do integrante (deixe em branco para manter a atual): ")
    if descricao:
        atualizacoes["descricao"] = descricao
        campos_atualizados.append("descricao")

    url_linkedin = input("Digite a nova URL do LinkedIn (deixe em branco para manter a atual): ")
    if url_linkedin:
        atualizacoes["url_linkedin"] = url_linkedin
        campos_atualizados.append("url_linkedin")

    url_github = input("Digite a nova URL do GitHub (deixe em branco para manter a atual): ")
    if url_github:
        atualizacoes["url_github"] = url_github
        campos_atualizados.append("url_github")

    if not atualizacoes:
        print("Nenhuma atualização realizada.")
        return

    atualizacoes['id'] = id
    partes_sql = [f"{campo} = :{campo}" for campo in campos_atualizados]
    sql = f"UPDATE tb_site_time SET {', '.join(partes_sql)} WHERE id = :id"

    try:
        cursor.execute(sql, atualizacoes)

        if cursor.rowcount == 0:
            print("Nenhum membro encontrado com o ID fornecido.")
        else:
            connection.commit()
            print(f"O membro com ID {id} foi atualizado com sucesso. Campos atualizados: {', '.join(campos_atualizados)}")

    except cx_Oracle.DatabaseError as e:
        print("Erro ao editar o membro:", e)
    except Exception as e:
        print("Um erro ocorreu:", e)
    finally:
        cursor.close()
       
#editar_membro()

def editar_disciplina():
    listar_disciplinas()
    id_disciplina = input("Digite o ID da disciplina a ser editada: ")

    connection = conn()
    cursor = connection.cursor()

    # Verificar se o ID existe
    cursor.execute("SELECT COUNT(*) FROM tb_site_disciplinas WHERE id = :id", [id_disciplina])
    (count,) = cursor.fetchone()
    if count == 0:
        print("Nenhuma disciplina encontrada com o ID fornecido.")
        return

    atualizacoes = {}
    campos_atualizados = []

    url_img = input("Digite a nova URL da imagem da disciplina (deixe em branco para manter a atual): ")
    if url_img:
        atualizacoes["url_img"] = url_img
        campos_atualizados.append("url_img")

    titulo = input("Digite o novo título da disciplina (deixe em branco para manter o atual): ")
    if titulo:
        atualizacoes["titulo"] = titulo
        campos_atualizados.append("titulo")

    descricao = input("Digite a nova descrição da disciplina (deixe em branco para manter a atual): ")
    if descricao:
        atualizacoes["descricao"] = descricao
        campos_atualizados.append("descricao")

    if not atualizacoes:
        print("Nenhuma atualização realizada.")
        return

    atualizacoes['id_disciplina'] = id_disciplina
    partes_sql = [f"{campo} = :{campo}" for campo in campos_atualizados]
    sql = f"UPDATE tb_site_disciplinas SET {', '.join(partes_sql)} WHERE id = :id_disciplina"

    try:
        cursor.execute(sql, atualizacoes)

        connection.commit()
        print(f"A disciplina com ID {id_disciplina} foi atualizada com sucesso. Campos atualizados: {', '.join(campos_atualizados)}")

    except cx_Oracle.DatabaseError as e:
        print("Erro ao editar a disciplina:", e)
    except Exception as e:
        print("Um erro ocorreu:", e)
    finally:
        cursor.close()
        connection.close()

#editar_disciplina()

def editar_case():
    listar_cases()
    id_case = input("Digite o ID do case a ser editado: ")

    connection = conn()
    cursor = connection.cursor()

    # Verificar se o ID existe
    cursor.execute("SELECT COUNT(*) FROM tb_site_cases WHERE id = :id", [id_case])
    (count,) = cursor.fetchone()
    if count == 0:
        print("Nenhum case encontrado com o ID fornecido.")
        return

    atualizacoes = {}
    campos_atualizados = []

    url_logo = input("Digite a nova URL do logo do case (deixe em branco para manter a atual): ")
    if url_logo:
        atualizacoes["url_logo"] = url_logo
        campos_atualizados.append("url_logo")
    
    titulo = input("Digite o novo título do case (deixe em branco para manter o atual): ")
    if titulo:
        atualizacoes["titulo"] = titulo
        campos_atualizados.append("titulo")
    
    descricao = input("Digite a nova descrição do case (deixe em branco para manter a atual): ")
    if descricao:
        atualizacoes["descricao"] = descricao
        campos_atualizados.append("descricao")
    
    if not atualizacoes:
        print("Nenhuma atualização realizada.")
        return
    
    atualizacoes['id_case'] = id_case
    partes_sql = [f"{campo} = :{campo}" for campo in campos_atualizados]
    sql = f"UPDATE tb_site_cases SET {', '.join(partes_sql)} WHERE id = :id_case"

    try:
        cursor.execute(sql, atualizacoes)
        connection.commit()
        print(f"O case com ID {id_case} foi atualizado com sucesso. Campos atualizados: {', '.join(campos_atualizados)}")

    except cx_Oracle.DatabaseError as e:
        print("Erro ao editar o case:", e)
    except Exception as e:
        print("Um erro ocorreu:", e)
    finally:
        cursor.close()
        connection.close()

#editar_case()

