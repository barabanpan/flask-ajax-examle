$('#send').click(function() {
    $.ajax({
        url: "/send?name=" + document.getElementById("name").value + "&age=" + document.getElementById("age").value,
        success: function(response) {
            $('#response').html(response);
        }
    });
})
