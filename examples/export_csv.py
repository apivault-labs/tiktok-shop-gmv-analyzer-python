import csv
from tiktok_shop_gmv_analyzer import TikTokShopGmvAnalyzerClient

rows = TikTokShopGmvAnalyzerClient().run({'mode': 'keyword', 'searchQueries': ['skincare'], 'maxItems': 20})
if rows:
    scalar_keys = [k for k, v in rows[0].items() if not isinstance(v, (dict, list))]
    with open("results.csv", "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=scalar_keys)
        writer.writeheader()
        writer.writerows({k: row.get(k) for k in scalar_keys} for row in rows)
