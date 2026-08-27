import json
from tiktok_shop_gmv_analyzer import TikTokShopGmvAnalyzerClient

rows = TikTokShopGmvAnalyzerClient().run({'mode': 'keyword', 'searchQueries': ['skincare'], 'maxItems': 20})
with open("results.json", "w", encoding="utf-8") as handle:
    json.dump(rows, handle, ensure_ascii=False, indent=2)
