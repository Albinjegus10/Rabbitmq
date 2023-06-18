
import pika

# Establish a connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the message queue
channel.queue_declare(queue='my_queue')

# Define the message you want to send
message = 'Hello, RabbitMQ!'

# Publish the message to the queue
channel.basic_publish(exchange='', routing_key='my_queue', body=message)

# Close the connection to RabbitMQ server
connection.close()
