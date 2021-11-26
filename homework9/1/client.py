import socket
import argparse
import time
from threading import Lock
from concurrent.futures import ThreadPoolExecutor


class Client:

    BUFFER_SIZE = 8196

    def __init__(self, thread_num, file,
                 s_host='localhost', s_port=12000):
        self.s_host = s_host
        self.s_port = s_port
        self.file = file
        self.thread_num = thread_num
        self.lock = Lock()
        print(f'{time.ctime()}: init client with {self.thread_num} thread and file - {self.file}')

    def send_request(self, url):
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        socket_.connect((self.s_host, self.s_port))
        socket_.sendall(url.encode('utf-8'))

        resp = b''
        while True:
            chunk = socket_.recv(self.BUFFER_SIZE)
            resp += chunk
            if len(chunk) < self.BUFFER_SIZE:
                break
        with self.lock:
            print(resp.decode('utf-8'))

    def run_workers(self):
        with ThreadPoolExecutor(max_workers=self.thread_num) as thread_pool:
            with open(self.file, 'r') as f:
                for url in f:
                    thread_pool.submit(self.send_request, url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', type=int, default=15)
    parser.add_argument('-f', type=str, default='urls.txt')
    args = parser.parse_args()

    client = Client(args.m, args.f)
    client.run_workers()
