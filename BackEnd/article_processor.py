from newspaper import Article

class ArticleParser:
    def __init__(self, source):
        self.source = source
        self.article = None

    def download(self):
        self.article = Article(self.source)
        self.article.download()

    def set_html(self, html_string):
        self.article = Article('')
        self.article.set_html(html_string)

    def parse(self):
        self.article.parse()

    def get_text(self):
        return self.article.text
