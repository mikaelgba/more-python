from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mensagem = "Mensagem do email"
password = "senha do email origem"
email_origem = "email origem"
email_destino = "email destino"
email_titulo = "Titulo da mensagem"


def enviar(mensagem_entrada, password_entrada, email_origem, email_destino, email_titulo):

    email_enviado = MIMEMultipart()
    mensagem = mensagem_entrada
    password = password_entrada
    email_enviado['From'] = email_origem
    email_enviado['To'] = email_destino
    email_enviado['Subject'] = email_titulo

    email_enviado.attach(MIMEText(mensagem, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls()
    server.login(email_enviado['From'], password)
    server.sendmail(email_enviado['From'], email_enviado['To'], email_enviado.as_string())
    server.quit()