function addChat() {
	//get the message from the user
	var message = document.getElementById('chat-message').value;
	//clear the text box
	document.getElementById('chat-message').value = "";
	//add the message to the messages under "You"
	
	var newHTML = '<div class="message you">' + message + '</div>';
	document.getElementById('chat-box').innerHTML += newHTML;
	
	// now get Trump's response via Ajax.

	$.ajax(
		'http://32d4b85d.ngrok.io/response',
		{
		type: "get",
		dataType: 'text',
		contentType: 'text/plain',
		asynchronous: false,
		data: {'q': message},
		success: function(resp,status) {
			console.log(resp);
			var elem = $('<div>').addClass("message trump").text(resp.text);
			//var thisHTML = '<div class="message trump">' + data + '</div>';
			$('#chat-box').append(elem);
			//document.getElementById('chat-box').innerHTML += thisHTML;
		}
	});
}
