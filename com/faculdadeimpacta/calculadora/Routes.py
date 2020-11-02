from flask import Flask, jsonify, request, redirect
import requests, json
import database_commands
import mailing_system
from flask_cors import CORS

class User_Error(Exception):
    pass

app = Flask(__name__)
CORS(app)
#sequencia json - userId,name,email,cpf,rg,phone,address,birth,gender
@app.route('/patient/create', methods=['POST'])
def new_patient():
    try:
        new_pacient = request.json
        cpf = int(new_pacient['cpf_paciente'])
        #if new_pacient['cpf'] == 387: #-- apenas para teste offline
        check = database_commands.Verify_User(cpf,int(new_pacient['id_usuario']))
        if check == True:
            raise User_Error
        status= database_commands.Create_User(new_pacient)     
        if status['status'] == 400:
            return jsonify(status),400
        else:
            return jsonify(status),200
    except User_Error:
        return jsonify(status = 400),400
    except Exception:
        return jsonify(status=500),500


@app.route('/exam/create', methods=['GET'])
def exam_list():
    try:
        result = {}
        user_id = request.json['id_usuario']
        result['pacientes'] = database_commands.Pacient_List(user_id)
        result['exames'] = database_commands.Exam_List()
        return jsonify(result), 200
    except Exception:
        return jsonify(status=500),500


@app.route('/exam/create', methods=['POST'])
def exam_create():
    try:
        exam = request.json
        database_commands.Create_Exam(exam)
        mailing_system.Send_Email(exam)
        return jsonify(status = 0), 200
    except Exception:
        return jsonify(status=500),500


@app.route('/exam', methods=['GET'])
def appointment_by_user():
    try:
        user_id = request.json['id_usuario']
        result = database_commands.Appointment_by_Id(user_id)
        return jsonify(result), 200
    except Exception:
        return jsonify(status=500),500
        
@app.route('/')
def index():
    result= database_commands.Exam_List()
    return jsonify(result)


@app.route('/login', methods=['POST'])
def login():
    try:
        user = request.json
        email = user['email_usuario']
        senha = user['senha_usuario']
        check = database_commands.Check_Login(email,senha)
        if check == True:
            raise User_Error
        status= database_commands.Create_Login(email,senha)     
        if status['status'] == 400:
            return jsonify(status),400
        else:
            user_id = database_commands.Get_Login(email,senha)
            status['id_usuario'] = user_id
            return jsonify(status),200
    except User_Error:
        return jsonify(status = 400),400
    except Exception:
        return jsonify(status=500),500


@app.route('/login', methods=['GET'])
def Verify_Login():
    #try:
    status = {}
    user = request.json
    email = user['email_usuario']
    senha = user['senha_usuario']
    check = database_commands.Check_Login(email,senha)
        #if check == False:
            #raise User_Error
        #else:
    user_id = database_commands.Get_Login(email,senha)
    status['id_usuario'] = user_id
    return jsonify(status),200
    '''except User_Error:
        return jsonify(status = 400),400
    except Exception:
        return jsonify(status=500),500'''

@app.route('/login/teste', methods=['POST'])
def Verify_Login1():
    #try:
    status = {}
    user = request.json
    email = user['email_usuario']
    senha = user['senha_usuario']
    check = database_commands.Check_Login(email,senha)
        #if check == False:
            #raise User_Error
        #else:
    user_id = database_commands.Get_Login(email,senha)
    status['id_usuario'] = user_id
    return jsonify(status),200
    '''except User_Error:
        return jsonify(status = 400),400
    except Exception:
        return jsonify(status=500),500'''

#Alterar para a conexão com servidor.
if __name__ == '__main__':
    app.run()