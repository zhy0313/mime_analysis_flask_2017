var chart_name = 'all_pie_doctor_office';
var chart_all_pie_doctor_office;
chart_all_pie_doctor_office = new Vue({
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
                    subtext: '纯属虚构',
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
                        data: [
                            {value: 335, name: '直接访问'},
                            {value: 310, name: '邮件营销'},
                            {value: 234, name: '联盟广告'},
                            {value: 135, name: '视频广告'},
                            {value: 1548, name: '搜索引擎'}
                        ],
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