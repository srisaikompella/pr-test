#!/usr/bin/env python3 
import subprocess
cmd ="ls -l"
data = subprocess.Popen([cmd], stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell=True)
stdout, stderr = data.communicate()
output_list = stdout.strip().decode("utf-8").split("\n")
[print(i) for i in output_list]

a = [1,2,3,4]
for i in a:
  if (i%2==0):
    print("prime::")
else: 
  print("not prime::")
