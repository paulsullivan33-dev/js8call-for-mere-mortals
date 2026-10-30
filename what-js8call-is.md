# What JS8Call Is

You are listening to a shortwave band at
night. In the headphones there is hiss,
a crackle, perhaps a voice so faint it
might be imagination. Somewhere in that
hiss, another station is typing. Not
sending Morse, not speaking — typing,
in complete sentences, at a power level
you could match with a handful of
batteries. Your computer finds the
message, checks it, repairs the parts
the noise ate, and puts the words on
your screen. You type an answer. It
goes back the same way. That is the
whole experience **JS8Call** exists to
provide.

JS8Call is a free, open-source program
for **weak-signal keyboard-to-keyboard
messaging** on the amateur HF bands. It
was created by Jordan Sherer, KN4CRD,
released to the public in April 2019,
and built — openly and with credit — as
a derivative of **WSJT-X**, the
weak-signal suite by Joe Taylor, K1JT,
and his collaborators. It is licensed
under the GPLv3. The program's own
description of itself, in the package
the lab installed (t00), is worth
quoting because it is unusually modest:
it calls itself "an experiment to test
the feasibility of a digital mode with
the robustness of FT8, combined with a
messaging and network protocol layer for
weak signal communication on HF". The
experiment worked. People use it daily.

## Three ideas stacked

It helps to see JS8Call as three ideas
stacked on each other.

The bottom layer is a **signal** — JS8
itself, a way of packing text into audio
tones so robust that the receiving end
can recover it from far below the noise
floor, at signal levels where a human
ear hears nothing at all. Chapter 2
takes it apart.

The middle layer is a **conversation**.
FT8, JS8's parent, exchanges fixed
tokens in a rigid 15-second dance —
callsigns, a grid square, a number,
farewell, done. JS8Call throws the
script away. What you type is what is
sent: free text, as long as you like,
spelled the way you spell. It feels less
like a contest exchange and more like a
very slow, very patient chat room whose
members may be oceans apart.

The top layer is a **network**. JS8Call
stations announce themselves with
heartbeat transmissions, answer simple
questions automatically ("what is my
signal report?" is answered by the
*program*, not the operator), relay
messages through third parties, and hold
messages for stations that are not
currently on the air — a store-and-
forward inbox spread across the whole
band. Chapter 10 takes that layer apart
piece by piece.

## The rule that comes first

Everything transmitted on the amateur
bands must carry the sending station's
callsign, and transmitting at all
requires an amateur radio licence. This
guide's lab had neither a licence to use
nor a radio to use it with, so the lab
never transmitted — not a CQ, not a
heartbeat, not a test tone into an
antenna. Its JS8Call ran with an
invented placeholder callsign, N0CALL,
and a sound device that exists only
inside the computer. Chapter 4 lists
what a real station needs, licence
included. If you take one sentence from
this guide onto the air, take this one:
the placeholder is a placeholder — never
let it, or anyone else's callsign, leave
a transmitter of yours.

## A first taste

On a real station, a JS8Call contact
looks undramatic, which is the point.
The waterfall shows thin traces in the
noise, and lines of decoded text appear
in the activity pane — a callsign, an
offset, words somebody typed. This
guide prints no example of such a line,
because the lab never decoded one, and
printing a plausible invention would
break the promise the transcripts keep.
What a first taste really looks like,
for the lab, is chapter 7: the real
window, the real frequency, the real
clock, and an honest empty band. On
your station, with an antenna, that
pane fills.

## Where it came from

The lineage matters because the
documentation assumes it. WSJT-X
(2001 onward) proved that computers
could decode signals far weaker than
any ear; FT8 (2017) made it fast enough
to take over the bands. KN4CRD proposed
stretching FT8's frame to carry long,
free-form messages in 2017, borrowed the
store-and-forward and directed-message
ideas from FSQCall, and rebuilt the
WSJT-X machinery around a messaging
interface. JS8Call is the result: WSJT-X
underneath — the same decoder family,
the same waterfall habits, the same
settings-file shape — with a different
idea about what the exchange is *for*.

## What you need, in one paragraph

A computer (this guide's lab used a
small shared Linux machine with no sound
card at all, which chapter 15 treats as
the cautionary tale it is), an HF
transceiver that can do upper sideband,
a way to move audio between radio and
computer, and — to transmit — a licence
and an antenna. Chapter 4 is the honest
shopping list, including the part where
the clock on your computer turns out to
be radio equipment.
