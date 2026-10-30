# Automation — The API

Outcome: you can drive JS8Call from
your own program — read its state, ask
its inbox, set its grid — over a plain
TCP connection, and you know the one
setting in this build that does not do
what it says. This is the chapter the
lab could test most completely: the
full session is t04, the client is
`js8call-lab/api_client.py`, and the
quirks are kept in t05.

## Turning it on

The API lives on the Reporting tab
(t02), and it is **off by default** —
every box starts unticked. The lab
enabled:

- **TCP Server API**, hostname
  127.0.0.1, port **2442**;
- **Accept TCP Requests**, without
  which the server listens but does not
  act;
- **Allow setting station information
  from the APIs**, which gates the
  write operations;
- and left Max Connections at 1.

A UDP twin exists on port 2242; the
lab could not exercise it, for a
reason belonging to the sandbox rather
than the program (t08). Nothing binds
to anything but loopback unless you
change the hostname — keep it that
way; this API has no password, and its
trust model is *the machine it runs
on*.

## The shape of a conversation

The protocol could hardly be simpler:
one JSON object per line, UTF-8 text,
over the TCP connection. A request
names a `type` and carries a `value`;
the reply echoes a related type with
the answer in `value` or in a `params`
object, always with an `_ID` counter
the program increments. The lab's
first exchange (t04):

```
>>> {"type": "STATION.GET_CALLSIGN", "value": ""}
<<< {"params":{"_ID":294070192071},"type":"STATION.CALLSIGN","value":"N0CALL"}
```

GET reads; the reply's type drops the
GET. That pattern holds throughout.
An unknown type is answered with
silence — the lab's `BOGUS.WHATEVER`
simply never came back (t04) — so a
client must time out politely rather
than wait forever.

## What the lab asked, and what answered

The working vocabulary the lab
verified, one message at a time (all
of t04):

- `STATION.GET_CALLSIGN` → `N0CALL`;
  `STATION.GET_GRID` → `AA00AA`;
  `STATION.GET_INFO` → the empty string
  (the lab never set an info text);
  `STATION.GET_STATUS` → the status
  template, verbatim and unsubstituted:
  `IDLE <MYIDLE> VERSION <MYVERSION>`.
- `RIG.GET_FREQ` → `{"DIAL":14078000,
  "FREQ":14079500, "OFFSET":1500}` —
  the dial, the offset, and their sum,
  agreeing with the window (chapter 8).
- `RX.GET_TEXT` and `TX.GET_TEXT` →
  the contents of the receive and
  compose panes: empty strings, truly.
- `RX.GET_BAND_ACTIVITY` → empty; the
  band was empty.
- `INBOX.GET_MESSAGES` →
  `{"MESSAGES":[]}` — the inbox,
  honestly bare.
- `MODE.GET_SPEED` → a number, whose
  meaning took a separate experiment
  (below).

And the write: `STATION.SET_GRID` with
value `AA00AB` was answered by a
`STATION.GRID` reply carrying the new
grid, a following GET confirmed it,
and the lab then set it back to
`AA00AA` and confirmed that too. The
write path is real, immediate, and —
because the gate setting was on —
exactly as powerful as it looks: a
program that can set your grid can set
your info and status as well, which is
why the gate exists.

The full message catalogue is larger —
the program's own strings list
`STATION`, `RIG` (including `SET_FREQ`
and `PTT`), `RX` activity events,
`TX.SEND_MESSAGE`, `INBOX.STORE_MESSAGE`,
`LOG.QSO`, `WINDOW.RAISE`, and more.
The lab exercised only reads plus the
one reversible write, and deliberately
never touched the transmit-side types:
an API that can send messages is a
transmitter key, and this guide's lab
does not key transmitters (chapter 1's
rule, applied to software).

## The speed numbers, measured

`MODE.SPEED` is a number with no label,
so the lab labelled it: choose a speed
in the program's own Mode menu, then
ask the API (t05):

| GUI speed | API number |
|---|---|
| Normal | 0 |
| Fast | 1 |
| Turbo | 2 |
| Slow | 4 |

No speed in this build reports 3 — the
numbering has a gap, presumably a
reserved seat. Quote these numbers
only for 2.2.0; another version may
seat its speeds differently, and the
two-minute experiment above is the way
to check yours.

## The quirk: SET_SPEED does not set

`MODE.SET_SPEED` was tried three ways —
the value as a bare number, as a
string, and inside `params` — and
every attempt was answered with a
polite `MODE.SPEED` report of the
*unchanged* speed (t05, verbatim).
The GUI never moved. Whether 2.2.0
wants a fourth shape or simply does
not implement the set, the lab could
not determine from outside; what it
can state is the behaviour, and the
guide teaches GET as proven and
SET_SPEED as answered-but-ineffective
in this build. `STATION.SET_GRID`
proves the write path itself works —
the gap is specific to this message.

## What this is for

With reads alone you can build a
station dashboard (who is on the band,
what the rig is doing, what is in the
inbox), a logger that files activity
your way, or an alert that pings you
when a watched callsign appears. With
writes — on a licensed station, with a
radio attached — the API is a remote
control: frequency, texts, stored
messages. The lab's client is forty
lines of Python with no libraries
beyond the standard one, and it is in
the lab folder for you to take apart.
