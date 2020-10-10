from flask import Flask, jsonify, request, redirect
import requests, json
app = Flask(__name__)
@app.route('/')
def index():
    return 'Por favor nunca te pedi nada, funcione!'

#Alterar para a conexão com servidor.
if __name__ == '__main__':
    app.run()