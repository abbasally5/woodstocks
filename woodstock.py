from flask import Flask
from flask import render_template, request, jsonify
from stocks import *
from song import *

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
		json = get_stock_info(stock_symbol)
		print 'c'
		print json
		return jsonify({
			'success': 'success',
			'stockName': json
			})

@app.route("/convertMusic", methods=["POST"])
def convertToMusic():
	print 'in music conversion'
	try:
		stock_symbol = unicode(request.form.get("stock_symbol"))
	except Exception as e:
		print e
	print stock_symbol

	return jsonify({
		'success': 'success'
		})



if __name__ == "__main__":
	app.run()