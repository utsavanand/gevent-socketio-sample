var socket = io.connect("/echo"),
    $log = $("#log"),
    $input = $("#input-echo");

socket.on('msg', function (msg) {
	alert("hey");
    $log.append($("<p>" + msg + "</p>"));
});

$("#form-echo").on("submit", function(event){
	alert("woah");
    event.preventDefault();
    var msg = $input.val();
    $input.val("");
    alert("hello");
    socket.emit("msg", msg);
});