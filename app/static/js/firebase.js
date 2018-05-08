var socket = io.connect(window.location.protocol+'//' + document.domain + ':' + location.port);
    socket.on('connect', function () {
        socket.send('yo');
    });

    socket.on('error', function (msg) {
        console.log(msg);
    });

    socket.on('money', function (data) {
    // console.log(data);
    $("#balance").text(data['balance']);
    $('ul#transaction').empty();
    data['transactions'].map((key) => {
        if (key < 0)
            $("ul#transaction").append('<li>Rs ' + Math.abs(key) + ' is debited form your account.</li>');
        else
            $("ul#transaction").append('<li>Rs ' + key + ' is credited to your account.</li>');
    });
});

socket.on('contact', function (data) {
    $('ul#contact').empty();
    $("ul#contact").append('<li>Address : ' + data['address'] + '</li>');
    $("ul#contact").append('<li>Mobile No : ' + data['mobile'] + '</li>');
});

$("button").click(function () {
    var amount = $("#amount").val();
    $("#amount").val('');
    socket.emit('transaction', {'amount': amount});
});