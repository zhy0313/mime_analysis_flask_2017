var auth = new Vue({
    delimiters: ['[[', ']]'],
    el: "#content",
    data: {
        error_message: ''
    },
    methods: {
        get_code: function (e) {
            var myreg = /^(1[3578]\d{9})$/;
            var phone = $('#phone').val();
            if (!myreg.test(phone)) {
                auth.error_message = 'please input right phone number';
            } else {
                $(e.target).attr('disabled', 'disabled');
                $.get('/sms_code/' + phone, function (data) {
                    if (data.error) {
                        auth.error_message = 'Phone number not found';
                    } else {
                        $('#phone').attr('readonly', 'readonly');
                    }
                });
                var i = 61;
                timer();

                function timer() {
                    i--;
                    $(e.target).text('resend after ' + i + 'sec');
                    if (i <= 0) {
                        clearTimeout(timer);
                        $(e.target).removeAttr("disabled");
                        $(e.target).text('resend');
                    } else {
                        setTimeout(timer, 1000);
                    }
                }
            }
        }
    }
});
