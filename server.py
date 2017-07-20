#!/usr/bin/env python
import logging
import os
import SimpleHTTPServer
import SocketServer
from StringIO import StringIO


PORT = int(os.getenv('PORT', '8000'))


class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        f = StringIO()
        f.write(self.headers)
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        encoding = 'utf-8'
        self.send_header('Content-type', 'text/text; charset=%s' % encoding)
        self.send_header('Content-Length', str(length))
        self.end_headers()
        self.copyfile(f, self.wfile)


if __name__ == '__main__':
    httpd = SocketServer.TCPServer(('', PORT), GetHandler)
    httpd.serve_forever()
