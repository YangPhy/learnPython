import subprocess
rc1=subprocess.call(["ls","-l"])
rc2=subprocess.check_call(["ls","-l"])
rc3=subprocess.check_output(['ls','-l'])
