// global variables
var formData = null;
var timerId = null;

$(document).ready(function(){
    formData = $("#currency-ex-form").serializeArray();
    if(formData && formData[0].value != ""){
        // drawGraph();
        startTimer();   
    } 
     
});

function validateForm(){
    formData = $("#currency-ex-form").serializeArray();
    var validation = true; 

    // clear all errors
    $(".form-group").each(function(i,e){
        $(this).removeClass("has-error");
    });    

    if(formData[0].value == "" || parseFloat(formData[0].value) <= 0 ){
        $("#amt-form-group").addClass("has-error"); 
        validation = false;       
    }

    if(formData[1].value == formData[2].value){
        $("#curr-form-group").addClass("has-error");
        validation = false;
    }

    return validation;
}

// making ajax get request
function getResult(formData){
    $.ajax({
        type        : 'GET',
        url         : '/result',
        data        : formData,
        dataType    : 'html',
        encode      : true,        
    })
    .done(function(data){
        $("#currency-ex-result").empty();
        $("#currency-ex-result").append(data);                
        startTimer();
    })
    .fail(function(data){
        $("#currency-ex-result").empty();
        $('#hresult-graph').empty();
        $("#currency-ex-result").append(data.responseText);
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
        if(seconds != 1) $("#timer-refresh").text(seconds + " seconds...");
        else $("#timer-refresh").text(seconds + " second...");        
        if (seconds <= 0) {
            getResult(formData);
            clearInterval(timerId);
        }
    },1000);
}

// switch currency to-from
function currencySwitch(){
    var froCurr = $('#froCurr').find(":selected").val();
    var toCurr = $('#toCurr').find(":selected").val();
    $('#froCurr').val(toCurr);
    $('#toCurr').val(froCurr);
}

// // draw historic data graph
// function drawGraph() {    
//     $.ajax({
//         type    : 'GET',
//         url     : '/hresult',
//         data    :  formData,
//         encode  : true,
//         async   : true 
//     }).done(function(data) {        
//         // create the chart
//         $('#hresult-graph').highcharts('StockChart', {

//             title: {
//                 text: "1 " + formData[1].value + " \u2192 " + formData[2].value
//             },

//             rangeSelector: {
//                  enabled: false
//             },

//             scrollbar: {
//                 enabled: false
//             },

//             series: [{
//                 name: formData[2].value,
//                 type: 'area',
//                 data: data,
//                 gapSize: 5,
//                 tooltip: {
//                     valueDecimals: 4
//                 },
//                 fillColor: {
//                     linearGradient: {
//                         x1: 0,
//                         y1: 0,
//                         x2: 0,
//                         y2: 1
//                     },
//                     stops: [
//                         [0, Highcharts.getOptions().colors[0]],
//                         [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
//                     ]
//                 },
//                 threshold: null
//             }]
//         });
//     })
//     .fail(function(data){
//         $('#hresult-graph').append(data.responseText);
//     });
// }


