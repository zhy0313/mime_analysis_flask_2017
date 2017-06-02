var chart_name = 'month_gauge_doctor_3';
var chart_month_gauge_doctor_3;
chart_month_gauge_doctor_3 = new Vue({
    el: chart_name,
    data: {
        title: chart_name,
        get_url: '',
        get_data: ''
    },
    methods: {
        refresh: function (e) {
            var vm = this;
            $.get(vm.get_url, {}, function (data) {
                vm.get_data = data;
                vm.chart();
            });
        },
        chart: function () {
            var option = {
                title: {
                    text: '某站点用户访问来源',
                    x: 'center'
                },
                tooltip: {
                    formatter: "{a} <br/>{b} : {c}%"
                },
                // toolbox: {
                //     feature: {
                //         restore: {},
                //         saveAsImage: {}
                //     }
                // },
                series: [
                    {
                        name: '业务指标',
                        type: 'gauge',
                        detail: {formatter: '{value}%'},
                        data: [{value: 50, name: '完成率'}]
                    }
                ]
            };

            var chart = echarts.init(document.getElementById(this.title));
            chart.setOption(option);
        }
    },
    mounted: function () {
        this.refresh();
    }
});