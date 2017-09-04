import re


class Example(object):

  def __init__(self, text, intent, entities):
    self.text = text
    self.intent = intent
    self.entities = self.parse_entities(entities)


  def parse_entities(self, entities):
    found_entities = []

    for type, values in entities.items():
      for value, synonyms in values.items():
        for matcher in set([value]).union(synonyms):
          match = re.search(r'\b({0})\b'.format(matcher), self.text, flags=re.IGNORECASE)
          if match:
            entity = Entity(type, value, match)
            found_entities.append(entity)

    return found_entities


  def to_json(self):
    return {
      'text': self.text,
      'intent': self.intent,
      'entities': [entity.to_json() for entity in self.entities]
    }



class Entity(object):

  def __init__(self, type, value, match):
    self.type = type
    self.value = value
    self.matched = match.group()
    self.start = match.start()
    self.end = match.end()


  def to_json(self):
    return {
      'entity': self.type,
      'value': self.value,
      'start': self.start,
      'end': self.end,
      'matched': self.matched
    }
