var socket = io.connect(window.location.protocol+'//' + document.domain + ':' + location.port);
    socket.on('connect', function () {
        socket.send('yo');
    });

    socket.on('change', function (data) {
    console.log(data);
    $("#balance").text(data['balance']);
    $('ul').empty();
    data['transactions'].map((key) => {
        if (key < 0)
            $("ul").append('<li>Rs ' + Math.abs(key) + ' is debited form your account.</li>');
        else
            $("ul").append('<li>Rs ' + key + ' is credited to your account.</li>');
    });
});

$("button").click(function () {
    var amount = $("#amount").val();
    $("#amount").val('');
    socket.emit('transaction', {'amount': amount});
});