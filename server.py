from flask import Flask, request, render_template
from time import sleep
import pyhcs
app = Flask(__name__)

@app.route("/sendmsg")
def sendmsg():
    sleep(0.1)
    if not pyhcs.connect():
        return
    sleep(0.1)
    pyhcs.exec_text("window-color white")
    # msg_input =  request.args.get("msg_input")
    # pyhcs.exec_text(msg_input)
    return "msg_input"

@app.route("/")
def index():
    return render_template("index.html")

def main():
    if not pyhcs.connect():
        return
    app.run(host="0.0.0.0", port=8080)

if __name__ == '__main__':
    main()