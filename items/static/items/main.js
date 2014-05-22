$(document).on('click', '.delete', function(event){
    var element = $(event.target);
    var id = element.attr("data-id");
    $.ajax({
        url: "/api/v1/items/" + id + "/",
        type: "DELETE",
        success: function(data, textStatus, jqXHR) {
            if (jqXHR.status === 204) {
                element.parent().parent().remove();
            }
        }
    });
});

$(".add").click(function(event) {
    var form = $("#addForm");
    $.ajax({
        url: "/api/v1/items/",
        type: "POST",
        data: JSON.stringify(form.serializeObject()),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function(data, textStatus, jqXHR) {
            if (jqXHR.status === 201) {
                form.trigger('reset');
                $("#itemsList tbody").append('<tr><td>' + data.name + '</td><td><span class="glyphicon glyphicon-minus delete" data-id="' + data.id + '"></span></td></tr>');
            }
        }
    });
});
