import requests
import json

# データ種別：労働力調査（詳細集計）
# エンドポイント：https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData

appId = "68755d6e047132dbfd283e8875b20670929196be"
# ここに自分のAPIキーを入れる。私の場合は「68755d6e047132dbfd283e8875b20670929196be」なのでここにそれを入力する。

STATS_DATA_ID = "0003420201"

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
    print("統計表名:", stat_info["STAT_NAME"]["@title"])
    print("調査年月:", stat_info["SURVEY_DATE"])

    print("\n--- データの一部 ---")
    values = data["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"]
    for item in values[:5]:
        print(f"コード: {item['@cat01']}, 値: {item['$']}")
else:
    print("データ取得に失敗しました。")
    print("エラーコード:", data["GET_STATS_DATA"]["RESULT"]["STATUS"])
    print("メッセージ:", data["GET_STATS_DATA"]["RESULT"]["ERROR_MSG"])
