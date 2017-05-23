var auth = new Vue({
    el: "body",
    data: {
        phone: '',
        code: '',
        password: '',
        password_retype: '',
        error_msg: ''
    },
    methods: {
        get_code: function(e) {
            var myreg = /^(1[3578]\d{9})$/;
            if (!myreg.test(this.phone)) {
                this.error_msg = 'please input right phone number'
            } else {
                $(e.target).attr('disabled', 'disabled');
                $.get('/auth/send-message', { phone: this.phone }, function(data) {
                    if (data.error) {
                        login.error_msg = data.msg;
                    } else {
                        $('#phone').attr('readonly', 'readonly');
                    }
                });
                var i = 61;
                timer();

                function timer() {
                    i--;
                    $(e.target).text('resend after ' + i + 'sec');
                    if (i == 0) {
                        clearTimeout(timer);
                        $(e.target).removeAttr("disabled");
                        $(e.target).text('resend');
                    } else {
                        setTimeout(timer, 1000);
                    }
                }
            }
        },
        register: function() {
            var myreg = /^(1[3578]\d{9})$/;
            if (!myreg.test(this.phone)) {
                this.error_msg = 'Please input right phone number'
            } else if (this.password != this.password_retype) {
                this.error_msg = 'Entered passwords differ!'
            } else {
                $('#submit_btn').attr('disabled', 'disabled');
                $.get('check_code/' + this.phone + '/' + this.code, {}, function(data) {
                    if (data.error) {
                        login.error_msg = data.msg;
                        $('#submit_btn').removeAttr("disabled");
                    }
                });
            }
        },
        login: function() {
            var myreg = /^(1[3578]\d{9})$/;
            if (!myreg.test(this.phone)) {
                this.error_msg = 'Please input right phone number'
            } else if (this.password != this.password_retype) {
                this.error_msg = 'Entered passwords differ!'
            } else {
                $('#submit_btn').attr('disabled', 'disabled');
                $.get('check_code/' + this.phone + '/' + this.code, {}, function(data) {
                    if (data.error) {
                        login.error_msg = data.msg;
                        $('#submit_btn').removeAttr("disabled");
                    }
                });
            }
        }
    }
});
