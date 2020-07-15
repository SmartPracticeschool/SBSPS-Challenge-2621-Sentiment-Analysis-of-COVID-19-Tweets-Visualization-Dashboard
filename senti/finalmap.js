// Prepare demo data
// Data is joined to map using value of 'hc-key' property by default.
// See API docs for 'joinBy' for more info on linking data and map.
var data = [
    ['madhya pradesh', 12553],
    ['uttar pradesh', 6577],
    ['karnataka', 78257],
    ['nagaland', 136],
    ['bihar', 4040],
    ['lakshadweep', 0],
    ['andaman and nicobar', 448],
    ['assam', 1056],
    ['west bengal', 73362],
    ['puducherry', 2242],
    ['daman and diu', 3459],
    ['gujarat', 30111],
    ['rajasthan', 11534],
    ['dadara and nagar havelli', 2213],
    ['chhattisgarh', 1257],
    ['tamil nadu', 90679],
    ['chandigarh', 31830],
    ['punjab', 35374],
    ['haryana', 7403],
    ['andhra pradesh', 4292],
    ['maharashtra', 178844],
    ['himachal pradesh', 7],
    ['meghalaya', 313],
    ['kerala', 11044],
    ['telangana', 76685],
    ['mizoram', 8],
    ['tripura', 1548],
    ['manipur', 469],
    ['arunanchal pradesh', 153],
    ['jharkhand', 2209],
    ['goa', 15228],
    ['nct of delhi', 115009],
    ['odisha', 25742],
    ['jammu and kashmir', 0],
    ['sikkim', 111],
    ['uttarakhand', 7515]
];

// Create the chart
Highcharts.mapChart('mapContainer', {
    chart: {
        map: 'countries/in/custom/in-all-disputed'
    },

    title: {
        text: 'Statewise Tweet Count'
    },

    subtitle: {
        text: 'Source map: <a href="http://code.highcharts.com/mapdata/countries/in/custom/in-all-disputed.js">India with disputed territories</a>'
    },

    mapNavigation: {
        enabled: true,
        buttonOptions: {
            verticalAlign: 'bottom'
        }
    },

    colorAxis: {
        min: 0,
		minColor: '#EEFBFB',
        maxColor: '#1E8582'
		
    },
    
    credits: {
        text: ""
    },

    series: [{
        data: data,
        name: 'Statewise tweet count',
        states: {
            hover: {
                color: '#87b42d'
            }
        },
        dataLabels: {
            enabled: true,
            format: '{point.name}'
        }
    }]
});
