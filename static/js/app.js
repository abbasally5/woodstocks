var stock = "";
var fileurl = "";
var playing = false;

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


var buildMusicBtn = function() {
	var code = "";
	code += "<button id='musicBtn' class='btn btn-success'>" + 
	"Convert " + stock + " Stock to Music" + "</button>";
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
	stock = data['Symbol'];
	var cardCode = buildStockCard(data);	
	$('#stockCards').html(cardCode);

	var btnCode = buildMusicBtn();
	$('#musicConverter').html(btnCode);
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
});

var buildMediaBtn = function() {
	var code = "<button id='mediaBtn' class='btn btn-success'>" + 
	"<a href=\"#\" onClick=\"MIDIjs.play(\'" + 
		fileurl + "\');\"><span class=\"glyphicon glyphicon-play\"" +
		 "aria-hidden=\"true\"></span></a></button>";
	//alert(code);
	return code;
}

var changeMediaBtn = function() {
	var code = ""
	if (playing)
	{
		code = "<button id='mediaBtn' class='btn btn-success'>" + 
		"<a href=\"#\" onClick=\"MIDIjs.stop();\"><span class=\"glyphicon glyphicon-pause\"" +
		 "aria-hidden=\"true\"></span></a></button>";
	}
	else
	{
		code = buildMediaBtn();
	}
	return code;
}

var musicBtnSuccess = function(json) {
	if (json['success'] == 'failure')
	{
		alert('We encountered an ever converting the stock to music.');
		return true;
	}
	//alert(json['file_url']);
	fileurl = json['file_url'];
	mediaBtnCode = buildMediaBtn(json['file_url']);
	$('#musicConverter').append(mediaBtnCode);
	return true;
}

var musicBtnComplete = function() {
	return true;
}

$('#musicConverter').on('click', '#musicBtn', function(e) {
	e.preventDefault();
	//alert('music button pressed' + stock);
	post('/convertMusic', {
		'stock_symbol': stock
	}, musicBtnSuccess, musicBtnComplete);
	//alert(stock);
});

$('#musicConverter').on('click', '#mediaBtn', function(e) {
	e.preventDefault();
	playing = !playing;
	//alert('media button pressed ' + stock);
	mediaBtnCode = changeMediaBtn();
	$('#mediaBtn').replaceWith(mediaBtnCode);
});
