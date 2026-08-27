from tiktok_shop_gmv_analyzer import TikTokShopGmvAnalyzerClient

client = TikTokShopGmvAnalyzerClient()
rows = client.run({'mode': 'keyword', 'searchQueries': ['skincare'], 'maxItems': 20})
print(rows[0] if rows else "No results")
