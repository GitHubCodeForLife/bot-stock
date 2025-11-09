import pika 
import os

def send_message_to_queue(queue_name, message, properties=None):
    piKaConnection = pika.BlockingConnection(
        pika.ConnectionParameters(
            os.getenv('RABBITMQ_HOST'),
            os.getenv('RABBITMQ_PORT'),
            '/',
            pika.PlainCredentials(os.getenv('RABBITMQ_USERNAME'), os.getenv('RABBITMQ_PASSWORD'))
        )
    )
    channel = piKaConnection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    print("send_message_to_queue: " + message)
    channel.basic_publish(exchange='', routing_key=queue_name, body=message, properties=properties)

def register_listener_to_queue(queue_name, callback):
    piKaConnection = pika.BlockingConnection(
        pika.ConnectionParameters(
            os.getenv('RABBITMQ_HOST'),
            os.getenv('RABBITMQ_PORT'),
            '/',
            pika.PlainCredentials(os.getenv('RABBITMQ_USERNAME'), os.getenv('RABBITMQ_PASSWORD'))
        )
    )
    channel = piKaConnection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

def send_message(message, properties=None):
    queue_name = os.getenv('TASK_QUEUE_NAME')
    send_message_to_queue(queue_name, message, properties)

def register_listener(callback):
    queue_name = os.getenv('TASK_QUEUE_NAME')
    print("Queue name: " + queue_name)
    register_listener_to_queue(queue_name, callback)

