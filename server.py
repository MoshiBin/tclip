from flask import Flask, abort, request
from win32clipboard import OpenClipboard, SetClipboardText, CloseClipboard, GetClipboardData
app = Flask(__name__)

@app.route("/get-clip")
def get_clip():
    OpenClipboard()
    content = GetClipboardData()
    CloseClipboard()
    return content


@app.route("/set-clip", methods=["POST",])
def set_clip():
    if "content" not in request.form:
        abort(400) # HTTP 400: Bad Request
    OpenClipboard()
    SetClipboardText(request.form["content"])
    CloseClipboard()
    return "OK"
