# The Main Window and Waterfall

Outcome: you can read every part of
JS8Call's main window — including the
waterfall, the part that frightens
newcomers — and you know what the lab's
window honestly showed: a working
receiver listening to a silent, virtual
band. The screenshot this chapter reads
is `js8call-main-window.png` in the lab
folder, taken from the real program
(t03).

## The top strip: where am I?

Across the top, in the largest type,
the **dial frequency**: 14.078 000 in
the lab's window — the 20-metre JS8
frequency, the program's home band.
Under it, the **offset**: 1500 Hz, the
audio position inside the passband
where this station is listening and
would transmit. Centre-top, the station
identity as saved — N0CALL – AA00AA —
with the UTC clock and date beneath it;
JS8Call lives on UTC, and so, while
operating, do you.

To the right, a cluster of buttons:
**RX** and **TX** indicators, **SPOT**
and **LOG** (chapter 12), **TUNE** (a
steady carrier for adjusting the
radio — the lab never pressed it, on
principle), and a blue readout of the
decode state. In the lab it read
`FAST+MULTI+AUTO+CONF`, which chapter 2
and the Mode menu unpack: the transmit
speed is Fast, MULTI decoding of all
speeds is on, and autoreply-with-
confirmation is enabled. The button is
a summary of the Mode menu, not a
control in itself — clicking it, the
lab verified, changes nothing (t05).

## The panes

Three working areas sit under the strip.

**Band activity** (left) is where
decoded frames land: columns for
offset, age, SNR, and the message
itself. Each decode cycle adds lines;
the age column lets old decodes fade
out of relevance. In the lab it stayed
empty, and empty is what truth looked
like (t06).

**Incoming and outgoing messages**
(centre) is the conversation pane: what
was said to you, what you sent, and —
in the box beneath with its placeholder
*TYPE YOUR OUTGOING MESSAGES HERE* — the
compose area of chapter 9. Under it, a
row of buttons: CQ, REPLY, SNR, INFO,
STATUS, Saved, Directed, Deselect,
Send, Halt. The middle four are the
automatic queries of chapter 10; they
light up when a station is selected.

**Callsigns heard** (right) is the
station list: every callsign decoded,
with age, SNR, offset, and name or
comment if known. In the lab it held a
single row — `@ALLCALL`, the standing
group address of chapter 10 — because
the program lists the group even when
no station has been heard.

## The waterfall

The waterfall is a scrolling map:
horizontal axis is audio frequency
(offset), vertical axis is time, new
rows arrive at the top, brightness is
signal strength. A JS8 signal is a thin
bright thread, steady for its frame's
length; noise is a dark field of
nothing much.

The lab's waterfall deserves an honest
reading, because it is a photograph of
organised silence. Its rows are
labelled in ten-second steps —
14:09:20, 14:10:50, each marked 20m —
because in MULTI mode the program draws
a row per decode pass, and the fastest
speed ticks every ten seconds. The
green horizontal lines are the pass
boundaries; the red vertical line near
1550 Hz marks where the station's own
ear is pointed, near the 1500 Hz
offset. The field is black because the
input was a null sink's monitor: perfect
electronic silence, no static, no band
noise, no stations. A real waterfall
glows faintly blue-green with noise and
speckles with signals; learning to read
one starts with knowing what *nothing*
looks like, and this is it.

Two gauges flank it. On the left, the
**receive level meter** in dB — the one
that answered 81 dB to the lab's test
tone (t06). Keep yours, on a real
station, in its green: too low starves
the decoder, too high clips. On the
right, a transmit-side level slider.
At the very bottom, a status bar: the
current state word (Receiving, or
Decoding while a pass runs), the mode
(JS8), and a decode counter — n/10,
the passes completed in the current
cycle — the program's quiet heartbeat,
visible in every lab screenshot,
steadily counting passes over silence.
