
import scrapy


class DemosSpider(scrapy.Spider):
    name = "demos"
    start_urls = [
        "https://www.demos.jp/",
    ]

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f"demo-{page}.html"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")

        for demo in response.css("div.demos-section"):
          yield{
                'title': demo.css("p.title::text").getall(),
                'date' : demo.css("span[1].info::text").getall(),
                "detail_url": demo.css("a::attr(href)").getall()
                }
                # デバッグメッセージを追加
          self.logger.info(f"Title: {title}, Date: {date}, Location: {location}")
                # if product_details_url is None:
                #     return
                # else:
        next_page = demo.css('a.show-more-btn::attr(href)').get()
        if next_page is not None:
          next_page = response.urljoin(next_page)
          yield scrapy.Request(next_page, callback=self.parse)
