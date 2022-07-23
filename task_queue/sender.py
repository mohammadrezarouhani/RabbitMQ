import pika
import sys

def main(message=''):
    con=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel=con.channel()
    channel.queue_declare('task_queue',durable=True) # for duribillity

    channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE) # for duribillity
            )      
    print('[x] ==> message sent!!!\n')
    con.close()


if __name__=='__main__':
    while(True):
        try:
            message=input('enter a message for processing\n  [x]:')
            main(message)
        except KeyboardInterrupt:
            sys.exit()