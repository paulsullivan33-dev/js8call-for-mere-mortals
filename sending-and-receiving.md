# Sending and Receiving Messages

Outcome: the shape of a JS8Call
conversation — how text gets from the
compose box into frames, and from
frames into your panes — with the
lab's boundary stated at the top: the
lab received (silence) for real, and
**never transmitted**. Every transmit-
side step in this chapter is therefore
described from the program's interface
and documentation, and labelled as
such; the receive-side mechanics are
the ones the lab exercised in t03 and
t06.

## Receiving: the program does the work

Reception needs nothing from you. The
decoder runs its passes at every frame
boundary — the bottom status bar's
counter ticking over, as in every lab
screenshot — and anything it rescues
from the noise is filed three ways at
once (chapter 8): the frame into band
activity, the sender into the callsigns
pane, and anything addressed to you —
your callsign, or a group you belong
to — into your message pane, with a
notification if you enabled one. The
lab's decoder ran those passes for
hours over a silent input; its
`ALL.TXT` log shows the session headers
and nothing else (t06), which is the
receive pipeline working correctly on a
band with nobody on it. Leave a real
station running overnight and the same
pipeline fills the panes by itself.

Two settings shape the listening.
**Decode depth** trades CPU for
sensitivity — how hard the decoder
strains at the faintest candidates —
and the **MULTI** option (chapter 2)
widens each pass to all four speeds.
Both were at their working defaults in
the lab: MULTI on, and the decoder
process running with the patience
settings t01 recorded.

## Composing: the box and its buttons

Sending starts in the compose box
under the message pane — the one whose
placeholder reads *TYPE YOUR OUTGOING
MESSAGES HERE*. You type ordinary text.
There is no form to fill and no fixed
exchange; the program will frame,
correct, and schedule whatever you
write. Around the box, the controls
the lab photographed:

- **Directed / Deselect** — aim the
  message. Select a callsign in the
  right-hand pane and your text is
  *directed* to that station; undirect
  it and it goes to the room.
- **Send** — queue the text for the
  next transmit frame boundary.
  Transmissions begin on the frame
  clock (chapter 2), not at the click:
  part of JS8's discipline is that
  everyone speaks in turn, on the
  boundaries.
- **Halt** — stop a transmission in
  progress.
- **CQ** — send the CQ template from
  your station settings (`CQ CQ CQ
  <MYGRID4>` by default).
- **Saved** — recall texts you stored
  on the Saved Messages tab.

Longer messages are split across
frames automatically; the receiving
station reassembles them. Nothing in
the interface hurries you — the mode's
whole character is in that lack of
hurry.

## A conversation's rhythm (documented)

What the lab could not do is have one,
so this paragraph is from the program's
documentation and the mode's customs,
not from a transcript. A typical
exchange: you call CQ or answer one;
the other station replies; you trade
sentences, each taking a frame or
several; signal reports are exchanged
with the one-button queries of chapter
10 rather than typed; and the contact
is logged (chapter 12) when it
completes. Either side may change
speed mid-conversation as conditions
move. The typing pace of the mode —
sixteen words a minute at Normal —
shapes the culture: short sentences,
plain words, no rush, and a certain
telegraphic courtesy that operators
coming from FT8's stopwatch find
restful.

## The one experiment not run

The lab's rules forbade the obvious
final test — it never pressed Send,
CQ, or TUNE, even with a dummy audio
device and a placeholder call, because
the guide's station does not exist and
its callsign must never be keyed into
any transmitter path, real or virtual,
by a guide that teaches other people's
stations. On your station, the honest
first transmission is the same one
every digital operator makes: a CQ, on
a clear offset, with your own callsign,
at low power, having first listened
long enough to know the offset is
clear. Chapter 13's recipes end with
the checklist for that moment.
