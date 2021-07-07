import subprocess
import sys
import os

# total arguments
if(len(sys.argv) != 2 ):
	print("[*] Invalid Command")
	print('[*] Sample:\r\npython3 nmapLoop.py "nmap -p- -A -T4 192.168.1.2"')
	exit()
timer = 0
while(1):
	timer = timer + 1
	cmd = sys.argv[1].split()
	returned_value = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = returned_value.communicate()
	print("-"*10)
	os.system("clear")
	print("[*] Scan:", timer)
	print(out.decode("utf-8"))
