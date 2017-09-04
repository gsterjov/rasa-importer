import json


class Exporter(object):

  def __init__(self, path):
    self.path = path

  def export(self, examples):
    doc = {
      "rasa_nlu_data": {
        "common_examples": [example.to_json() for example in examples]
      }
    }

    with open(self.path, 'w') as outfile:
      json.dump(doc, outfile)
