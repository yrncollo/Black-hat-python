import subprocess

# result = subprocess.check_output(['ls', '-la'])
# result = result.decode("utf-8")
# print(result)

ip = input("Enter the IP: ")
"""
file = "initial"
nmap_command =[
        'nmap',
        '-sC',
        '-sV',
        '-oA',
        file,
        ip
        ]
nmap = subprocess.check_output(nmap_command)
nmap = nmap.decode("utf-8")
print(nmap)
"""


gobuster_command = [
    'gobuster',
    'dir',
    '-u',
    f'http://{ip}/',
    '-w',
    '/usr/share/SecLists/Discovery/Web-Content/common.txt'
]
gobuster = subprocess.check_output(gobuster_command)
gobuster = gobuster.decode("utf-8")
print(gobuster)
