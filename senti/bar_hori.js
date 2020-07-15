
Highcharts.chart('barContainer1', {
    chart: {
        type: 'bar',
        style: "{font-family:'Monserrat',sans-serif;size:40px;}"
    },
    colors: [
        "#FFA69E","#5E6472"

    ],
    title: {
        text: "Positive/Negative"
    },
    xAxis: {
    
        categories: ['March', 'April', 'May', 'June']
    },
    credits: {
        text: ""
    },
    yAxis: {
        min: 0,
		max: 400000,
        title: {
            text: "Number of Tweets"
        }
    },
    legend: {
        reversed: true
    },
    plotOptions: {
        series: {
            stacking: 'normal'
        }
    },
    series: [{
        name: 'Positive',
        data: [54012, 153856, 216834, 23974]
    }, {
        name: 'Negative',
        data: [45378, 117932, 180545, 21353]
    }, ]
});