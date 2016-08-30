import time

n = int(time.time()) %127
print(chr(n).upper(),"=",n)