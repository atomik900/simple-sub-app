import http.server
import random

class RequestHandler(http.server.SimpleHTTPRequestHandler):

    
    opcije = ["isNotSub","isNotSub","isSub","isNotSub"]


    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type','text-html')
        self.end_headers()
        strana=open('index.html','rb')
        self.wfile.write(f'<body><div class="container">'.encode('utf-8'))
        for i in range(10):
            self.wfile.write(f'<div class="row"><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div><div class="cube {random.choice(self.opcije)}"></div></div>'.encode('utf-8'))

        self.wfile.write('<script>var isSub = document.getElementsByClassName("isSub");var IsNot = document.getElementsByClassName("isNotSub");for (var i=0;i<isSub.length;i++){isSub[i].addEventListener("click",function(){isSub[i].classList.add("hit");})}for (var i=0;i<isSub.length;i++){isNot[i].addEventListener("click",function(){isNot[i].classList.add("miss");})}</script></body></html>'.encode('utf-8'))
        
        self.wfile.write(strana.read())

server= http.server.HTTPServer(('localhost',80),RequestHandler)
server.serve_forever()