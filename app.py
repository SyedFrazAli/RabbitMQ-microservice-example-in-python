import streamlit as st
import pika
st.title("2 : RabbitMQ")
st.title("E-commerce Order Interface by Fraz")

message = st.text_input("Enter the order details:")
if st.button("Place Order"):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='orders')
    channel.basic_publish(exchange='', routing_key='orders', body=message)

    st.success(f"Order placed: {message}")
    connection.close()
