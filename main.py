from flask import Flask, jsonify, request
import requests
import html_extracter

app = Flask(__name__)

# page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
# soup = BeautifulSoup(page.text, 'html.parser')


@app.route('/main', methods = ['GET', 'POST'])
def main():
	raw_html = request.args.get('html') or None
	"""main algorithm, takes in html and returns http reqeust to BetterNews in json format"""
	# news_articles =
	# google_cloud()
	# better_news()


	return jsonify(news_articles)


@app.route('/test', methods = ['GET'])
def http_test():
	state1 = request.args.get('state') or None

	if state1 == 1:


		data = {

		'key':'value'
		
		}

		return jsonify(data)
	else:
		return "failure"


if __name__ == '__main__':
	app.run(debug = True)
