$(document).ready(function(){

    $(document).on('click', '#btnAddPtag', function(){

        const inputVal = $('#input').val();
        data = {'data': inputVal};

        $.ajax({
            url : '/ajaxtest/response/',
            dataType : 'json',
            data : data,
            type : 'POST',
            content_type : "application/json",
            success: function(result){
                $('#divShowInput').append(`<p> ${result.data} </p>`);
            }
        });
    });
});