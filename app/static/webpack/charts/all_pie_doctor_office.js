var chart_name = 'all_pie_doctor_office';
new Vue({
    el: '#' + chart_name,
    data: {
        title: chart_name,
        get_url: '/time/offices/',
        get_data: ''
    },
    methods: {
        refresh: function (e) {
            var vm = this;
            $.get(vm.get_url, {}, function (data) {
                vm.get_data = JSON.parse(data);
                vm.chart();
            });
        },
        chart: function () {
            var data = this.get_data;
            data = data.map(function (val) {
                return {
                    name: val.doctor_office,
                    value: val.count
                }
            });
            var option = {
                color: window.global.color,
                title: {
                    text: '医生科室统计',
                    x: 'center'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                // legend: {
                //     orient: 'vertical',
                //     left: 'left',
                //     data: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎']
                // },
                series: [
                    {
                        name: '访问来源',
                        type: 'pie',
                        radius: '55%',
                        center: ['50%', '60%'],
                        data: data,
                        itemStyle: {
                            emphasis: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
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