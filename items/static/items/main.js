$(".delete").click(function(event) {
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
    $.ajax({
        url: "/api/v1/items/",
        type: "POST",
        data: JSON.stringify($("#addForm").serializeObject()),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function(data) {
            alert('123');
        }
    });
});
