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
    msg.text = msg.text.upper()
    send_to_queue(str(msg))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def send_to_queue(message: str):
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
    channel.queue_declare(queue=config.OUTPUT_QUEUE_NAME, durable=True)
    channel.basic_publish(exchange='', routing_key=config.OUTPUT_QUEUE_NAME, body=message)
    connection.close()


if __name__ == "__main__":
    main()
