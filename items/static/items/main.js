$(".delete").click(function(event) {
    $.get("delete/"+$(event.target).attr("data-id"), function(data){
        if (data == "ok") {
            $(event.target).parent().parent().remove();
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
