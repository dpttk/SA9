import os

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')

INPUT_QUEUE_NAME = 'input_queue'
OUTPUT_QUEUE_NAME = 'filtered_queue'

STOP_WORDS = ('bird-watching', 'ailurophobia', 'mango')
