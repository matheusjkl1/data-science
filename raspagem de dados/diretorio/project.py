import requests
from time import sleep
from parsel import Selector


def fetch(url):
    """Seu código deve vir aqui"""
    sleep(1)
    response = requests.get(url)
    status = response.status_code
    if not status == 200:
        return None
    return response.text


def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    # writer_class = ".tec--author__info p *::text"
    writer_class = ".z--font-bold *::text"
    writer_get = selector.css(writer_class).get()
    if not type(writer_get) == str:
        writer = writer_get
    else:
        writer = writer_get.strip()
    shares_selector = "#js-author-bar > nav > div:nth-child(1)::text"
    suffix = " Compartilharam"
    shares_get = selector.css(shares_selector).get()
    if not type(shares_get) == str:
        shares = 0
    else:
        shares = int(shares_get[:-len(suffix)])
    comments_selector = "#js-comments-btn::attr(data-count)"
    comments_get = selector.css(comments_selector).get(),
    if not type(comments_get[0]) == str:
        comments_count = comments_get[0]
    else:
        comments_count = int(comments_get[0])
    summary_selectior = ".tec--article__body > p:nth-child(1) *::text"
    summary = selector.css(summary_selectior).getall()
    summary_string = ''
    for item in summary:
        summary_string = summary_string + item
    sources_get = selector.css(".z--mb-16 > div a::text").getall()
    sources = [item.strip() for item in sources_get]
    categories_get = selector.css("#js-categories a::text").getall()
    categories = [item.strip() for item in categories_get]

    dictionary = {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("time::attr(datetime)").get(),
        "writer": writer,
        "shares_count": shares,
        "comments_count": comments_count,
        "summary": summary_string,
        "sources": sources,
        "categories": categories,
    }
    return dictionary
    # return "dictionary"


def scrape_novidades(html_content):
    selector = Selector(html_content)
    selector_class = ".tec--list__item .tec--card__title__link::attr(href)"
    news_list = selector.css(selector_class).getall()
    return news_list


def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    selector_class = "div.tec--list.tec--list--lg > a::attr(href)"
    next_page_url = selector.css(selector_class).get()
    return next_page_url


# def get_tech_news(amount):
#     """lista noticias na quatidade desejada"""
#     url = 'https://www.tecmundo.com.br/novidades'
#     notice_list = []
#     url_list = scrape_novidades(fetch(url))

#     while(len(url_list) < amount):
#         if(len(url_list) < amount):
#             url = scrape_next_page_link(fetch(url))
#             url_list.extend(scrape_novidades(fetch(url)))

#     for notice in url_list[0:amount]:
#         info = scrape_noticia(fetch(notice))
#         notice_list.append(info)

#     return notice_list

def get_tech_news(amount):
    news_per_page = 20
    fetch_url = fetch('https://www.tecmundo.com.br/novidades')
    fetch_next_page = scrape_next_page_link(fetch_url)
    fetch_news = scrape_novidades(fetch_url)
    pages = []
    count = 0
    next_page = False
    for link_count in range(amount):
        if (link_count >= news_per_page) and (next_page is False):
            print('entrei aqui')
            html_content = fetch(fetch_next_page)
            fetch_news = scrape_novidades(html_content)
            next_page = True
            count = 0
        html_notice_currence = fetch(fetch_news[count])
        notice = scrape_noticia(html_notice_currence)
        pages.append(notice)
        count += 1
    print(pages)
    return pages


list_of_dicts = [
  {
    '_id': '6170d287ea269bc96c6a6318', 'url': 'https://www.tecmundo.com.br/vamos.htm',
    'title': 'Vamoscomtudo', 'timestamp': '2020-11-23T11:00:01', 'writer': 'Leonardo', 'shares_count': 1,
    'comments_count': 1, 'summary': 'Sumario 2', 'sources': ['ResetEra'], 'categories': ['PC', 'Console']
  },
  {
    '_id': '6170d287ea269bc96c6a6318', 'url': 'https://www.tecmundo.com.br/vamos.htm',
    'title': 'Vamoscomtudo', 'timestamp': '2020-11-23T11:00:01', 'writer': 'Leonardo', 'shares_count': 1,
    'comments_count': 1, 'summary': 'Sumario 2', 'sources': ['ResetEra'], 'categories': ['PC', 'Console']
  },
]

url = "url"
title = "title"
values_of_key = [news[url] for news in list_of_dicts]

print(values_of_key)

URL_BASE = "https://www.tecmundo.com.br/mobilidade-urbana-smart"
URL_CROP = "-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
URL_NEWS = "https://www.tecmundo.com.br/novidades"
# result = scrape_noticia(fetch(URL_BASE + URL_CROP))
# result2 = scrape_novidades(fetch(URL_NEWS))
# scrape_next_page_link(fetch(URL_NEWS))
# get_tech_news(5)
# print(result)
# print(result2)
# print(result3)
