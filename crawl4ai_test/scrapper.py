# import asyncio
# from crawl4ai import AsyncWebCrawler


# async def main():
#     async with AsyncWebCrawler(verbose=True) as crawler:
#         result = await crawler.arun(url="https://www.nbcnews.com/business")
#         print(f"Basic crawl result: {result.markdown[:500]}")  # Print first 500 characters

# asyncio.run(main())


import json
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def extract_structured_data_using_css_extractor():
    print("\n--- Using JsonCssExtractionStrategy for Fast Structured Output ---")

    # Define the extraction schema
    schema = {
        "name": "Coinbase Crypto Prices",
        "baseSelector": ".cds-tableRow-t45thuk",
        "fields": [
            {
                "name": "crypto",
                "selector": "td:nth-child(1) h2",
                "type": "text",
            },
            {
                "name": "symbol",
                "selector": "td:nth-child(1) p",
                "type": "text",
            },
            {
                "name": "price",
                "selector": "td:nth-child(2)",
                "type": "text",
            }
        ],
    }

    # Create the extraction strategy
    extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)

    # Use the AsyncWebCrawler with the extraction strategy
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://www.coinbase.com/explore",
            extraction_strategy=extraction_strategy,
            bypass_cache=True,
        )

        assert result.success, "Failed to crawl the page"

        # Parse the extracted content
        crypto_prices = json.loads(result.extracted_content)
        print(f"Successfully extracted {len(crypto_prices)} cryptocurrency prices")
        print(json.dumps(crypto_prices, indent=2))

    return crypto_prices

# Run the async function
asyncio.run(extract_structured_data_using_css_extractor())
