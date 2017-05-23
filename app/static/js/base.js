Vue.config.delimiters = ["[[", "]]"];


var now_date = new Date();

var now_year = now_date.getFullYear(),
    now_month = now_date.getMonth() + 1;

var color = ['#00a0e9', '#E74C3C', '#34495E', '#E67E22', '#1ABC9C', '#95A5A6', '#9B59B6', '#F1C40F', '#2980B9', '#16A085', '#2C3E50', '#27AE60', '#C0392B', '#7F8C8D', '#D35400', '#8E44AD', '#F39C12'];

$(document).ready(function() {
    $('.input-group').on('focus', '.form-control', function() {
        $(this).closest('.input-group, .form-group').addClass('focus');
    }).on('blur', '.form-control', function() {
        $(this).closest('.input-group, .form-group').removeClass('focus');
    });

    $('.smoove').smoove({ moveY: '500px' });

    $(".pinned").pin({
    	containerSelector: '.min-height',
        minWidth: 768
    });
});
