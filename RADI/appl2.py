import http.server
import random

class RequestHandler(http.server.SimpleHTTPRequestHandler):

    
    opcije = ["isNotSub","isNotSub","isSub","isNotSub"]


    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type','text-html')
        self.end_headers()
        strana=open('index.html','rb')
        self.wfile.write(strana.read())
        self.wfile.write(f'<body><h1>Submarine Game 1.0</h1><div class="container">'.encode('utf-8'))
        for i in range(10):
            self.wfile.write(f'<div class="row"><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div></div>'.encode('utf-8'))

        self.wfile.write('<script>var isSub =document.querySelectorAll(".isSub");var isNot = document.querySelectorAll(".isNotSub");isSub.forEach(polje=>{polje.addEventListener("click",function(){polje.classList.add("hit");})});isNot.forEach(polje=>{polje.addEventListener("click",function(){polje.classList.add("miss")})});</script></body></html>'.encode('utf-8'))
        
        

server= http.server.HTTPServer(('localhost',80),RequestHandler)
server.serve_forever()