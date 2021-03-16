import scrapy
from ..items import Flipkart2Item


class FlipspideySpider(scrapy.Spider):
    name = 'flipspidey'
    nextpage = 2

    start_urls = ['https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.brand%255B%255D%3DSamsung&otracker=nmenu_sub_TVs+%26+Appliances_0_Samsung&page=1']

    def parse(self, response):

        myitems = Flipkart2Item()

        maindiv = response.css('._2kHMtA')
        footerdiv = response.css('._2MImiq')

        for mydata in maindiv:

            tvbrand = mydata.css('div._3pLy-c div._4rR01T').css('::text').extract()
            tvprice = mydata.css('div._25b18c div._30jeq3').css('::text').extract()
            tvimage = mydata.css('img._396cs4').css('img::attr(src)').extract()
            tvres = mydata.css('.rgWa7D:nth-child(3)::text').extract()
            tvwarranty = mydata.css('.rgWa7D:nth-child(8) , .rgWa7D:nth-child(7)').css('::text').extract()
            tvrating = mydata.css('._3LWZlK::text').extract()


            for pagenumber in footerdiv:
                pageno = pagenumber.css('._2Kfbh8::text').extract()


                myitems['product_type'] = 'television'
                myitems['product_name'] = tvbrand
                myitems['product_price'] = tvprice
                myitems['product_image'] = tvimage
                myitems['product_desc'] = tvres
                myitems['product_warranty'] = tvwarranty
                myitems['product_rating'] = tvrating
                myitems['page_number'] = pageno

                yield myitems

            next_page = 'https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.brand%255B%255D%3DSamsung&otracker=nmenu_sub_TVs+%26+Appliances_0_Samsung&page=' + str(FlipspideySpider.nextpage) + ''


            if FlipspideySpider.nextpage <6:
                FlipspideySpider.nextpage += 1

                yield response.follow(next_page,callback=self.parse)



