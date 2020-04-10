import schedule
import time
import json
import requests

PATH_STAGEDATA = './stage_data.json'
HEADERS = {'User-Agent': 'ここにbot名と連絡先(twitterIDなど)を書いてね'}
SCHEDULE_URL = 'https://spla2.yuu26.com/schedule'

def getJson():
    r = requests.get(SCHEDULE_URL, headers=HEADERS)
    stage_data = r.json()
    with open(PATH_STAGEDATA, 'w') as f:
        json.dump(stage_data, f, ensure_ascii=False, indent=2)
        print('ステージ情報を更新しました')

schedule.every().day.at("01:01").do(getJson)
schedule.every().day.at("03:01").do(getJson)
schedule.every().day.at("05:01").do(getJson)
schedule.every().day.at("07:01").do(getJson)
schedule.every().day.at("09:01").do(getJson)
schedule.every().day.at("11:01").do(getJson)
schedule.every().day.at("13:01").do(getJson)
schedule.every().day.at("15:01").do(getJson)
schedule.every().day.at("17:01").do(getJson)
schedule.every().day.at("19:01").do(getJson)
schedule.every().day.at("21:01").do(getJson)
schedule.every().day.at("23:01").do(getJson)

while True:
    schedule.run_pending()
    time.sleep(1)
