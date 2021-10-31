import os
import subprocess 
import datetime
import json
import requests
import time

from settings import *


def do_monitor():
    res = subprocess.run(["cat", "/sys/class/thermal/thermal_zone0/temp"], stdout=subprocess.PIPE)
    print(res)
    if res.returncode == 0:
        print("OK")
        str = res.stdout.decode() #byte列 -> 文字列
        temp = int(str)/1000 #文字列 -> int -> div by 1000で温度に変換

        now = datetime.datetime.now()
        time_stamp = now.strftime("%Y/%m/%d %H:%M:%S.%f")


        data = {
            "time-stamp": time_stamp, "cpu-temp": temp
        }
        gas_post(data)
    else:
        print("NG")
        os.Exit(1)

def gas_post(data):
    try:
        requests.post(GAS_URL, data=json.dumps(data), headers={"Content-Type": "application/json"})
    except KeyboardInterrupt:
        sys.exit()
    except requests.exceptions.ConnectionError:
        # 時々このエラーが発生するため追加
        print("Error, 送信失敗, %s" % data["time_stamp"])


if __name__ == "__main__":
    print("BEGIN monitor")
    while True:
        do_monitor()
        print("sleep 60sec")
        time.sleep(60)
