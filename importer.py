import json

from example import Example


class Importer(object):

  def __init__(self, path):
    self.doc = json.load(open(path))

  def examples(self):
    all_examples = []

    entities, intents = self.parse()

    for name, intent in intents.items():
      for text in intent['examples']:
        example = Example(text, name, entities)
        all_examples.append(example)

    return all_examples

  def parse(self):
    entities = self.parse_entities(self.doc['entities'])
    intents = self.parse_intents(self.doc['intents'])
    return entities, intents

  def parse_intents(self, intents):
    parsed = {}

    for item in intents:
      name = item['intent']
      examples = item['examples']
      parsed[name] = {'examples': self.parse_examples(examples)}

    return parsed

  def parse_examples(self, examples):
    return [item['text'] for item in examples]

  def parse_entities(self, entities):
    transformed = {}

    for entity in entities:
      # each entity has a value and synonyms for that value
      name = entity['entity']
      transformed[name] = {}

      for value in entity['values']:
        entity_value = value['value']
        transformed[name][entity_value] = value['synonyms']

    return transformed
