class Source:
  """
  This class defines our source Objects
  """
  def __init__(self, id, name,description, url, category):
    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category


class Articles:
  """
  Article class defines the article Object
  """
  def __init__(self, author, title, description,url, picture, publishedAt):
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.picture = picture
    self.publishedAt = publishedAt
