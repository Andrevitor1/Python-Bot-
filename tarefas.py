#importando bibliotecas
import schedule
import time
from twilio.rest import Client

#Seus dados twilio 
account_sid = 'SEU_ACCOUNT_SID'
auth_token = 'SEU_AUTH_TOKEN_AQUI'
client = Client(account_sid, auth_token)

#Números do whatsaap necessários 
from_whatsapp_number ='número do whatsapp twilio'
to_whatsapp_number ='seu número do whatsapp'

#Funções com as tarefas desejadas
def enviar_mensagem(mensagem):
    message = client.messages.create(
        body=mensagem,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
    print(f'Mensagem enviada: {mensagem}')

def Acordar():
    enviar_mensagem("O mais importante")

def Café():
    enviar_mensagem("Iniciar o dia")

def Estudar():
    enviar_mensagem("Faça o quanto conseguir")

def Almoço():
    enviar_mensagem("Se alimentar bem")

def Treinar():
    enviar_mensagem("Faça com excelência")            

#Programando horários das tarefas 
schedule.every().day.at("05:00").do(Acordar)  
schedule.every().day.at("05:15").do(Café)  
schedule.every().day.at("05:30").do(Estudar)  
schedule.every().day.at("12:00").do(Almoço)  
schedule.every().day.at("18:30").do(Treinar)     

#Ativando loop para o bot funcionar 
while True:
    schedule.run_pending()  
    time.sleep(1)