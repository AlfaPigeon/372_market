from http.server import HTTPServer, BaseHTTPRequestHandler

WhiteList = ['/', '/index.html']


class requestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if(self.path not in WhiteList):
            self.send_response(403)
            self.end_headers()
            return

        if self.path == '/':
            self.path = '/index.html'
        try:
            page = open("../Frontend"+self.path).read()
            self.send_response(200)
        except:
            page = "<b>"+"No page here! 404"+"</b>"
            self.send_response(404)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes(page, 'utf-8'))

    def do_POST(self):
        self.send_header('content-type', 'text/html')
        self.end_headers()


def main():
    address = ('localhost', 8080)
    server = HTTPServer(address, requestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
