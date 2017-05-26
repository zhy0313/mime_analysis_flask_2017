var chart_name = 'province_line_user';
var chart_province_line_user;
chart_province_line_user = new Vue({
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
                    text: '注册量',
                    textStyle: {
                      fontWeight: '100'
                    },
                    left: 'center',
                    bottom: '5px',
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
                grid: {
                    left: '3%',
                    right: '4%',
                    top: '3%',
                    bottom: '30px',
                    containLabel: true
                },
                xAxis: [
                    {
                        type: 'category',
                        boundaryGap: false,
                        show: false,
                        data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                    }
                ],
                yAxis: [
                    {
                        type: 'value',
                        show: false,
                        splitLine: {
                            show: false
                        }
                    }
                ],
                series: [
                    {
                        name: '邮件营销',
                        type: 'line',
                        stack: '总量',
                        smooth: true,
                        itemStyle: {
                            normal: {
                                color: "#5BC0DE"
                            }
                        },
                        areaStyle: {
                            normal: {
                                color: "#5BC0DE"
                            }
                        },
                        data: [120, 132, 101, 134, 90, 230, 210]
                    }
                ]
            };

            var chart1 = echarts.init(document.getElementById(this.title+'1'));
            var chart2 = echarts.init(document.getElementById(this.title+'2'));
            var chart3 = echarts.init(document.getElementById(this.title+'3'));
            chart1.setOption(option);
            chart2.setOption(option);
            chart3.setOption(option);
        }
    },
    mounted: function () {
        this.refresh();
    }
});