import subprocess
child1=subprocess.Popen(['ls','-l'],stdout=subprocess.PIPE)
child2=subprocess.Popen(["wc"],stdin=child1.stdout,stdout=subprocess.PIPE)
out=child2.communicate()
print(out)
