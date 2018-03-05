import scrapy
from mySpider.items import ItcastItem
#创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    #爬虫名
    name = "itcast"
    #允许爬虫作用的范围 域
    allowd_domains = ["http://www.itcast.cn/"]
    #爬虫起始的url
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]


    def parse(self, response):

        item = ItcastItem()
        # with open("teacher.html", "wb+") as f:
        #     f.write(response.body)

        # extract将匹配出来的结果转换为Unicode字符串

        #匹配所有老师的根结点列表集合
        teacher_list = response.xpath('//div[@class="li_txt"]')
        teacherItem = []
        for each in teacher_list:
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()

            item['name'] =name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            print(item['name'])

            teacherItem.append(item)

        return teacherItem