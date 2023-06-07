

import socket

#Function to scan a specfic target for open ports
def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass

# get the targets and ports from the user.
targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

#check if multiple targets are provided by user
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
