import pika

# Establish a connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the message queue
channel.queue_declare(queue='my_queue')

# Define a callback function to process received messages
def callback(ch, method, properties, body):
    print(f"Received message: {body}")

# Set up the callback function to consume messages from the queue
channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)

# Start consuming messages
channel.start_consuming()
