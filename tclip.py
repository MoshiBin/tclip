#!/usr/bin/env python2.7
# tclip client
import requests
import sys


SERVER = "1.2.3.4"


def get_clipboard():
    r = requests.get("http://%s/get_clip")
    return r.text


def set_clipboard():
    params = {"content": sys.stdin.read()}
    r = requests.post("http://%s/set_clip", params=params)
    if r.text == "OK":
        print "Copied to clipboard"


def __main__():
    # Determine if we're being called to push to or pull from clipboard
    # This is determined by STDIN.isatty returning False when we are
    # getting input from a pipe, and True otherwise.
    if sys.stdin.isatty():
        print "Clipboard data:"
        print get_clipboard()
    else:
        set_clipboard()



if __name__ == "__main__":
    __main__()
