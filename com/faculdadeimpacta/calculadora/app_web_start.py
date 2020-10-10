from flask import Flask, jsonify, request, redirect
import os
import requests, json
#import database_commands
#import mailing_system

class User_Error(Exception):
    pass

app = Flask(__name__)
#sequencia json - userId,name,email,cpf,rg,phone,address,birth,gender
'''
@app.route('/patient/create', methods=['POST'])
def new_patient():
    try:
        new_pacient = request.json
        cpf = int(new_pacient['cpf'])
        #if new_pacient['cpf'] == 387: #-- apenas para teste offline
        check = database_commands.Verify_User(cpf,int(new_pacient['userId']))
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
        user_id = request.json['userId']
        result['pacient'] = database_commands.Pacient_List(user_id)
        result['exam'] = database_commands.Exam_List()
        return jsonify(result), 200
    except Exception:
        return jsonify(status=500),500


@app.route('/exam/create', methods=['POST'])
def exam_create():
    try:
        exam = request.json
        database_commands.Create_Exam(exam)
        print(exam)
        mailing_system.Send_Email(exam)
        return jsonify(status = 0), 200
    except Exception:
        return jsonify(status=500),500


@app.route('/exam', methods=['GET'])
def appointment_by_user():
    try:
        user_id = request.json['userId']
        result = database_commands.Appointment_by_Id(user_id)
        return jsonify(result), 200
    except Exception:
        return jsonify(status=500),500
        '''
@app.route('/')
def index():
    return 'POR FAVOR FUNCIONE!'

#Alterar para a conexão com servidor.
if __name__ == '__main__':
    app.run()