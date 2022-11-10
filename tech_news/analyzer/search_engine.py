from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news_title = search_news(query)
    return [(news["title"], news["url"]) for news in news_title]


# Requisito 7
def search_by_date(date):
    try:
        format_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        news_date = search_news({"timestamp": format_date})
        return [(news["title"], news["url"]) for news in news_date]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    query = {"tags": {"$regex": tag, "$options": "i"}}
    news_tag = search_news(query)
    return [(news["title"], news["url"]) for news in news_tag]


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    news_category = search_news(query)
    return [(news["title"], news["url"]) for news in news_category]
