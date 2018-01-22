import scrapy

class TumblingSpiderClass(scrapy.Spider):

    name = "tumbling"

    start_urls=[
    'https://www.gymnasticbodies.com/forum/search/?&q=tumbling&type=forums_topic&item=29190&sortby=relevancy',
    ]


    def parse(self,response):

        threads =  response.xpath("//*[@class='ipsStreamItem ipsStreamItem_contentBlock ipsStreamItem_expanded ipsAreaBackground_reset ipsPad  ']")

        for thread in threads:

            # absolute link of the thread
            thread_absolute_link = thread.xpath(".//*[@data-linktype ='link']/@href").extract_first()

            # just follow the absolute link
            yield response.follow(thread_absolute_link,self.parse_thread)


    def parse_thread(self,response):

        comments =  response.xpath("//*[@class='cPost_contentWrap ipsPad']")
        title =  response.xpath("//*[@class='ipsType_break ipsContained']/span/text()").extract_first()
        category =  response.xpath("//*[@class='ipsType_normal']/span/a/text()").extract_first()

        for comment in comments :

            # comment content
            content = "".join(comment.xpath(".//*[@data-role='commentContent']/p/text()").extract())

            yield{
                "title": title,
                "content": content,
                "category": category
            }
