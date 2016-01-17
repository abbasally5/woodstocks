from flask import Flask
from flask import render_template, request, jsonify
from stocks import *

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/stockquote", methods=["GET"])
def stock_info():
	try:
		stock_symbol = unicode(request.args.get("stock_symbol"))
	except Exception as e:
		print e
	stock_symbol = stock_symbol.upper()
	print stock_symbol
	global stocks
	if binary_search(stock_symbol) is False:
		print 'fail'
		print stock_symbol
		return jsonify({
			'success': 'failure'
			})
	else:
		return jsonify({
			'success': 'success',
			'stockName': get_stock_info(stock_symbol)
			})


if __name__ == "__main__":
	app.run()