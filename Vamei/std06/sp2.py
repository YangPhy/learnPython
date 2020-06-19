import subprocess
out1=subprocess.call("ls -l",shell=True)
out2=subprocess.call("cd /home && ls",shell=True)
