# TikTok Shop GMV Analyzer — Python SDK

Python client for the [TikTok Shop GMV Analyzer Apify Actor](https://apify.com/apivault_labs/tiktok-shop-seller-product-creator-gmv-analyzer). Send public Actor inputs, wait for the hosted run, and receive clean Dataset rows without maintaining scraping infrastructure.

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-blue)](https://apify.com/apivault_labs/tiktok-shop-seller-product-creator-gmv-analyzer)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Results

- Seller, product, niche and creator modes
- GMV and profit ranges
- Creator contribution signals
- Product opportunity scoring

The Actor uses public marketplace signals and returns estimates or ranges where a platform does not publish exact figures.

## Install

```bash
pip install git+https://github.com/apivault-labs/tiktok-shop-gmv-analyzer-python.git
```

Create an Apify token at [Console → Integrations](https://console.apify.com/account/integrations), then:

```python
from tiktok_shop_gmv_analyzer import TikTokShopGmvAnalyzerClient

client = TikTokShopGmvAnalyzerClient(api_token="apify_api_xxxxxx")
rows = client.run({'mode': 'keyword', 'searchQueries': ['skincare'], 'maxItems': 20})
print(rows[0] if rows else "No results")
```

You can set `APIFY_API_TOKEN` instead of passing the token in code.

## Public input options

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | `string` | `keyword` | Choose whether to research product keywords, seller portfolios, individual products, or creator contribution. |
| `searchQueries` | `array` | `—` | Keywords used in Keyword mode and to discover public creator-product relationships in Creator mode. |
| `sellerUrls` | `array` | `—` | Public TikTok Shop store URLs or numeric seller IDs used in Seller mode. |
| `productUrls` | `array` | `—` | Public TikTok Shop PDP links used in Product mode. |
| `productIds` | `array` | `—` | Numeric product IDs used in Product mode. |
| `creatorIds` | `array` | `—` | In Creator mode, return only matching public creator IDs or names. Leave empty to rank every creator discovered for the supplied keywords. |
| `maxItems` | `integer` | `30` | Hard limit for unique products scanned or returned. Set this before a large run to control cost. |
| `maxConcurrency` | `integer` | `4` | Parallel product processing. The default balances speed and reliability. |
| `timeoutSeconds` | `integer` | `35` | Maximum time allowed for one public page request. |
| `costOfGoodsPercent` | `number` | `30` | Your estimated sourcing cost as a percentage of sale price. |
| `platformFeePercent` | `number` | `6` | Assumed TikTok Shop marketplace and transaction fees. |
| `creatorCommissionPercent` | `number` | `10` | Assumed affiliate creator commission per attributed order. |
| `advertisingPercent` | `number` | `10` | Estimated paid-media cost as a percentage of product revenue. |
| `refundRatePercent` | `number` | `2` | Estimated returns and refunds allowance. |
| `shippingCostPerOrder` | `number` | `0` | Seller-paid fulfillment and shipping cost per unit in USD. |

The complete, versioned schema is also available on the [Actor page](https://apify.com/apivault_labs/tiktok-shop-seller-product-creator-gmv-analyzer).

## Pricing

Pay per delivered result through Apify, starting around **$5/1,000 results** on paid tiers. Free-plan pricing and platform usage can differ; check the Actor page before large runs.

## Examples

- `examples/quickstart.py` — first run
- `examples/bulk_analysis.py` — expand a target list
- `examples/export_csv.py` — save flat result fields
- `examples/save_json.py` — preserve nested output
- `examples/cost_estimate.py` — estimate result-event charges
- `examples/environment_token.py` — keep credentials out of code

## Architecture and privacy

This repository is intentionally a thin API client. Collection, retries, analysis and billing run inside the hosted Apify Actor. No private implementation, credentials, scoring weights or infrastructure configuration are included.

## License

MIT. The hosted Actor is a separate paid service governed by Apify terms.
