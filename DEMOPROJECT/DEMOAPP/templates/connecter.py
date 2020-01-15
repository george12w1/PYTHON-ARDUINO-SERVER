from pymongo import MongoClient


class Connection:
  def __init__(self):
      pass
      self.cluster = MongoClient("mongodb+srv://todireanugeorge15:2r#$6uuZ&bA%pXW@cluster0-otq8c.mongodb.net/test?retryWrites=true&w=majority")
  def connection(self):
    return self.cluster