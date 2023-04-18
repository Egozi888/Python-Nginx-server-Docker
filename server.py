import http.server
import socketserver
import datetime

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            # Load the template
            with open('/usr/share/nginx/html/index.html', 'r') as f:
                content = f.read()
                # Get the current day of the week and date
                today = datetime.datetime.now().strftime("%A, %d %B %Y")
                # Replace placeholders in the template with actual values
                content = content.replace('[DAY_OF_WEEK]', today.split(',')[0])
                content = content.replace('[CURRENT_DATE]', today.split(',')[1].strip())
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(content, 'utf-8'))
        else:
            self.send_error(404)


# Set the port number that the server should listen on
PORT = 8080
Handler = MyHandler

# Create a TCP server instance on the specified port and pass requests to the MyHandler class
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server started on port", PORT)
    httpd.serve_forever()