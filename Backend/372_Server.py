from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
WhiteList_GET = ['/', '/index', '/login', '/sale', '/search', '/profile',
                 '/css/index.css', '/css/test.css', '/css/login.css']
WhiteList_POST = ['/api/login']


class requestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if(self.path.split("?")[0] not in WhiteList_GET):
            self.send_response(404)
            self.end_headers()
            return

        page = self.GET_API()

        self.wfile.write(bytes(page, 'utf-8'))

    def do_POST(self):

        if(self.path not in WhiteList_POST):
            self.send_response(404)
            self.end_headers()
            return
        self.POST_API()

    def GET_API(self):
        if(self.path.split("/")[1] == "css"):
            return self.css_GET()
        elif(self.path.split("/")[1] == "js"):
            return self.js_GET()
        elif(self.path == "/" or self.path == "/index"):
            return self.index_GET()
        elif(self.path == "/login"):
            return self.login_GET()
        elif(self.path.split("?id=")[0] == "/sale"):
            return self.sale_GET(self.path.split("?id=")[1])
        elif(self.path.split("?search=")[0] == "/search"):
            return self.search_GET(self.path.split("?search=")[1])
        elif(self.path.split("?user=")[0] == "/profile"):
            return self.profile_GET(self.path.split("?user=")[1])

    def POST_API(self):
        if(self.path == '/api/login'):
            return self.login_form_POST()

    def index_GET(self):
        try:
            layout = open("Frontend/Layout.html").read()
            page = open("Frontend/index.html").read()
            page = layout.replace(
                "@content", page).replace("@title", "Main Page")
            self.send_response(200)
        except:
            page = "<b>"+"No page here! 404"+"</b>"
            self.send_response(404)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        return page

    def login_GET(self):
        try:
            page = open("Frontend/login.html").read()
            self.send_response(200)
        except:
            page = "<b>"+"No page here! 404"+"</b>"
            self.send_response(404)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        return page

    def sale_GET(self, id):
        try:

            # api here use post gre sql to return values
            # ?id=

            layout = open("Frontend/Layout.html").read()
            page = open("Frontend/sale.html").read()
            page = layout.replace(
                "@content", page).replace("@title", "Product Name")
            self.send_response(200)
        except:
            page = "<b>"+"No page here! 404"+"</b>"
            self.send_response(404)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        return page

    def profile_GET(self, id):
        try:

            # api here use post gre sql to return values
            # ?id=

            layout = open("Frontend/Layout.html").read()
            page = open("Frontend/profil.html").read()
            page = layout.replace(
                "@content", page).replace("@title", "Product Name")
            self.send_response(200)
        except:
            page = "<b>"+"No page here! 404"+"</b>"
            self.send_response(404)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        return page

    def search_GET(self, search):
        try:

            # api here use post gre sql to return values
            # ?search=

            layout = open("Frontend/Layout.html").read()
            page = open("Frontend/search.html").read()
            item = open("Frontend/prefab/search_item").read()
            bookmark = "Nothing Found!"
            for _ in range(100):
                product_name = "GOLDMASTER CR1-X7 Bluetooth Fm Transmitter 2020 MODEL"
                product_id = "11111"
                product_image = "https://images-na.ssl-images-amazon.com/images/I/71vKyimxsiL._UL1500_.jpg"
                product_price = "100 TL"
                _item = item.replace("@product_name", product_name).replace("@product_id", product_id).replace(
                    "@product_image", product_image).replace("@product_price", product_price)
                page = page.replace(bookmark, bookmark + _item)
            page = page.replace(bookmark, "")
            page = layout.replace("@content", page).replace("@title", search)
            self.send_response(200)
        except:
            page = "<b>"+"No page here! 404"+"</b>"
            self.send_response(404)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        return page

    def css_GET(self):
        try:
            page = open("Frontend"+self.path).read()
            self.send_response(200)
        except:
            page = "<b>"+"No css here! 404"+"</b>"
            self.send_response(404)
        self.send_header('content-type', 'text/css')
        self.end_headers()
        return page

    def js_GET(self):
        try:
            page = open("Frontend"+self.path).read()
            self.send_response(200)
        except:
            page = "<b>"+"No js here! 404"+"</b>"
            self.send_response(404)
        self.end_headers()
        return page

    def login_form_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        print(body)

        self.send_response(301)
        if(body.split("&")[1].split("=")[1] == "123"):
            self.send_header('Location', '/')
        else:
            self.send_header('Location', '/login')

        self.end_headers()
        self.wfile.write(bytes("ok", 'utf-8'))
        return True


def main():
    address = ('localhost', 8080)
    server = HTTPServer(address, requestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
