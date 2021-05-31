from wiktionaryparser import WiktionaryParser
parser = WiktionaryParser()
parser.set_default_language('old norse')
word = parser.fetch('abbadissa')
print(word)