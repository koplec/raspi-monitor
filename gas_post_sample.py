import json
import requests
import datetime

from settings import *

print(GAS_URL)

try:
    now = datetime.datetime.now()
    time_stamp = now.strftime("%Y/%m/%d %H:%M:%S.%f")

    data = {
        "time-stamp" : time_stamp,
        "cpu-temp": 12.345
    }
    
    requests.post(GAS_URL, data=json.dumps(data), headers={"Content-Type": "application/json"})
except KeyboardInterrupt:
    sys.exit()
except requests.exceptions.ConnectionError:
    # 時々このエラーが発生するため追加
    print("Error, 送信失敗, %s" % data["time_stamp"])