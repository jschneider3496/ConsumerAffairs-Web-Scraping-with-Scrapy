import scrapy
from ..items import ConsumeraffairsItem


class UberSpider(scrapy.Spider):
    name = "uber_ca"

    def start_requests(self):
        urls = []
        for x in range(0, 58):
            url = 'https://www.consumeraffairs.com/travel/uber.html?page=' + str(x) + '#sort=recent&filter=none'
            urls.append(url)
        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = ConsumeraffairsItem()

        # whole_reviews = response.xpath('//div[@class= "rvw js-rvw"]')

        date = response.xpath('//div[@class= "rvw js-rvw"]/div[3]/span/text()').extract()
        stars = response.xpath('//div[@class= "rvw js-rvw"]/div[1]/div/img/@data-rating').extract()
        comment = response.xpath('//div[@class= "rvw js-rvw"]/div[3]/p[2]/text()').extract()
        result = zip(date, stars, comment)
        for date, stars, comment in result:
            items['date'] = date
            items['stars'] = stars
            items['comment'] = comment
            yield items

            # with open('reviews.txt', 'w') as f:
            #     for u in comment:
            #         f.write("Comment: " + u + "\n")
            #     for u in stars:
            #         f.write("Stars: " + u + "\n")
            #     for u in date:
            #         f.write("Date: " + u + "\n")


# items = dict()
