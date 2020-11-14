import mysql.connector
from datetime import datetime,timezone,timedelta
import pytz



def Connection_String():
    connection = mysql.connector.connect(
    host = "boqd43jjdhnntmzjlj1a-mysql.services.clever-cloud.com",
    user = "upecywjre2o1y8c7",
    password = "FGqNH0hsA0RvMzj519p0",
    database = "boqd43jjdhnntmzjlj1a"
    )
    return connection


def row_to_dict(description, row):
    if row == None: return None
    dictionary = {}
    for item in range(0, len(row)):
        dictionary[description[item][0]] = row[item]
    return dictionary


def rows_to_dict(description, rows):
    result = []
    for row in rows:
        result.append(row_to_dict(description, row))
    return result


def Create_User(dados):
    status = {}
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "INSERT INTO tb_paciente(id_usuario, nome_paciente, email_paciente, cpf_paciente, rg_paciente, telefone_paciente, endereco_paciente, dt_nascimento, sexo_paciente, st_paciente) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(int(dados['id_usuario']), str(dados['nome_paciente']), str(dados['email_paciente']), int(dados['cpf_paciente']), str(dados['rg_paciente']), str(dados['telefone_paciente']), str(dados['endereco_paciente']), str(dados['dt_nascimento']), str(dados['sexo_paciente']), str(dados['st_paciente'])))
        connection.commit()
        status['status'] = 0
    except Exception:
        connection.rollback()
        status['status'] = 400
    finally:
        cursor.close()
        connection.close()
        return status


def Delete_Patient(dados):
    status = {}
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "UPDATE tb_paciente SET  st_paciente = %s where id_paciente = %s"
        cursor.execute(sql,(str(dados['st_paciente']), int(dados['id_paciente'])))
        connection.commit()
        status['status'] = 0
    except Exception:
        connection.rollback()
        status['status'] = 400
    finally:
        cursor.close()
        connection.close()
        return status


def Update_User(dados):
    status = {}
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "UPDATE tb_usuario SET  senha_usuario = %s where id_usuario = %s"
        cursor.execute(sql,(str(dados['senha_usuario']), int(dados['id_usuario'])))
        connection.commit()
        status['status'] = 0
    except Exception:
        connection.rollback()
        status['status'] = 400
    finally:
        cursor.close()
        connection.close()
        return status


def Update_Patient(dados):
    status = {}
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "UPDATE tb_paciente SET  nome_paciente = %s, email_paciente = %s, cpf_paciente = %s, rg_paciente = %s, telefone_paciente = %s, endereco_paciente = %s, dt_nascimento = %s, sexo_paciente = %s, st_paciente = %s where id_paciente = %s"
        cursor.execute(sql,(str(dados['nome_paciente']), str(dados['email_paciente']), int(dados['cpf_paciente']), str(dados['rg_paciente']), str(dados['telefone_paciente']), str(dados['endereco_paciente']), str(dados['dt_nascimento']), str(dados['sexo_paciente']),str(dados['st_paciente']), int(dados['id_paciente'])))
        connection.commit()
        status['status'] = 0
    except Exception:
        connection.rollback()
        status['status'] = 400
    finally:
        cursor.close()
        connection.close()
        return status

def Verify_User(cpf,id):
    connection = Connection_String()
    cursor = connection.cursor()
    sql = "SELECT cpf_paciente FROM tb_paciente WHERE cpf_paciente = %s and id_usuario = %s"
    cursor.execute(sql, (cpf,id))
    test = cursor.fetchone()
    cursor.close()
    connection.close()
    if test != None: 
        return True
    return False

def Pacient_List(id):
    connection = Connection_String()
    cursor = connection.cursor()
    sql = "SELECT * from tb_paciente where id_usuario = %s"
    cursor.execute(sql,(id,))
    rows = cursor.fetchall()
    pacient_list = rows_to_dict(cursor.description, rows)
    cursor.close()
    connection.close()
    return pacient_list

def Exam_List():
    connection = Connection_String()
    cursor = connection.cursor()
    sql = "SELECT id_exame, nome_exame FROM tb_exame"
    cursor.execute(sql,())
    rows = cursor.fetchall()
    exam_list = rows_to_dict(cursor.description, rows)
    cursor.close()
    connection.close()
    return exam_list


def Create_Exam(exam):
    connection = Connection_String()
    cursor = connection.cursor()
    sql = "INSERT INTO tb_agendamento(dt_agendamento, id_exame, id_paciente, id_usuario, convenio, unidade_agendamento) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql,(exam['dt_agendamento'], exam['id_exame'], exam['id_paciente'], exam['id_usuario'], exam['convenio'], exam['unidade_agendamento']))
    connection.commit()
    cursor.close()
    connection.close()


def Mail_Select(exam):
    connection = Connection_String()
    
    cursor = connection.cursor()
    sql = """SELECT 
	            ag.id_agendamento, 
	            ex.nome_exame, 
	            ag.dt_agendamento, 
	            pt.nome_paciente, 
                pt.email_paciente 
            FROM  
	            tb_agendamento AS ag INNER JOIN 
	            tb_exame AS ex ON ag.id_exame = ex.id_exame INNER JOIN 
	            tb_paciente AS pt ON ag.id_paciente = pt.id_paciente 
            WHERE 
	            ag.id_agendamento = (SELECT MAX(id_agendamento) FROM tb_agendamento WHERE id_usuario = %s);"""
    cursor.execute(sql,(exam['id_usuario'],))
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    return row


def Appointment_by_Id(userId):
    connection = Connection_String()
    cursor = connection.cursor()
    sql = """
        SELECT 
	            ag.id_agendamento, 
	            ex.nome_exame, 
	            ag.dt_agendamento, 
	            pt.nome_paciente
            FROM  
	            tb_agendamento AS ag INNER JOIN 
	            tb_exame AS ex ON ag.id_exame = ex.id_exame INNER JOIN 
	            tb_paciente AS pt ON ag.id_paciente = pt.id_paciente 
            WHERE 
	            ag.id_usuario = %s;
        """
    cursor.execute(sql,(userId,))
    rows = cursor.fetchall()
    appointment_list = rows_to_dict(cursor.description, rows)
    data_e_hora = datetime.strptime(appointment_list[2], "%Y-%m-%d %H:%M:%S")
    fuso_horario = timezone("America/Sao_Paulo")
    appointment_list[2] = data_e_hora.astimezone(fuso_horario)
    cursor.close()
    connection.close()
    return appointment_list


def Check_Login(email,senha):
    connection = Connection_String()
    cursor = connection.cursor()
    sql = "SELECT id_usuario FROM tb_usuario WHERE email_usuario = %s and senha_usuario = %s"
    cursor.execute(sql, (email,senha))
    test = cursor.fetchone()
    cursor.close()
    connection.close()
    if test != None: 
        return True
    return False


def Create_Login(email,senha):
    status = {}
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "INSERT INTO tb_usuario(email_usuario, senha_usuario) VALUES(%s, %s)"
        cursor.execute(sql,(email, senha))
        connection.commit()
        status['status'] = 0
    except Exception:
        connection.rollback()
        status['status'] = 400
    finally:
        cursor.close()
        connection.close()
        return status

def Get_Login(email,senha):
    connection = Connection_String()
    cursor = connection.cursor()
    sql = "SELECT id_usuario FROM tb_usuario WHERE email_usuario = %s and senha_usuario = %s"
    cursor.execute(sql, (email,senha))
    test = cursor.fetchone()
    cursor.close()
    connection.close()
    return test

def exam_test():
    connection = Connection_String()
    cursor = connection.cursor()
    sql = 'INSERT INTO tb_exame(nome_exame) VALUES (%s)'
    cursor.execute(sql,('exameteste2',))
    connection.commit()
    cursor.close()
    connection.close()

