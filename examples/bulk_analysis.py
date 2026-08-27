from tiktok_shop_gmv_analyzer import TikTokShopGmvAnalyzerClient

client = TikTokShopGmvAnalyzerClient()
payload = {'mode': 'keyword', 'searchQueries': ['skincare'], 'maxItems': 20}
# Add more targets or queries to the list fields supported by this Actor.
rows = client.run(payload)
print(f"Received {len(rows)} rows")
