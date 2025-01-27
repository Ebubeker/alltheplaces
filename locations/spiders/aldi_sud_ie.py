from scrapy.spiders import SitemapSpider

from locations.structured_data_spider import StructuredDataSpider
from locations.user_agents import BROSWER_DEFAULT


class AldiSudIE(SitemapSpider, StructuredDataSpider):
    name = "aldi_sud_ie"
    item_attributes = {"brand": "ALDI", "brand_wikidata": "Q41171672", "country": "IE"}
    allowed_domains = ["aldi.ie"]
    download_delay = 10
    sitemap_urls = ["https://www.aldi.ie/sitemap/store-en_ie-eur"]
    sitemap_rules = [("", "parse_sd")]
    user_agent = BROSWER_DEFAULT
