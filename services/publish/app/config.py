import os

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')

INPUT_QUEUE_NAME = 'screaming_queue'

EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

EMAIL_RECIPIENTS = [
#     'm.dudinov@innopolis.university',
#     'i.platonov@innopolis.university',
#     'g.butakov@innopolis.university',
#     'a.shaposhnikov@innopolis.university',
#     'n.ruchkin@innopolis.university',
]
