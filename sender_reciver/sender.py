from fileinput import close
import pika

con = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = con.channel()
channel.queue_declare('hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello Word')
con.close()

