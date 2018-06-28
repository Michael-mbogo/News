class News:
    def __init__(self,name,description,url,category,language,country):
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
class Articles:
    def __init__(self,name,author,title,description,url,urlToImage,publishedAt):
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt =publishedAt
