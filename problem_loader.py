import requests
import pickle
import logging

def preprocess_data(data):
    return list(map(int, data.split())) 

class ProblemLoader():
  def __init__(self, url, preprocessor=preprocess_data):
    self.url = url
    self.preprocess_data = preprocessor

  def fetch(self):
    values = []
    try:
        logging.info("Loading existing dataset")
        values = pickle.load(open("100kint.p", "rb"))
    except:
        logging.debug("Failed to load existing dataset!")
        logging.info("Preprocess new dataset")
        r = requests.get(self.url, allow_redirects=True)
        values = self.preprocess_data(r.content)
        pickle.dump(values, open("100kint.p", "wb"))
    return values
