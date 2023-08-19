import pika

def callback(ch, method, properties, body):
    print("Received:", body)

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='orders')

    channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)

    print("Waiting for messages...")
    channel.start_consuming()
except Exception as e:
    print("Error:", e)
