var chart_name = 'month_line_doctor_all_count';
new Vue({
    el: chart_name,
    data: {
        title: chart_name,
        get_url: '/time/days/',
        get_data: ''
    },
    methods: {
        refresh: function (e) {
            var vm = this;
            var select_year = $('#select_year2').val();
            var select_month = $('#select_month2').val();
            $.get(vm.get_url + select_year + '/' + select_month, {}, function (data) {
                vm.get_data = JSON.parse(data);
                vm.chart();
            });
        },
        chart: function () {
            var data = this.get_data;
            var day = [],
                register_count = [],
                authorize_count = [],
                trade_count = [];
            data.sort(function (a, b) {
                return a > b;
            }).map(function (val) {
                day.push(val.day + '日');
                register_count.push(val.register_count);
                authorize_count.push(val.authorize_count);
                trade_count.push(val.trade_count);
            });
            var option = {
                color: window.global.color,
                title: {
                    text: '月份统计'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross',
                        label: {
                            backgroundColor: '#6a7985'
                        }
                    }
                },
                legend: {
                    data: ['register_count', 'authorize_count', 'trade_count']
                },
                toolbox: {
                    feature: {
                        saveAsImage: {}
                    }
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: [
                    {
                        type: 'category',
                        boundaryGap: false,
                        data: day
                    }
                ],
                yAxis: [
                    {
                        type: 'value'
                    }
                ],
                series: [
                    {
                        name: 'register_count',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {normal: {}},
                        data: register_count
                    },
                    {
                        name: 'authorize_count',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {normal: {}},
                        data: authorize_count
                    },
                    {
                        name: 'trade_count',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {normal: {}},
                        data: trade_count
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