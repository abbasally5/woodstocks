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

var stockFormSuccess = function(json) {
	$("#stockInput").val("");
	alert(json);
	return true;
}

var stockFormComplete = function() {	
	return true;
}

$('#stockForm').submit(function(e) {
	e.preventDefault();
	alert('you entered the form');
	get('/stockquote', {
		'stock_symbol': $('#stockInput').val()
	}, stockFormSuccess, stockFormComplete);
})