import os

pid = os.fork()

def ping(x):
    h_up = os.system(f'ping 192.168.1.{x} -n 2 -w 0.1 > Null')
    if h_up:
        print(f'192.168.1.{x} is down')
    else:
        print(f'192.168.1.{x} is up')


for i in range(255):
    if pid == 0:
        ping(i)

    ping(255 - i)
