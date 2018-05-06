function send_message() {
    let msg_input = document.getElementById("msg_input");
    let msg_text = msg_input.value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
        }
        if (this.readyState == 4 && this.status == 404) {
            console.log("Connection lost");
        }
        
    };
    xhttp.open("POST", "sendmsg?" + "msg_input=" + encodeURIComponent(msg_text), true);
    xhttp.send();
    

    msg_input.value = '';
    msg_input.focus();
}
send_button.onclick = send_message;