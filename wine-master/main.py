from http.server import HTTPServer, SimpleHTTPRequestHandler

print(11234532234)
server = HTTPServer(('0.0.0.0', 8002), SimpleHTTPRequestHandler)
server.serve_forever()
