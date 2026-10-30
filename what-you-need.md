# What You Need

Outcome: an honest shopping and
paperwork list for a real JS8Call
station, with the item people forget —
the clock — in its proper place. The
lab had only the first item on this
list, and this chapter is where the
guide is most careful to say so.

## A licence (to transmit)

Amateur radio is licensed everywhere.
In most countries there is a foundation
or entry tier that covers the HF bands
JS8Call lives on, and a higher tier that
opens more power and spectrum; the
exam is a known, studyable thing, and
this series' Ham Radio guide walks
through it. You need no licence, no
permission, and no one's agreement to
*listen* — a receive-only JS8Call
station is lawful anywhere a receiver
is. The moment a transmission carries
your signal, the rules attach: your own
callsign, sent as identification; the
band plan for your region; your
licence's power limits; no encryption,
no commercial traffic, no broadcasting.
JS8Call puts your callsign in every
frame automatically — chapter 6 sets it
— which makes the placeholder warning
worth repeating: **a callsign that is
not yours must never be transmitted**,
and the lab's N0CALL exists precisely so
that no real identity was ever at risk
of it.

## A radio

Any HF transceiver that offers upper
sideband and a way to get audio in and
out will do. Dedicated digital-mode
radios make it easy — a single USB cable
carrying audio both ways plus rig
control — but the mode was designed for
the general case: a radio, an interface,
a computer. You do not need power. JS8's
whole premise is that a few watts into a
modest antenna cross oceans when the
band cooperates; the lab's own ceiling
was zero watts into no antenna, and
real stations routinely work at five.

## An audio path

The radio and the computer exchange
sound, nothing more exotic. The common
arrangements:

- **The radio's own USB audio** — most
  modern HF rigs appear as a sound card.
  Choose that device in the Audio tab.
- **An interface box** — a small unit
  between the radio's accessory socket
  and the computer, isolating grounds
  and setting levels.
- **A plain sound card and cables** —
  workable, with more level-setting and
  more hum to chase.

Whichever you choose, two levels matter:
receive level into the decoder (the
main window's meter is your gauge), and
transmit level into the radio — enough
to make power, never so much that the
radio's ALC is working hard, which
splatters distortion across your
neighbours. Setting those levels is
the real first-evening task of a new
digital station; the software in this
guide is the easy half.

## A computer, and its clock

The computing demand is slight — a
decoder that runs happily on a
Raspberry Pi class machine — but the
**clock** demand is strict. JS8 frames
begin on UTC boundaries (chapter 2), so
your computer's time must be right
within about a second. Let the operating
system sync to network time (it does by
default on most), and check it against
any known-good clock before blaming the
band for silence. The lab machine's
clock was disciplined by the sandbox;
its waterfall rows marched in tidy
ten-second steps for other reasons
(chapter 7), but the discipline is the
same one your station needs.

## Optional: rig control

A CAT connection — serial or USB from
radio to computer, driven by Hamlib —
lets JS8Call read the dial, change
bands with the frequency table, and key
the transmitter cleanly instead of
relying on VOX. It is a convenience and
a safety feature (the program knows the
frequency it is about to use), not a
requirement. Chapter 6 shows the tab
where it is configured; the lab's
stood at None, and the guide does not
pretend otherwise.

## An antenna, and patience

Whatever you have. JS8's sensitivity
forgives compromise antennas to a degree
that surprises voice operators. What it
asks in return is patience: a Normal
frame is fifteen seconds, a thoughtful
exchange is several frames, and the band
opens when it opens. The mode rewards
the operator who puts the kettle on.
