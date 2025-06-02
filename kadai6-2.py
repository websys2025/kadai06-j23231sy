#エンドポイント： https://archive-api.open-meteo.com/v1/archive

import requests
import json

url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": 35.6895,
    "longitude": 139.6917,
    "start_date": "2024-05-01",
    "end_date": "2024-05-03",
    "daily": "temperature_2m_max",
    "timezone": "Asia/Tokyo"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("=== 東京の日別最高気温（2024年5月1日～3日） ===")
    for date, temp in zip(data["daily"]["time"], data["daily"]["temperature_2m_max"]):
        print(f"{date}: {temp}°C")
else:
    print("データ取得に失敗しました。ステータスコード：", response.status_code)
