from __future__ import print_function
import socket
import re
import subprocess
def getip():
        arpscan = subprocess.Popen(['arp-scan', '127.0.0.1', '-q'], stdout=subprocess.PIPE).communicate()[0]
        target = re.findall(b'((\d{1,3}\.){3}\d{1,3})', arpscan)[0][0]
        return(target)

target = getip()
print(target)
for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        payload = s.recv(1024)
        if 'FUKU' not in payload:
                print('\n[+] Port %s has a service running' % port)
                print(payload)
        else:
                print('.', end='')
        s.close()
