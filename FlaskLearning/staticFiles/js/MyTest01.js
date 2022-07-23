
function clickMe() {
    let result = "Hello world!";
    showTitleInDiv(result);
    return result;
}

function showTitleInDiv(val) {
    $("#div1").text(val);
}