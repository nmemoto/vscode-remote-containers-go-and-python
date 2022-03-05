# %%
import pandas as pd
import requests
import io

# %%
# https://cio.go.jp/policy-opendata
# オープンデータ取組済自治体一覧（令和４年１月12日時点）　CSV（都道府県）より
url = "https://cio.go.jp/sites/default/files/uploads/documents/digital/opendata_lg_pref_list_20220112.csv"
content = requests.get(url).content
df = pd.read_csv(io.BytesIO(content), encoding="SHIFT-JIS")
