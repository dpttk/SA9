from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from time import sleep

import pika

from app import config
from app.domain.message import Message


def main():
    credentials = pika.PlainCredentials(username=config.RABBITMQ_USER, password=config.RABBITMQ_PASSWORD)
    connection_parameters = pika.ConnectionParameters(
        credentials=credentials,
        host=config.RABBITMQ_HOST,
        port=config.RABBITMQ_PORT,
        heartbeat=600,
        blocked_connection_timeout=300,
    )
    connection = pika.BlockingConnection(parameters=connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue=config.INPUT_QUEUE_NAME, durable=True)
    channel.basic_consume(queue=config.INPUT_QUEUE_NAME, on_message_callback=callback)
    channel.start_consuming()


def callback(ch, method, properties, body):
    data = body.decode().split('\n')
    msg = Message(alias=data[0], text=data[1])
    send_emails(f'From user: {msg.alias}\nMessage: {msg.text}')
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_emails(message: str):
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    s.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)

    for email in config.EMAIL_RECIPIENTS:
        send_email(message, email, s)
        sleep(1)

    s.quit()


def send_email(message: str, recipient: str, sender_session: smtplib.SMTP_SSL):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Letter from assignment'
    msg['From'] = config.EMAIL_SENDER
    msg['To'] = recipient
    msg.attach(MIMEText(message, 'plain'))
    sender_session.sendmail(config.EMAIL_SENDER, recipient, msg.as_string())


if __name__ == "__main__":
    main()
