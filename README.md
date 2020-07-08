# WebscraperApp

Chrome extension that looks at the article you’re reading, and then intelligently suggests new articles to read; note: **final build is still in progress**

---

Spec:

<div style="width: 640px; height: 480px; margin: 10px; position: relative;"><iframe allowfullscreen frameborder="0" style="width:640px; height:480px" src="https://app.lucidchart.com/documents/embeddedchart/9a682224-6080-418d-bcd7-74e7af484fa3" id="M2fb~J_DOrFt"></iframe></div>

---

Backend
a) Scrape data off of the website the user is correctly on
b) Run scraped data through NLP to extract key terms and identify article topic
c) Using the key terms identified in (b) use ML to identify relevant articles 
d) Use BetterNews API to query and retrieve relevant articles
e) Store and cache results 

Frontend
a) actual chrome extension: logo for extension button; how would the articles pop up (maybe miniature views of the article pop up on the bottom right, with title and news source in bigger font)

Please contact toddyu@berkeley.edu for detailed inquiries
