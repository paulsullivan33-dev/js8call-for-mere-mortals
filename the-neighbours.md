# The Neighbours

Outcome: where JS8Call sits in the
family of keyboard-and-radio tools, and
what each neighbour does that it
doesn't (and the reverse). These
neighbours are characterised from
their documentation and this series'
own guides — not re-run for this
chapter — except where the relationship
is the program's own admitted ancestry.

## WSJT-X and FT8 — the parent

JS8Call is a WSJT-X derivative, and it
does not hide it: the source tree, the
decoder's shape, the settings habits
are all inherited, and the package's
own README says so (t00). FT8 itself is
the opposite philosophy in the same
signal clothing: fixed exchanges,
machine-paced, a contact in about a
minute, no conversation possible or
intended. If you want the most contacts
per hour from the weakest signals, FT8
is the tool and WSJT-X is its home
(and this series' WSJT-X guide its
manual). If you want to *say* something,
that is the gap JS8Call was built to
fill. Most stations run both.

## Fldigi — the other keyboard

Fldigi is the sound-card modes
workhorse: dozens of modes (PSK31,
RTTY, Olivia, and more), free-form
keyboard conversation, macros, logging
— a generation older in spirit and far
broader. Its modes mostly need signals
a human can almost hear; JS8's error
correction reaches far deeper into the
noise, at the price of speed and of
JS8Call's single-mode focus. Fldigi
conversations are live typist-to-typist
in a way JS8's frame clock is not; JS8
conversations survive conditions that
would erase Fldigi's modes entirely.
This series' Fldigi guide proves its
modes with an off-air loopback — the
test this guide's lab rules did not
permit itself.

## FSQ and FSQCall — the ancestor

FSQ is a fast, ears-optional keyboard
mode for VHF and HF local work, and
FSQCall built directed calls, relaying,
and message storage on top of it —
the direct ancestors of chapter 10's
features, as JS8Call's own history
acknowledges (chapter 1). FSQ needs
audible-ish signals and rewards local
nets; JS8 took the protocol ideas down
to the noise floor. If your group is
all in one county, FSQ's speed is a
joy; if it is scattered across an
ocean, JS8 is the inheritance spent
well.

## The wider family, briefly

- **WSPR** — also from the WSJT stable:
  not messaging at all, but beacons —
  who heard whom, at what strength,
  worldwide. The propagation scientist's
  tool.
- **APRS** — packet radio's position
  and short-message network, mostly
  VHF, with an internet backbone.
  JS8Call touches it at one edge, the
  `@APRSIS` spot bridge of chapter 12.
- **Winlink** — actual email over HF,
  with infrastructure and gateways;
  the tool for *deliver this message to
  the internet*, where JS8Call's inbox
  is *hold this message until the band
  delivers it*.
- **FreeDV** — digital *voice* squeezed
  into an SSB channel: the other answer
  to "what else can error correction do
  down there?"
- **Meshtastic and the LoRa meshes** —
  the same social idea (keyboards,
  relays, store-and-forward) on
  unlicensed spectrum with little
  radios, no licence and no ionosphere.
  Different physics, recognisable
  culture.

## Choosing

Reach for JS8Call when the message
matters more than the contact count,
when the band is poor, when the group
is scattered and patient, and when a
network that leaves notes for absent
friends sounds like the point — because
it is. Reach for its neighbours when
you want speed, voice, volume, or a
different layer of the stack. The
waterfall does not care; it will show
you all of them, one thin thread at a
time.
