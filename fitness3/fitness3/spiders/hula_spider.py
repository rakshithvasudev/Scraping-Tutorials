import scrapy

class HulaSpider(scrapy.Spider):

    name = "hula"

    start_urls =[
    'https://hawaiihulacompany.com/blog/',
    ]

    def parse(self,response):

        posts = response.xpath("//*[@class='post']")

        for post in posts:

            title =  post.xpath(".//*[@class='post-title']/h2/a/text()").extract_first()

            div_tags = post.xpath(".//div")

            entire_content = []

            # get the text of all the div tags
            for div_tag in div_tags:

                # get the div tag text
                div_tag_text = "".join(div_tag.xpath(".//text()").extract())

                # add it to the post content
                entire_content.append(div_tag_text)

            entire_content = "".join(entire_content)

            yield {

            "title": title,
            "content": entire_content

            }

        # pagination
        next_page_absolute_link = response.xpath("//*[@class='previous-entries']/a/@href").extract_first()

        if next_page_absolute_link is not None:
            yield response.follow(next_page_absolute_link,self.parse)
