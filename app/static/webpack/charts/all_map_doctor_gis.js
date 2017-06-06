var chart_name = 'all_map_doctor_gis';
new Vue({
    delimiters: ["[[", "]]"],
    el: '#' + chart_name + '_block',
    data: {
        title: chart_name,
        get_url: '/region/index/',
        get_data: '',
        select_province: '湖北',
        provinces: ["南海诸岛","台湾", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "广西", "海南", "四川", "贵州", "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆", "北京", "天津", "上海", "重庆", "香港", "澳门"]
    },
    watch: {
        select_province: function () {
            window.global.select_province = this.select_province;
            this.refresh();
        }
    },
    methods: {
        refresh: function (e) {
            var vm = this;
            $.get(vm.get_url+vm.select_province, {}, function (data) {
                vm.get_data = JSON.parse(data);
                vm.chart();
            });
        },
        chart: function () {
            var vm = this;
            var option = {
                title: {
                    text: vm.select_province,
                    left: 'center'
                },
                series: [{
                    type: 'map',
                    mapType: 'china',
                    selectedMode: 'single',
                    label: {
                        normal: {
                            show: true
                        },
                        emphasis: {
                            show: true
                        }
                    },
                    itemStyle: {
                        normal: {
                            areaColor: window.global.color[0],
                            borderColor: '#fff'
                        },
                        emphasis: {
                            areaColor: window.global.color[4]
                        }
                    },
                    data: [
                        {name: vm.select_province, selected: true}
                    ]
                }]
            };
            var chart = echarts.init(document.getElementById(this.title));
            chart.setOption(option);
            chart.on('mapselectchanged', function (params) {
                vm.select_province=params.batch[0].name;
            })
        }
    },
    mounted: function () {
        this.refresh();
    }
});