#!/usr/bin/env python3
"""A minimal client for the JS8Call TCP API (127.0.0.1:2442).

Sends one JSON message per line, exactly as the API expects, and
prints everything the application sends back, verbatim. Used by
the guide's lab to prove the API against the real application.
Nothing here transmits: the requests only read station state,
read the (empty) receive panes, and set the grid square twice --
once to a neighbouring square and once back -- to prove the
write path works.
"""

import json
import socket
import sys
import time

HOST, PORT = "127.0.0.1", 2442


def drain(sock, seconds=1.5):
    """Collect whatever arrives within `seconds` of quiet."""
    sock.settimeout(seconds)
    buf = b""
    try:
        while True:
            chunk = sock.recv(65536)
            if not chunk:
                break
            buf += chunk
            sock.settimeout(0.4)
    except socket.timeout:
        pass
    return buf.decode("utf-8", "replace")


def ask(sock, msg_type, value=""):
    msg = {"type": msg_type, "value": value}
    line = json.dumps(msg)
    print(f">>> {line}", flush=True)
    sock.sendall((line + "\n").encode())
    time.sleep(0.3)
    reply = drain(sock)
    for rline in reply.splitlines():
        if rline.strip():
            print(f"<<< {rline}", flush=True)
    if not reply.strip():
        print("<<< (no reply)", flush=True)
    print(flush=True)


def main():
    sock = socket.create_connection((HOST, PORT), timeout=5)
    print(f"connected to {HOST}:{PORT}", flush=True)
    greeting = drain(sock, 2.0)
    for gline in greeting.splitlines():
        if gline.strip():
            print(f"<<< (unsolicited) {gline}", flush=True)
    print(flush=True)

    ask(sock, "STATION.GET_CALLSIGN")
    ask(sock, "STATION.GET_GRID")
    ask(sock, "STATION.GET_INFO")
    ask(sock, "STATION.GET_STATUS")
    ask(sock, "MODE.GET_SPEED")
    ask(sock, "RIG.GET_FREQ")
    ask(sock, "RX.GET_TEXT")
    ask(sock, "TX.GET_TEXT")
    ask(sock, "RX.GET_BAND_ACTIVITY")
    ask(sock, "INBOX.GET_MESSAGES")
    ask(sock, "STATION.SET_GRID", "AA00AB")
    ask(sock, "STATION.GET_GRID")
    ask(sock, "STATION.SET_GRID", "AA00AA")
    ask(sock, "STATION.GET_GRID")
    ask(sock, "BOGUS.WHATEVER")

    sock.close()
    print("connection closed", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
