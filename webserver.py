from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
      <title>My webserver</title>
   </head>
   <body bgcolor="#FFB6C1">
      <h2>
      Top 5 Revenue Generating Companies
      <h2>
      <h3>
         <ol type="1" font-size>
            <LI> Microsoft Corp : $203.08 billion</LI>
            <LI> Oracle Corp : $46.07 billion</LI>
            <LI> SAP SE (SAP) : $32.97 billion</LI>
            <LI> Salesforce, Inc. : $30.29 billion </LI>
            <LI> Adobe Inc. : $17.61 billion </LI>
         </ol>
      </h3>
   </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8080)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()