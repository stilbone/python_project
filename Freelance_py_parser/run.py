import http.server
import socketserver
import webbrowser

import habr_fl_descriptor
import freelance_descriptor


habr_fl_descriptor.main()
freelance_descriptor.main()


PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

webbrowser.open('http://localhost:8080/', new=2)
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
