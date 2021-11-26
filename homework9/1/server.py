import socket
import argparse
import time

import requests
import json
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from collections import Counter


def parse(url, raw_html, top=10):
    word_list = BeautifulSoup(raw_html, 'lxml').text.split()
    cleaned_list = [word for word in word_list if word[0].isalpha()]
    counter = Counter(cleaned_list)
    array = {
        word: count for word, count in counter.most_common(min(top, len(cleaned_list)))
    }
    return json.dumps({url.strip(): array}, indent=4)


class Server:

    BUFFER_SIZE = 8196

    def __init__(self, thread_num, top,
                 host='localhost', port=12000):
        self.host = host
        self.port = port
        self.thread_num = thread_num
        self.top = top
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_.bind((self.host, self.port))
        self.lock = Lock()
        self.url_counter = 0
        self.log_(f'init server with {self.thread_num} workers and counting top {self.top} words')

    def handle_connection(self, client, address):
        data = b''
        while True:
            chunk = client.recv(self.BUFFER_SIZE)
            data += chunk
            if len(chunk) < self.BUFFER_SIZE:
                break
        if data:
            url = data.decode('utf-8')
            raw_html = requests.get(url).text
            response = (parse(url, raw_html, self.top) + '\n').encode('utf-8')
            client.send(response)
            with self.lock:
                self.url_counter += 1
                self.log_(f'{self.url_counter} urls parsed at the moment')

    def run(self):
        self.url_counter = 0
        self.socket_.listen()
        self.log_(f'started listening {self.host}:{self.port}')
        with ThreadPoolExecutor(max_workers=self.thread_num) as thread_pool:
            while True:
                client, address = self.socket_.accept()
                thread_pool.submit(self.handle_connection, client, address)

    @staticmethod
    def log_(text):
        print(f"{time.ctime()}: {text}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=int, default=10)
    parser.add_argument('-k', type=int, default=5)
    args = parser.parse_args()

    server = Server(thread_num=args.w, top=args.k)
    server.run()
