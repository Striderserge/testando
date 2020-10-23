import mysql.connector



def Connection_String():
    connection = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "1234",
    database = "sergio"
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
        sql = "INSERT INTO paciente(user_id, name, email, cpf, rg, phone, address, birth, gender) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(int(dados['userId']), str(dados['name']), str(dados['email']), int(dados['cpf']), str(dados['rg']), str(dados['phone']), str(dados['address']), str(dados['birth']), str(dados['gender'])))
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
    sql = "SELECT cpf FROM paciente WHERE cpf = %s and user_id = %s"
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
    sql = "SELECT id,name,cpf from paciente where user_id = %s"
    cursor.execute(sql,(id,))
    rows = cursor.fetchall()
    pacient_list = rows_to_dict(cursor.description, rows)
    cursor.close()
    connection.close()
    return pacient_list

def Exam_List():
    connection = Connection_String()
    cursor = connection.cursor()
    sql = "SELECT id, name FROM exame"
    cursor.execute(sql,())
    rows = cursor.fetchall()
    exam_list = rows_to_dict(cursor.description, rows)
    cursor.close()
    connection.close()
    return exam_list


def Create_Exam(exam):
    connection = Connection_String()
    cursor = connection.cursor()
    sql = 'INSERT INTO agendamento(data_agendamento, exam_id, patient_id, user_id) VALUES (%s, %s, %s, %s)'
    cursor.execute(sql,(exam['date'], exam['examId'], exam['patientId'], exam['userId']))
    connection.commit()
    cursor.close()
    connection.close()


def Mail_Select(exam):
    connection = Connection_String()
    
    cursor = connection.cursor()
    sql = """SELECT 
	            ag.id, 
	            ex.name as exname, 
	            ag.data_agendamento, 
	            pt.name, 
                pt.email 
            FROM  
	            agendamento AS ag INNER JOIN 
	            exame AS ex ON ag.exam_id = ex.id INNER JOIN 
	            paciente AS pt ON ag.patient_id = pt.id 
            WHERE 
	            ag.id = (SELECT MAX(id) FROM agendamento WHERE user_id = %s);"""
    cursor.execute(sql,(exam['userId'],))
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    return row


def Appointment_by_Id(userId):
    connection = Connection_String()
    cursor = connection.cursor()
    sql = """
        SELECT 
	            ag.id, 
	            ex.name as exname, 
	            ag.data_agendamento, 
	            pt.name
            FROM  
	            agendamento AS ag INNER JOIN 
	            exame AS ex ON ag.exam_id = ex.id INNER JOIN 
	            paciente AS pt ON ag.patient_id = pt.id 
            WHERE 
	            ag.user_id = %s;
        """
    cursor.execute(sql,(userId,))
    rows = cursor.fetchall()
    appointment_list = rows_to_dict(cursor.description, rows)
    cursor.close()
    connection.close()
    return appointment_list


def Check_Login(email,senha):
    connection = Connection_String()
    cursor = connection.cursor()
    sql = "SELECT user_id FROM usuario WHERE email = %s and password = %s"
    cursor.execute(sql, (email,senha))
    test = cursor.fetchone()
    cursor.close()
    connection.close()
    if test != None: 
        return False
    return True


def Create_Login(email,senha):
    status = {}
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "INSERT INTO usuario(email, password) VALUES(%s, %s)"
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
    sql = "SELECT user_id FROM usuario WHERE email = %s and password = %s"
    cursor.execute(sql, (email,senha))
    test = cursor.fetchone()
    cursor.close()
    connection.close()
    return test


