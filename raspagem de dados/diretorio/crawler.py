from parsel import Selector
import requests

URL_BASE = "http://books.toscrape.com/catalogue/"

response = requests.get(URL_BASE + "page-1.html")
selector = Selector(text=response.text)
next_page_url = 'page-1.html'
while next_page_url:
    # Busca o conteúdo da próxima página
    # response = requests.get(URL_BASE + next_page_url)
    # selector = Selector(text=response.text)
    # Imprime os produtos de uma determinada página
    for product in selector.css(".product_pod"):
        # Busca e extrai o título e  o preço
        re = r"£\d+\.\d{2}"
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".product_price .price_color::text").re(re)
        print('Titulo ' + title, 'Preco ' + price[0])

        # Busca o detalhe de um produto
        detail_href = product.css("h3 a::attr(href)").get()
        detail_page_url = URL_BASE + detail_href

        # Baixa o conteúdo da página de detalhes
        detail_response = requests.get(detail_page_url)
        detail_selector = Selector(text=detail_response.text)

        # Extrai a descrição do produto
        id = '#product_description'
        description = detail_selector.css(id + " ~ p::text").get()
        suffix = "...more"
        if description.endswith(suffix):
            description = description[:-len(suffix)]
        print('Descricao' + description)

    # Descobre qual é a próxima página
    next_page_url = selector.css(".next a::attr(href)").get()
