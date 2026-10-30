# Messages, Heartbeats, Relays and the Inbox

Outcome: the network layer of JS8Call —
the part that makes it more than a slow
chat — piece by piece, with each piece
marked as the lab found it: visible in
the program's own interface and
settings (verified), or described from
the documentation (labelled).

## Kinds of message

Everything on a JS8 band is one of
three kinds, and the panes of chapter 7
exist to sort them.

A **directed message** is addressed to
one callsign. The sender's program
frames it for that station; every
station hears it (chapter 8), but only
the addressee's program files it as
theirs. Selecting a callsign and using
the Directed button (chapter 9) is how
you write one.

An **undirected message** is addressed
to the room — a CQ, a general comment —
and lands in everyone's activity pane.

A **group message** is addressed to a
named group, written with an @ sign:
`@ALLCALL` is the built-in group of all
stations, which the program lists in
your callsigns pane even in total
silence (the lab's one permanent row,
t03). You may define your own groups
in the Station settings — the field
the lab photographed reads *Callsign
Groups (comma separated)*, with a
checkbox to sit `@ALLCALL` out — and
stations join the groups they list.
Groups are how nets and clubs carve a
room of their own out of a public band.

## Heartbeats: the network's pulse

A **heartbeat** is a short automatic
transmission — the template in the
lab's settings reads `HB <MYGRID4>` —
sent periodically to announce *this
station is on the air, here is its
grid*. Heartbeats live in the 500–1000
Hz sub-band (chapter 8) and give the
network its map: from heartbeats alone,
your callsigns pane learns who is
around, where, and how strong.

The Networking & Autoreply settings
(t02) hold the manners: heartbeats
pause while you are in a QSO; stations
you list are never acknowledged; and a
companion option, the heartbeat
**acknowledgement**, lets your program
answer a heartbeat automatically with
your report of their signal — the
`ACK` toggle in the Mode menu, which
sat greyed in the lab because heartbeat
networking itself was off by default
and the lab left it off: a placeholder
station does not announce itself, even
to nobody.

## Automatic queries: the program answers

Some directed messages are *questions
the program answers by itself*, and
the main window gives them buttons —
**SNR**, **INFO**, **STATUS** sit
between REPLY and Saved for exactly
this reason (chapter 7). The set, from
the program's documentation:

- `SNR?` — how are you hearing me? The
  answering program replies with the
  SNR it measured on your last frame.
- `INFO?` — answered with the station
  info text from settings.
- `STATUS?` — answered with the status
  template (`IDLE <MYIDLE> VERSION
  <MYVERSION>` in the lab's settings).
- `GRID?` — answered with the grid.
- `AGN?` — say again: repeats the last
  message.
- Closing courtesies — `QSL?`, `RR`,
  `73`, `SK` — acknowledged and logged
  in the flow of a contact.

This is the FSQ inheritance in
JS8Call's blood: a station can be
*usefully present* — answering where it
is and how it hears you — while its
operator is making tea. **Autoreply**
extends the idea: with it on, the
program can answer directed messages
with your stored reply text, under the
rules the lab read in t02 — confirm
before sending if you ask it to, only
for callsigns you list, never for ones
you exclude, and off entirely after an
idle timeout (60 minutes as shipped)
so an unattended station eventually
falls politely silent.

## Relays: messages that hop

A message may be **relayed**: sent to a
station in range, which retransmits it
toward a station neither of you can
quite reach. The relay marker is the
`>` character — the settings name it
exactly, in the option *Disable message
relay (>) when autoreply is enabled*
(t02). The settings also carry a
`RelayOFF` switch. Relaying is the
network thinking like a network:
propagation is patchy, stations are
scattered, and a message that hops once
can cross a gap no single transmission
could. Relayed traffic is also why
heartbeats matter — you cannot choose
a hop you have not heard.

## The inbox: store and forward

The deepest of the network features,
and the one whose furniture the lab
could inspect directly. A message can
be **stored** at a station for a
callsign that is not currently on the
air; when that callsign appears, the
holding station delivers it. The
receiving side of the system is the
**station inbox**: messages held for
you, collected and kept locally. In
the lab's data directory the inbox is
a SQLite database, `inbox.db3`, with a
single table `inbox_v1` (t03) — a file
you can open with any SQLite tool and
read, which the lab did at the schema
level. Through the API (chapter 11),
the inbox is fully exposed:
`INBOX.GET_MESSAGES` answered the lab
with an empty list — `{"MESSAGES":[]}`
(t04) — and `INBOX.STORE_MESSAGE` is
the corresponding write, present in
the program's vocabulary though the
lab, having no station to store a
message *from* and no business inventing
one, left it unexercised.

Taken together — heartbeats for
presence, queries for status, relays
for reach, an inbox for the absent —
JS8Call is less a modem with a chat
window than a small, patient postal
system that happens to run on radio.
That is the idea its author set out to
test, and on the air, by all reports,
it works. The lab's part was to verify
that every piece of that machinery is
really there in the program, named,
wired, and — through the API —
reachable. It is.
