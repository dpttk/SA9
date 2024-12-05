from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from time import sleep

from app import config


class FilterFilter:
    def __init__(self, input_queue, output_queue):
        self.input = input_queue
        self.output = output_queue

    def process(self):
        while True:
            msg = self.input.get()
            if msg is None:
                break

            if any(word in msg.text for word in config.STOP_WORDS):
                continue

            self.output.put(msg)


class ScreamingFilter:
    def __init__(self, input_queue, output_queue):
        self.input = input_queue
        self.output = output_queue

    def process(self):
        while True:
            msg = self.input.get()
            if msg is None:
                break

            msg.text = msg.text.upper()

            self.output.put(msg)


class PublisherFilter:
    def __init__(self, input_queue, output_queue):
        self.input = input_queue
        self.output = output_queue

    def process(self):
        while True:
            msg = self.input.get()
            if msg is None:
                break

            self._send_emails(f'From user: {msg.alias}\nMessage: {msg.text}')

    def _send_emails(self, message: str):
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.ehlo()
        s.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)

        for email in config.EMAIL_RECIPIENTS:
            self._send_email(message, email, s)
            sleep(1)

        s.quit()

    def _send_email(self, message: str, recipient: str, sender_session: smtplib.SMTP_SSL):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Letter from assignment'
        msg['From'] = config.EMAIL_SENDER
        msg['To'] = recipient
        msg.attach(MIMEText(message, 'plain'))
        sender_session.sendmail(config.EMAIL_SENDER, recipient, msg.as_string())
