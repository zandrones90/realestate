import scrapy
from .. import items
from ..items import TutorialItem


class ImmobiliareSpider(scrapy.Spider):
    name = "immobiliare"
    page_number = 2
    start_urls = [
        'https://www.immobiliare.it/vendita-case/arezzo-provincia/?criterio=rilevanza&pag=1',
    ]

    def parse(self, response):

        items = TutorialItem()
        all_li = response.css("div.listing-item_body")

        for immobiliare in all_li:
            title = immobiliare.css('a::text').extract()
            price = immobiliare.css('li.lif__pricing::text').extract()
            link = immobiliare.css('a::attr(href)').extract()
            text = immobiliare.css('.descrizione__truncate::text').extract()
            price = numero(str(price))
            if price != -1 and price <= 150000:

                title = subs(str(title))
                items['text'] = text
                items['price'] = price
                items['title'] = title
                items['link'] = link
                yield items  # mi vieve sempre stampato prima price e poi title

        next_page = 'https://www.immobiliare.it/vendita-case/arezzo-provincia/?criterio=rilevanza&pag=' + str(ImmobiliareSpider.page_number)
        if ImmobiliareSpider.page_number< '''insrisci a mano il numero delle pagina''':
            ImmobiliareSpider.page_number += 1
            print(ImmobiliareSpider.page_number)
            yield response.follow(next_page, callback=self.parse)


def subs(nome):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Z',
                'K', 'J', 'W']
    # alphabet1 = ['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','z','k','j','w', ',']
    for i, n in enumerate(nome):
        if n in alphabet:
            init = i
            break
    nome = nome[init:]
    for i, n in enumerate(nome):
        if n == '\\':
            fine = i
            break
    nome = nome[:fine]
    return nome


def numero(num):
    init = -1
    for i, n in enumerate(num):
        if n == '€':
            init = i + 1
            break
    if init == -1:
        return init
    num = num[init:]
    for i, n in enumerate(num):
        if n == '\\' or n== "'" or n == ']':
            fine = i
            break
    num = num[:fine].replace(".", "")
    num = int(num)
    return num
'''
#nel caso non ci fossero link in cui cercare
def __init__(self,filename=None, *args, **kwargs):
    super(SpiderBot, self).__init__(+args, **kwargs)
    
    self.start_url = search_urls_from_file(filename) if filename else[]
    
    filename = è una file txt
    '''
