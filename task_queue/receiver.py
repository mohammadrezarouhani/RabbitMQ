import sys
import pika 
import time

def main():
    con=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel=con.channel()
    channel.queue_declare('task_queue',durable=True)

    def callback(ch,method,propertice,body):
        print('processing ==> {}'.format(body))
        time.sleep(body.count(b'.'))
        channel.basic_ack(delivery_tag=method.delivery_tag)
        print('processing done !!!!')
        
    channel.basic_qos(prefetch_count=1)     # for implementing fair dispatching 
    channel.basic_consume(queue='task_queue',on_message_callback=callback)
    channel.start_consuming()

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
