"""This module contains the logic to extract the keywords from a set of text."""
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
<<<<<<< HEAD
from google.cloud import storage
=======
<<<<<<< HEAD
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
=======
>>>>>>> 6add5b83d9496c4a6baf6970c40abb68e093f3ca

client = language.LanguageServiceClient()

# before starting, 
# run "pip3 install --upgrade google-cloud-language" in terminal and selected environment
# then, authenticate by typing this into the terminal using the correct path:
# export GOOGLE_APPLICATION_CREDENTIALS="/[path-to-key]/[key]"
# e.g. export GOOGLE_APPLICATION_CREDENTIALS="/Users/toddyu/Desktop/Projects/WebscraperAppKeys/webscraper-app2019-4d5a7b00cfcb.json"

# test to analyze
text = 'Hello, world!'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)
print(text)
>>>>>>> 45219fe410749586d357737bc05a3c588ce22c63
