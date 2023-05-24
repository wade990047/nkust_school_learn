function first_String() {
    document.write("這是一句來自JS的文件訊息");
    for(var i=1;i<=6;i++) {
        document.write("<h"+i+">Test<h"+i+">")
    }
    document.getElementById("content").innerHTML = "這是被JS改掉的字串內容";
    document.getElementById("content").style.fontSize = "35px";

}
function greeting() {
    window.alert("草安");
}

function change_text(msg) {
    document.getElementById("content").innerHTML = msg;
}
function bmi() {
    var h = document.getElementById("height").value;
    var w = document.getElementById("weight").value;
    var result = w / (h/100)**2;
    document.getElementById("bmiresult").innerText = result.toFixed(2);
}