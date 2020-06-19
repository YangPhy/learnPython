import subprocess
child=subprocess.Popen(["ping","-c","5","wwww.google.com"])
print("parent process")
