var chart_name = 'year_bar_doctor_all_count';
new Vue({
    el: '#'+chart_name+'_block',
    data: {
        title: chart_name,
        get_url: '/time/months/',
        get_data: '',
        select_year: window.global.now_year
    },
    watch: {
        select_year: function () {
            this.refresh()
        }
    },
    methods: {
        refresh: function () {
            var vm = this;
            $.get(vm.get_url+vm.select_year, {}, function (data) {
                vm.get_data = JSON.parse(data);
                vm.chart();
            });
        },
        chart: function () {
            var data = this.get_data;
            var month=[],
                register_count=[],
                authorize_count=[],
                trade_count=[];
            data.sort(function (a, b) {
                return a>b;
            }).map(function (val) {
                month.push(val.month+'月');
                register_count.push(val.register_count);
                authorize_count.push(val.authorize_count);
                trade_count.push(val.trade_count);
            });
            var option = {
                color: window.global.color,
                title: {
                    text: '全年统计'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                        type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                    }
                },
                legend: {
                    data: ['register_count', 'authorize_count', 'trade_count']
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
                        data: month
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
                        type: 'bar',
                        data: register_count
                    },
                    {
                        name: 'authorize_count',
                        type: 'bar',
                        data: authorize_count
                    },
                    {
                        name: 'trade_count',
                        type: 'bar',
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