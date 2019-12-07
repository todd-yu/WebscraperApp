"""This module contains the logic to extract the keywords from a set of text."""
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

client = language.LanguageServiceClient()

# before starting, 
# authenticate by typing this into the terminal using the correct path:
# export GOOGLE_APPLICATION_CREDENTIALS="/Users/toddyu/Desktop/Projects/WebscraperAppKeys/webscraper-app2019-4d5a7b00cfcb.json"

# test to analyze
text = 'Hello, world!'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)
print(text)