import requests

class Grabber:
  def __init__(self, url):
    self.url=url
  def returnPage(self):
    return requests.get(self.url)



