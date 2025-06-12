import requests
import json
# BODIK APIを使用
try:
# BODIK APIを呼び出す準備
    api_server = 'https://wapi.bodik.jp'
    apiname = 'aed'
    url = f'{api_server}/{apiname}'

    # BODIK APIを呼び出す
    response = requests.get(url, timeout=5.0)

    # APIの実行結果を確認する
    if response is not None and response.status_code == 200:
        # 結果をJSONで取得する
        data = response.json()

        # BODIK APIの検索結果を解析する
        if data is not None and 'resultsets' in data:
            resultsets = data['resultsets']
        if 'features' in resultsets:
            features = resultsets['features']
            for feature in features:
                properties = feature['properties']
                print(json.dumps(properties, indent=2, ensure_ascii=False))
        else:
            print('no features', resultsets)
    else:
        print('status_code', response)

except Exception as e:
    # 例外が発生
    print('Exception', e)