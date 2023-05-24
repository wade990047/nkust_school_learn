function greeting() 
{
    window.alert("Good day!");
}

function changeText(obj) {
    var msg = obj.textContent;
    document.getElementById("content").innerHTML = msg;
}

function bmi() {
    var h = document.getElementById("height").value;
    var w = document.getElementById("weight").value;
    var result = w / (h/100)**2;
    document.getElementById("bmiresult").innerHTML = result.toFixed(2);
}

function changeTV() {
    var tv = document.getElementById("tvselect");
    var tvText = tv.options[tv.selectedIndex].text;
    var vid = tv.value;
    const prestr= '<iframe width="560" height="315" src="https://www.youtube.com/embed/';
    const poststr = '" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>';
    var tvstr = prestr + vid + poststr;
    document.getElementById("tvtitle").innerHTML = tvText;
    document.getElementById("tvdisplay").innerHTML = tvstr;
}

function clockTick() {
    var currentTime = new Date(),
        month = currentTime.getMonth() + 1,
        day = currentTime.getDate(),
        year = currentTime.getFullYear(),
        hours = currentTime.getHours(),
        minutes = currentTime.getMinutes(),
        seconds = currentTime.getSeconds(),
        text = (year + "/" + month + "/" + day + ' ' + hours + ':' + minutes + ':' + seconds);
    // here we get the element with the id of "date" and change the content to the text variable we made above
    document.getElementById('date').innerHTML = text;
  }
setInterval(clockTick, 1000);