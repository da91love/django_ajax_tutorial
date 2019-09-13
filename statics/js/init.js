$(document).ready(function(){

    $('#selectItems').select2();
    $('#selectItems').attr({'width':'100%'});

    /**
     * Ajax to setup csrftoken
     */
    const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    function _csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!_csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});