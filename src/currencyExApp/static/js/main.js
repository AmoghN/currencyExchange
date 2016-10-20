// global variables
var data = null;
var timerId = null;

$(document).ready(function(){
    startTimer();
    data = $("#currency-ex-form").serializeArray();
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
        $("#currency-ex-result").remove();
        $(".container").append(data);        
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

//switch currency to-from
function currencySwitch(){
    var froCurr = $('#froCurr').find(":selected").val();
    var toCurr = $('#toCurr').find(":selected").val();
    $('#froCurr').val(toCurr);
    $('#toCurr').val(froCurr);
}
