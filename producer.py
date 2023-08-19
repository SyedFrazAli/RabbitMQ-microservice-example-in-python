import pika

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='orders')

    message = "New order: Product XYZ"
    channel.basic_publish(exchange='', routing_key='orders', body=message)

    print("Sent:", message)
except Exception as e:
    print("Error:", e)
finally:
    connection.close()
