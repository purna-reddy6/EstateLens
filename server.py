
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler


socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving Realest prototype at http://localhost:{PORT}")
    print("Open this URL in your browser.")
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever()


