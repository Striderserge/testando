import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import database_commands
""" PREVIA DE DADOS PARA ENVIAR
    ag.id, 
    ex.name as exname, 
    ag.data_agendamento, 
    pt.name, 
    pt.email """
def Send_Email(exam):
    data = database_commands.Mail_Select(exam)
    sender_address = 'teste.bild@gmail.com'
    sender_pass = 'bild2507'
    receiver_address = [str(data[4]),sender_address]
    mail_content = '''Paciente : {}
    Data pré-agendada : {}
    Exame : {}
    '''.format(str(data[3]),str(data[2]),str(data[1]))
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = str(receiver_address)
    message['Subject'] = 'Pré Agendamento de Exame.'
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls() 
        session.login(sender_address, sender_pass) 
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
    except:
        print('Something went wrong...')
