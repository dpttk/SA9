import pika

from app import config


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
channel.queue_declare(queue=config.QUEUE_NAME, durable=True)


def send_to_queue(message: str):
    channel.basic_publish(exchange='', routing_key=config.QUEUE_NAME, body=message)
