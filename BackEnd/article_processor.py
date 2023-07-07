from newspaper import Article
def getContents(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

