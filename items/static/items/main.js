$(".delete").click(function(event) {
    $.get("delete/"+$(event.target).attr("data-id"), function(data){
        if (data == "ok") {
            $(event.target).parent().parent().remove();
        }
    });
});
