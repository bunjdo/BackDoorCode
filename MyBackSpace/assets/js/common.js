$.fn.serializeObject = function()
{
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};

$(document).ready(function () {
    $("form#ajax-form").submit(function (e) {

        $("form#ajax-form button[type='submit']").prop('disabled', true);

        var formData = $('form#ajax-form').serializeObject();

        //$.each($('form#ajax-form').serializeArray(), function (_, kv) {
        //    formData[kv.name] = kv.value;
        //});

        console.log(formData);

        $.ajax({
            url: window.location.pathname,
            type: "POST",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(formData),
            success: function (data, msg) {
                console.log(data);

                alert(data.status);
                if (data.status === "ok") {
                    window.location.replace(data.url);
                }
            },
            error: function (jqXHR, msg, throws) {
                console.log(jqXHR);
                console.log(msg);
                console.log(throws);
                alert("Ошибка");
            }
        });

        e.preventDefault();
        return false;

    });
});