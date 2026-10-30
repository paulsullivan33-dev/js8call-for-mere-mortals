# Frequencies and Band Activity

Outcome: you know where JS8 lives on
each band — the program's own table,
not a copied chart — and how to think
about the slice of spectrum the
waterfall shows you.

## The dial frequencies

JS8Call keeps a table of one **dial
frequency** per band, all USB, and hops
between them from the main window's
band control. The Frequencies settings
tab shows the table (t02); the complete
list, decoded from the program's saved
configuration (t08), is:

| Band | Dial (MHz) |
|---|---|
| 160m | 1.842 |
| 80m | 3.578 |
| 40m | 7.078 |
| 30m | 10.130 |
| 20m | 14.078 |
| 17m | 18.100 |
| 15m | 21.078 |
| 12m | 24.915 |
| 10m | 28.078 |
| 6m | 50.318 |
| 2m | 144.178 |

The pattern is easy to hold: on most HF
bands the JS8 dial sits just above the
FT8 watering hole — 7.078 beside FT8's
7.074, 14.078 beside 14.074 — so a band
you already know how to find for FT8
needs one small step upward. The lab's
window lived on 14.078, the default
home, and its ALL.TXT headers record
the fact twice: `14.078 MHz JS8` (t06).

These frequencies are conventions, not
allocations: the band plans of your
region govern where digital modes may
sit, and the program's table is tagged
by IARU region for that reason. The
table is also editable, and the
Frequencies tab carries a **Frequency
Schedule** — automatic band changes at
set UTC times, a feature unattended
listening posts use to follow the day's
propagation. The lab left it empty.

## Dial, offset, and where you really are

A JS8 "frequency" is two numbers. The
dial sets the radio; the **offset** —
0 to about 3000 Hz — sets your place
inside the receiver's passband, and
your true emitted frequency is dial
plus offset (t04's arithmetic:
14.078 MHz + 1500 Hz). Stations spread
themselves across the passband by
choosing different offsets, dozens of
conversations sharing one dial setting
without sharing a channel. The waterfall
(chapter 7) is the map of that sharing:
each thread of light is one station at
one offset.

Choosing an offset is etiquette as
much as technique: pick a clear spot,
and remember that the bottom few
hundred hertz have a special resident.

## The heartbeat sub-band

Offsets from **500 to 1000 Hz** are the
**heartbeat sub-band** — the region the
program's Networking settings name
explicitly, with an option to allow
heartbeat transmissions outside it
(t02). Heartbeats (chapter 10) cluster
there so that the network's housekeeping
traffic — stations announcing *I am
here, this is my grid* — has a known
home that monitoring stations can watch,
without sprinkling announcements across
the conversational spectrum. When you
see regular short traces low in the
passband, ticking away at frame
boundaries, you are probably watching
the heartbeat network breathe.

## What "band activity" means

The left pane's name is literal: it is
the band's activity as decoded —
every frame the decoder rescued, in
time order, whether or not it was
addressed to you. JS8 is a broadcast
medium in the original sense: all
stations in range hear all frames, and
the program sorts them for you — into
the activity pane (everything), the
callsigns pane (who), and your message
pane (what concerns you). There is no
tuning away from a conversation you are
not part of, short of changing bands;
there is only the filter of your
attention, which chapter 10's groups
help organise. In the lab, the pane's
emptiness across hours of decode passes
was the correct and complete picture of
its band: a virtual receiver, on a
virtual band, in a rack, hearing
nothing — and reporting exactly that.
