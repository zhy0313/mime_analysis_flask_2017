require('./vendor/map/china.js');
require('./vendor/jquery.pin.min.js');
require('./vendor/echarts-wordcloud.min.js');

var now_date = new Date();

window.global = {
    now: now_date,
    now_year: now_date.getFullYear(),
    now_month: now_date.getMonth() + 1,
    color: ['#00a0e9', '#E74C3C', '#34495E', '#E67E22', '#1ABC9C', '#95A5A6', '#9B59B6', '#F1C40F', '#2980B9', '#16A085', '#2C3E50', '#27AE60', '#C0392B', '#7F8C8D', '#D35400', '#8E44AD', '#F39C12'],
};
// $.ajaxSetup({
//     headers: {
//         'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
//     }
// });

$(document).ready(function () {

    $('#navbar_list').find('.nav-item a[href="' + window.location.pathname + '"]').parent().addClass('active');

    $('.smoove').smoove({moveY: '500px'});

    $(".pinned").pin({
        containerSelector: 'body>.container',
        minWidth: 768
    });
});
