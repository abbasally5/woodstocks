var post = function(url, data, success, complete) {
    $.ajax({
        url: url,
        type: "POST",
        datatype: "json",
        data: data,
        success: success,
        complete: complete
    });
    return false;
};

var get = function(url, data, success, complete) {
    $.ajax({
        url: url,
        type: "GET",
        datatype: "json",
        data: data,
        success: success,
        complete: complete
    });
    return false;
}

var buildStockCard = function(data) {
	var name = data['Name'];
	var symbol = data['Symbol'];
	var exchange = data['Exchange'];
	var price = data['LastPrice'];
	var changePer = data['ChangePercent'];
	var change = data['Change'];
	var date = data['Timestamp'];

	var code = "<div class='panel panel-success'>" +
  "<div class='panel-heading'>" +
    "<h3 class='panel-title'>" + name + "</h3>" +
    "<h4 class='panel-title'>" + exchange + ": " + symbol + 
    " - " + date + "</h4>" + 
  "</div>" + 
  "<div class='panel-body'>" + 
    "<h3>" + price + "</h3>" + 
    "<h4>" + change + "(" + changePer + "%)</h4>" +
  "</div>" +
"</div>";
	return code;
}


var stockFormSuccess = function(json) {
	$("#stockInput").val("");
	//alert('hello');
	var data = json['stockName'];
	var htmlCode = buildStockCard(data);	
	$('#stockCards').append(htmlCode);
	//alert('hello2');
	return true;
}

var stockFormComplete = function() {	
	return true;
}

$('#stockForm').submit(function(e) {
	e.preventDefault();
	//alert('you entered the form');
	get('/stockquote', {
		'stock_symbol': $('#stockInput').val()
	}, stockFormSuccess, stockFormComplete);
})