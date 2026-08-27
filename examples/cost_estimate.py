from tiktok_shop_gmv_analyzer import TikTokShopGmvAnalyzerClient

for count in (10, 100, 1000):
    print(count, TikTokShopGmvAnalyzerClient.estimate_cost(count), "USD estimated result charges")
