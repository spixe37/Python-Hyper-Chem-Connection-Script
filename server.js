const express = require('express');
const request = require('request');
let spawn = require('child_process').spawn;

let app = express();
app.use(express.static("./static"));

let py    = spawn('python', ['test2.py']);
let data = "window-color red";
let dataString = '';

app.post('/sendmsg', (req, resp) => {
    resp.statusCode = 200;

    let input_text = req.param('msg_input');
    send_cmd(input_text);
    resp.send(input_text);
});

function send_cmd(cmd) {
    py.stdout.on('data', function(data){
        dataString = data;
    });
    
    py.stdout.on('end', function(){
        console.log('Sum of numbers=',dataString);
    });
    py.stdin.write(cmd);
    py.stdin.end();
};

app.listen(80, () => {
    console.log("Server started");
});