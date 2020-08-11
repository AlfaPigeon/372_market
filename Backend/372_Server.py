from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from http.cookies import SimpleCookie
from pg import DB
import urllib.parse

WhiteList_GET = ['/', '/index', '/login', '/sale', '/search', '/profile', '/register', '/shop', '/profile_edit',
                 '/css/index.css', '/css/test.css', '/css/login.css']
WhiteList_POST = ['/api/login', '/api/edit_profile']

nologin = ['/login', '/register', '/css/index.css',
           '/css/test.css', '/css/login.css', '/api/login']
db = None


class requestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.cookies = SimpleCookie(self.headers.get('Cookie'))
        print(self.cookies)
        try:
            print(self.cookies["id"])
            self.userid = self.cookies['id'].value
        except:
            path = self.path.split("?")[0]
            if(path not in nologin):
                self.send_response(404)
                return

        try:
            self.username = db.query(
                "Select username From login where id=\'"+str(self.userid)+" \'")[0][0]
        except:
            self.username = "username"

        # check id with data base

        if(self.path.split("?")[0] not in WhiteList_GET):
            self.send_response(404)
            self.end_headers()
            return

        page = self.GET_API().replace("@username", self.username)

        self.wfile.write(bytes(page, 'utf-8'))

    def do_POST(self):
        self.cookies = SimpleCookie(self.headers.get('Cookie'))
        try:
            print(self.cookies["id"])
            self.userid = self.cookies['id'].value
        except:
            path = self.path.split("?")[0]
            if(path not in nologin):
                self.send_response(404)
                return

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
        elif(self.path == "/profile"):
            return self.profile_GET(str(self.userid))
        elif(self.path.split("?user=")[0] == "/profile"):
            return self.profile_GET(self.path.split("?user=")[1])
        elif(self.path.split("?shop=")[0] == "/shop"):
            return self.shop_GET(self.path.split("?shop=")[1])
        elif(self.path == "/profile_edit"):
            return self.profile_edit_GET()
    
    def POST_API(self):
        if(self.path == '/api/login'):
            return self.login_form_POST()
        elif(self.path == '/api/edit_profile'):
            return self.profile_edit_form_POST()

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

    def profile_edit_GET(self):
        try:
            layout = open("Frontend/Layout.html").read()
            page = open("Frontend/profile_edit.html").read()
            page = layout.replace("@content", page).replace("@title", "Profile edit")
            self.send_response(200)
        except:
            page = "<b>"+"No page here! 404"+"</b>"
            self.send_response(404)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        return page
        
    def profile_GET(self, id):


        try:
            seller_username = db.query("SELECT username from public.\"login\" where id=\'"+id+"\'")[0][0]
        except:
            seller_username = ""

        try:
            name = db.query("SELECT isim FROM public.\"KULLANICI\" where id=\'"+id+"\'")[0][0]
        except:
            name = ""

        try:
            surname = db.query("SELECT soyisim from public.\"KULLANICI\" where id=\'"+id+"\'")[0][0]
        except:
            surname = ""
        
        try:
            emails = ""
            email_results = db.query("SELECT email from public.\"kullanıcı_email\" where id=\'"+id+"\'").getresult()
            for email in email_results:
                emails += email[0] +" ; "
        except:
            emails = ""

        try:
            phones = ""
            phone_results = db.query("SELECT phone from public.\"kullanıcı_telefon\" where id=\'"+id+"\'").getresult()
            for phone in phone_results:
                phones += phone[0] +" ; "
        except:
            phones = ""

        try:
            addresses = ""
            address_results = db.query("SELECT address from public.\"kullanıcı_adres\" where id=\'"+id+"\'").getresult()
            for address in address_results:
                addresses += address[0] +" ; "
        except:
            addresses = ""


        try:
            image = db.query("SELECT image from public.\"KULLANICI\" where id=\'"+id+"\'")[0][0]
        except:
            image = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/User_font_awesome.svg/1200px-User_font_awesome.svg.png"


        try:

            # api here use post gre sql to return values
            # ?id=
            layout = open("Frontend/Layout.html").read()
            page = open("Frontend/profil.html").read()
            page = layout.replace("@content", page).replace("@title", str(seller_username)).replace("@seller_username",str(seller_username)).replace("@surname",str(surname)).replace("@name",str(name)).replace("@email",str(emails)).replace("@phone",str(phones)).replace("@adres",str(addresses)).replace("@image",str(image))
            self.send_response(200)
        except:
            page = "<b>"+"No page here! 404"+"</b>"
            self.send_response(404)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        return page

    def shop_GET(self, id):

        if(id == str(self.userid)):
            print("tihs is us")

        try:

            # api here use post gre sql to return values
            # ?id=

            layout = open("Frontend/Layout.html").read()
            page = open("Frontend/shop.html").read()
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
            results = db.query("SELECT * FROM public.\"URUN\" WHERE isim LIKE \'%"+urllib.parse.unquote_plus(search)+"%\' ").getresult()
            for result in results:
                print(result)
                product_name = result[1]
                product_id = result[0]
                product_image = result[5] 
                product_price = str(int(result[4]))+" TL"
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
        self.cookies = SimpleCookie(self.headers.get('Cookie'))
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')


        username = body.split("&")[0].split("=")[1]
        passwd = body.split("&")[1].split("=")[1]

        try:
            self.userid = db.query("Select id From public.\"login\" Where username=\'" + username+"\' and password=\'"+passwd+"\'")[0]
        except:
            self.send_response(301)
            self.send_header('Location', '/login')
            self.end_headers()
            return False

        self.userid = int(self.userid[0])

        self.cookies["id"] = self.userid
        self.cookies["id"]['path'] = "/"

        self.send_response(301)
        self.send_header('Location', '/')

        for morsel in self.cookies.values():
            self.send_header("Set-Cookie", morsel.OutputString())
        self.end_headers()

        self.wfile.write(bytes("ok", 'utf-8'))

        return True

    def profile_edit_form_POST(self):
        self.cookies = SimpleCookie(self.headers.get('Cookie'))
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')

        json = {body.split("&")[k].split("=")[0]:urllib.parse.unquote_plus(body.split("&")[k].split("=")[1]) for k in range(len(body.split("&")))}

        print(json)

        try:
            db.query("UPDATE public.\"KULLANICI\" SET isim=\'"+json['name']+"\', soyisim=\'"+json['surname']+"\', image=\'"+json['image']+"\' WHERE id=\'"+str(self.userid)+"\'")

  
            db.query("DELETE FROM public.\"kullanıcı_telefon\" WHERE id=\'"+str(self.userid)+"\'")

            db.query("DELETE FROM public.\"kullanıcı_email\" WHERE id=\'"+str(self.userid)+"\'")

            db.query("DELETE FROM public.\"kullanıcı_adres\" WHERE id=\'"+str(self.userid)+"\'")


            for mail in json['email'].split(";"):
                db.query("INSERT INTO public.\"kullanıcı_email\"(id, email) VALUES (\'"+str(self.userid)+"\', \'"+mail+"\')")
            for phone in json['phone'].split(";"):
                db.query("INSERT INTO public.\"kullanıcı_telefon\"(id, phone) VALUES (\'"+str(self.userid)+"\', \'"+phone+"\')")
            for address in json['address'].split(";"):
                db.query("INSERT INTO public.\"kullanıcı_adres\"(id, address) VALUES (\'"+str(self.userid)+"\', \'"+address+"\')")
                
        except:
            self.send_response(301)
            self.send_header('Location', '/profile_edit')
            self.end_headers()
            return False

        self.send_response(301)
        self.send_header('Location', '/profile')
        self.end_headers()

        self.wfile.write(bytes("ok", 'utf-8'))

        return True

def main():
    address = ('localhost', 8080)
    server = HTTPServer(address, requestHandler)
    server.serve_forever()


if __name__ == "__main__":
    db = DB(dbname='372_market', host='localhost',
            port=5432, user='postgres', passwd='123')
    main()
