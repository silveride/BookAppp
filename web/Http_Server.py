# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:51:33 2017

@author: mmathew
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
#import SocketServer

from Storage import DynamoIntr

class S(BaseHTTPRequestHandler):
        
    def __init__(self, *args, **kwargs):
        # super(S, self).__init( *args, **kwargs)
        self.db = DynamoIntr()
        self.db.open()
        self.db.initTable()
        
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        print("get called...")
        self.wfile.write(bytes("<html><body><h1>hi!</h1></body></html>",'utf8'))

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        # Doesn't do anything with posted data
        print("post called..")
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        # parse the message and post
        (key,val) = self.parse(post_data.decode('utf-8'))
        print("Inserting valued to dynamo")
        self.db.set(key,val)
        self._set_headers()
        self.wfile.write(bytes("<html><body><h1>POST!</h1><pre>" + post_data.decode('utf-8') + "</pre></body></html>",'utf8'))
        
    def parse(self, data):
        return tuple(data.split('&'))
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()