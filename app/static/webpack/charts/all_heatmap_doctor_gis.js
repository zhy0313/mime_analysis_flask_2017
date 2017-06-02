var chart_name = 'all_heatmap_doctor_gis';
new Vue({
    el: chart_name,
    data: {
        title: chart_name,
        get_url: '/time/regions/',
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
            var max = 0;
            data = data.map(function (val) {
                max = max>val.register_count?max:val.register_count;
                return [val.longitude, val.latitude, val.register_count]
            });
            max = Math.ceil(max/10)*10;

            var option = {
                title: {
                    text: '全国用户分布热力图',
                    left: 'center',
                    textStyle: {
                        color: '#fff'
                    }
                },
                backgroundColor: '#404a59',
                visualMap: {
                    min: 0,
                    max: max,
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