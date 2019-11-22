from flask import Flask, jsonify, request, CORS
import requests
from bs4 import BeautifulSoup
import webbrowser

app = Flask(__name__)
CORS(app)

# page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
# soup = BeautifulSoup(page.text, 'html.parser')

@app.route('/main', methods = ['GET', 'POST'])

#sample comment for git push





if __name__ == '__main__':
	app.run(debug = True)
