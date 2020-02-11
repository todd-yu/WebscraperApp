"""This module contains the logic to extract the keywords from a set of text."""
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import requests

client = language.LanguageServiceClient()

testUrl = "https://techcrunch.com/2019/12/06/elon-musk-found-not-liable-in-case-brought-against-him-by-british-diver"
page = requests.get(testUrl)

text = extract_text(page)
document = language.types.document(
    content = text,
    language = "en",
    type = "PLAIN_TEXT"
)
categories = client.classify_text(document = document).categories
print(categories)
