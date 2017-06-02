var chart_name = 'all_heatmap_doctor_gis';
var chart_all_heatmap_doctor_gis;
chart_all_heatmap_doctor_gis = new Vue({
    el: chart_name,
    data: {
        title: chart_name,
        get_url: '/regions/',
        get_data: ''
    },
    methods: {
        refresh: function (e) {
            var vm = this;
            $.get(vm.get_url, {}, function (data) {
                console.log(data);
                vm.get_data = data;
                vm.chart();
            });
        },
        chart: function () {
            var data = this.get_data;
            data = data.map(function (val) {
                return []
            });

            var option = {
                title: {
                    text: '全国主要城市空气质量',
                    subtext: 'data from PM25.in',
                    sublink: 'http://www.pm25.in',
                    left: 'center',
                    textStyle: {
                        color: '#fff'
                    }
                },
                backgroundColor: '#404a59',
                visualMap: {
                    min: 0,
                    max: 500,
                    splitNumber: 5,
                    inRange: {
                        color: ['#d94e5d', '#eac736', '#50a3ba'].reverse()
                    },
                    textStyle: {
                        color: '#fff'
                    }
                },
                geo: {
                    map: 'china',
                    label: {
                        emphasis: {
                            show: false
                        }
                    },
                    roam: false,
                    itemStyle: {
                        normal: {
                            areaColor: '#323c48',
                            borderColor: '#111'
                        },
                        emphasis: {
                            areaColor: '#2a333d'
                        }
                    }
                },
                series: [{
                    name: 'AQI',
                    type: 'heatmap',
                    coordinateSystem: 'geo',
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