# -*- coding: utf-8 -*-


from http.server import BaseHTTPRequestHandler, HTTPServer
#import SocketServer
from urllib.parse import urlparse
from Storage import PostGresDBInterface

class BookWebServer(BaseHTTPRequestHandler):
        
    def __init__(self, *args, **kwargs):
        print ("BookWebServer: Server Started")
        
        
    def setupHeaders(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print("BookWebServer: Get received")
        custName = getCustomerNameFromURL()
        entries = getCustNameEntriesFromDB(custName)
        customerInfo = transformCustomerInfoAsText(entries)        
        self.setupHeaders()
        self.wfile.write(bytes("<html><body>"+customerInfo+"</body></html>",'utf8'))
        
        
    def getCustomerNameFromURL(self):
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        return query_components["name"]
        
    def getCustNameEntresFromDB(self,custName):
        dbInterface = PostGresIntr()
        db.StartInterface()
        statement = 'SELECT * from CUSTOMER WHERE FIRST_NAME = {}'.format(custName)
        db.executeStatement(statement)
        return db.fetchResult()
        
    def transformCustomerInfoAsText(self, entries):
        text = ""
        for entry in entries:
            for element in entry:
                text = text+str(element)+','
            text = text + '\n'
        return text
        
#Test part. start the server
def runServer(server_class=HTTPServer, handler_class=BookWebServer, port=80):
    try:
        server_address = ('', port)
        httpd_server = server_class(server_address, handler_class)
        print ('Starting httpd...')
        httpd_server.serve_forever()
    except KeyboardInterrupt:
        print ("Received Keyboard Interrupt")
        httpd_server.socket.close()
        
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        runServer(port=int(argv[1]))
    else:
        runServer()