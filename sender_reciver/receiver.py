import pika
import sys
import os


def main():
    con = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = con.channel()
    channel.queue_declare('hello')

    def callback(ch, method, propertice, body):
        print(ch)
        print(method)
        print(propertice)
        print(body)

    channel.basic_consume(queue='hello', on_message_callback=callback,auto_ack=True)
    print('waiting for recieving a message!!!')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('interrupted')
        try:
            sys.exit()
        except SystemExit:
            os._exit(0)