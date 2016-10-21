// global variables
var data = null;
var timerId = null;

$(document).ready(function(){
    data = $("#currency-ex-form").serializeArray();
    drawGraph();
    startTimer();    
});

function validateForm(){
    data = $("#currency-ex-form").serializeArray();
    var validation = true; 

    // clear all errors
    $(".form-group").each(function(i,e){
        $(this).removeClass("has-error");
    });    

    if(data[0].value == "" || parseFloat(data[0].value) <= 0 ){
        $("#amt-form-group").addClass("has-error"); 
        validation = false;       
    }

    return validation;
}

// making ajax get request
function getResult(data){
    $.ajax({
        type        : 'GET',
        url         : '/result',
        data        : data,
        dataType    : 'html',
        encode      : true  
    })
    .done(function(data){
        $("#currency-ex-result").empty();
        $("#currency-ex-result").append(data);                
        startTimer();
    });
}

// refresh countdown
function startTimer(){
    var seconds = 60;
    // stop old timer
    if (timerId) clearInterval(timerId);
    // start new timer
    timerId = setInterval(function(){
        seconds -= 1;
        if (seconds <= 0) {
            getResult(data);
            clearInterval(timerId);
        }
        $("#timer-refresh").text(seconds);

    },1000);
}

// switch currency to-from
function currencySwitch(){
    var froCurr = $('#froCurr').find(":selected").val();
    var toCurr = $('#toCurr').find(":selected").val();
    $('#froCurr').val(toCurr);
    $('#toCurr').val(froCurr);
}

// draw historic data graph
function drawGraph() {    
    $.ajax({
        type    : 'GET',
        url     : '/hresult',
        data    :  data,
        encode  : true 
    }).done(function(data) {        
        // create the chart
        $('#hresult-graph').highcharts('StockChart', {

            title: {
                text: hresultGraphTitle
            },

            subtitle: {
                text: '(past month)'
            },

            xAxis: {
                gapGridLineWidth: 0
            },

            rangeSelector: {
                buttons: [],           
                inputEnabled: false
            },

            series: [{
                name: name,
                type: 'area',
                data: data,
                gapSize: 5,
                tooltip: {
                    valueDecimals: 5
                },
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                threshold: null
            }]
        });
    });
}


