import http.server
import random

class RequestHandler(http.server.SimpleHTTPRequestHandler):
 
    opcije = ["isNotSub","isNotSub","isSub","isNotSub"] 

    def do_GET(self):  
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header('Content-type','text-html')
            self.end_headers()
            strana=open('index.html','rb') 
            content = "<div class='container'>"
            for i in range(10):
                content +='<div class="row">'
                for j in range(10):
                    content+=f"<div class='cube {random.choice(self.opcije)}'></div>"
                content +='</div>'
            content += "</div>"
            self.wfile.write(strana.read().decode("utf-8").replace("KONTEJNER",content).encode("utf-8"))
            print(content) 
        else:
            super().do_GET() 

server= http.server.HTTPServer(('localhost',8000),RequestHandler)
server.serve_forever()
