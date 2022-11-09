import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        header = {"user-agent": "Fake user-agent"}
        response = requests.get(url, header=header, timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    url = selector.css("h2.entry-title a::attr(href)").getall()
    return url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css(".next ::attr(href)").get()
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("li.meta-author .author a::text").get(),
        "comments_count": len(selector.css("comment-list").getall()),
        "summary": "".join(
            selector.css(
                "div.entry-content > p:nth-of-type(1) ::text"
            ).getall()
        ).strip(),
        "tags": selector.css(
            "section.post-tags li a[rel=tag]::text"
        ).getall(),
        "category": selector.css("span.label::text").get()
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
