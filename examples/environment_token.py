import os
from tiktok_shop_gmv_analyzer import TikTokShopGmvAnalyzerClient

if not os.environ.get("APIFY_API_TOKEN"):
    raise SystemExit("Set APIFY_API_TOKEN before running this example")
client = TikTokShopGmvAnalyzerClient()
print(client.run_one({'mode': 'keyword', 'searchQueries': ['skincare'], 'maxItems': 20}))
