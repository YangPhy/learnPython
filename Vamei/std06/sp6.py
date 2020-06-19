import subprocess
child=subprocess.Popen(["cat"],stdin=subprocess.PIPE)
child.communicate("py".encode())
