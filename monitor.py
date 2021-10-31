import os
import subprocess 

res = subprocess.run(["cat", "/sys/class/thermal/thermal_zone0/temp"], stdout=subprocess.PIPE)
print(res)
if res.returncode == 0:
    print("OK")
    str = res.stdout.decode() #byte列 -> 文字列
    temp = int(str)/1000 #文字列 -> int -> div by 1000で温度に変換
    
else:
    print("NG")
    os.Exit(1)

