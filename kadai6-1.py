import requests
import json

# エンドポイント：https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData

API_KEY = "68755d6e047132dbfd283e8875b20670929196be"

STATS_DATA_ID = "0000020201"

url = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"
params = {
    "appId": API_KEY,
    "statsDataId": STATS_DATA_ID,
    "lang": "J"  
}


response = requests.get(url, params=params)
data = response.json()

if data["GET_STATS_DATA"]["RESULT"]["STATUS"] == 0:
    print("データ取得成功！\n")

    stat_info = data["GET_STATS_DATA"]["STATISTICAL_DATA"]["TABLE_INF"]
    print("統計名：", stat_info["STAT_NAME"]["@title"])
    print("調査年月：", stat_info["SURVEY_DATE"])
    print("\n--- 一部データ（学校数等） ---")
    values = data["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"]
    for item in values[:10]: 
        category = item["@cat01"]
        area = item["@area"]
        time = item["@time"]
        value = item["$"]
        print(f"区分: {category}, 地域コード: {area}, 時期: {time}, 値: {value}")
else:
    print("データ取得に失敗しました。")
    print("エラーコード:", data["GET_STATS_DATA"]["RESULT"]["STATUS"])
    print("メッセージ:", data["GET_STATS_DATA"]["RESULT"]["ERROR_MSG"])
