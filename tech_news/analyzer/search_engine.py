from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news_title = search_news(query)
    return [(news["title"], news["url"]) for news in news_title]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    query = {"tags": {"$regex": tag, "$options": "i"}}
    news_tag = search_news(query)
    return [(news["title"], news["url"]) for news in news_tag]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
