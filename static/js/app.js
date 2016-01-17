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

	var code = "";

	if (change > 0)
	{
		code += "<div class='panel panel-success'>";
	}
	else
	{
		code += "<div class='panel panel-danger'>";
	}

	code += "<div class='panel-heading'>" +
    "<h3 class='panel-title'>" + name + "</h3>" +
    "<h4 class='panel-title'>" + exchange + ": " + symbol + 
    " - " + date + "</h4>" + 
  "</div>" + 
  "<div class='panel-body'>" + 
    "<h3>$" + (Math.round(price * 100) / 100) + "</h3>" + 
    "<h4>" + (Math.round(change * 100) / 100) + 
    " (" + (Math.round(changePer * 100) / 100) + "%)</h4>" +
  "</div>" +
"</div>";
	return code;
}


var stockFormSuccess = function(json) {
	$("#stockInput").val("");
	//alert('hello');
	if (json['success'] == 'failure')
	{
		alert('We do not have information for that stock');
		return true;
	}
	var data = json['stockName'];
	var htmlCode = buildStockCard(data);	
	$('#stockCards').html(htmlCode);
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