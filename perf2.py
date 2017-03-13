# perf2.py
# requests/sec of fast requests


from socket import *
import time
from threading import Thread


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))

n = 0
stop = 0


def monitor():
    global n
    global stop
    while True or stop > 10:
        time.sleep(1)
        print('{0} reqs/sec'.format(n))
        n = 0
        stop += 1
    stop = 0
    return 0

Thread(target=monitor).start()

while True or stop > 10:
    sock.send(b'1')
    resp = sock.recv(100)
    n += 1
    stop += 1

