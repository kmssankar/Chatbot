var lastTimeID = 0;

$(document).ready(function() {
  $('#btnSend').click( function() {
    sendChatText();
    $('#chatInput').val("");
  });
});

function startChat(){
  setInterval( function() { getChatText(); }, 2000);
}

function sendChatText(){
  var chatInput = $('#chatInput').val();
  console.log(chatInput);
  if(chatInput != ""){
	  var Apendchat = "";
	  Apendchat += '<div style="color:#0000FF" >' + 'You </b>: ' + chatInput + '</div>';
	  $('#view_ajax').append(Apendchat);
	  $.ajax({
		  type: 'GET',
          dataType: 'json',
          contentType: 'application/json; charset=utf-8',
          url: '/fleet/Reply',
          data: {
                 'Input': chatInput
                },
                success: function(result) {
                	console.log (result);
                	    var html = "";
                	      html += '<div style="color:#0000AA" >' + ' <b> LAISA :</b>: ' + result["ResponseRply"] + '</div>';                        
                	    $('#view_ajax').append(html);
                }
    });
  }
}