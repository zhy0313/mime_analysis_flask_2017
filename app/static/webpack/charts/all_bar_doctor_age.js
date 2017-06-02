var chart_name = 'all_bar_doctor_age';
new Vue({
    el: chart_name,
    data: {
        title: chart_name,
        get_url: '/time/age_groups/',
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
            var data_category = [];
            data = data.map(function (val) {
                data_category.push(val.age_group);
                return val.count
            });
            var option = {
                color: window.global.color,
                title: {
                    text: '年龄段'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                        type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                    }
                },
                // legend: {
                //     data: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎', '百度', '谷歌', '必应', '其他']
                // },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: [
                    {
                        type: 'category',
                        data: data_category
                    }
                ],
                yAxis: [
                    {
                        type: 'value'
                    }
                ],
                series: [{
                    name: '人数',
                    type: 'bar',
                    data: data
                }]
            };


            var chart = echarts.init(document.getElementById(this.title));
            chart.setOption(option);
        }
    },
    mounted: function () {
        this.refresh();
    }
});