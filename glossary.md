# Glossary

**Activity log (ALL.TXT)** — the file
in JS8Call's data directory recording
each session and every decoded frame,
in time order. The station's diary.

**Age** — in the activity and callsign
panes, how long since a frame or
station was last heard; JS8Call ages
entries out so the panes show the
living band, not its history.

**ALC** — automatic level control in a
transmitter. Transmit audio driven too
hard makes the ALC work — and makes
your signal dirty. Set levels so it
barely stirs.

**APRS-IS** — the internet side of
APRS, the packet-radio position and
messaging network. JS8Call can forward
`@APRSIS` messages and spots into it.

**Autoreply** — JS8Call answering
directed messages by itself, under the
operator's rules: confirmation,
allowlists, and an idle timeout.

**Band activity** — everything the
decoder rescues from the band, whether
or not it is addressed to you; also
the name of the pane that shows it.

**CAT** — computer-aided transceiver
control: the radio taking orders —
frequency, mode, PTT — over a cable,
here via Hamlib.

**CQ** — the general call: *I am here
and open to contact.* In JS8Call, a
template message and a button.

**Decoder** — the part that turns audio
into text. In JS8Call, a separate
program, `js8`, fed through shared
memory.

**Decode depth** — how hard the
decoder strains at faint candidates:
more depth, more sensitivity, more
CPU.

**Dial frequency** — the frequency the
radio is tuned to; a JS8 station's
true frequency is the dial plus its
audio offset.

**Directed message** — a message
addressed to one callsign (or a group),
as opposed to an undirected message to
the whole band.

**FEC (forward error correction)** —
redundant mathematical structure added
to a transmission so the receiver can
repair damage without asking for a
repeat. The heart of every weak-signal
mode.

**Frame** — one fixed-length JS8
transmission, beginning on a UTC
boundary: 30, 15, 10, or 6 seconds by
speed.

**FT8** — the weak-signal mode JS8 is
built from: fixed, terse exchanges at
15-second pace, from the WSJT-X suite.

**Grid (Maidenhead locator)** — a
compact code for a place on Earth,
four or six characters; stations
exchange grids as a matter of course.

**Group** — a named set of callsigns
addressed together with an @ name;
`@ALLCALL` is the built-in group of
everybody.

**Hamlib** — the library JS8Call uses
to control radios: one interface, a
long list of supported rigs.

**Heartbeat** — a short periodic
automatic transmission announcing a
station's presence and grid, sent in
the 500–1000 Hz sub-band.

**Inbox** — the store-and-forward
mailbox: messages held for a station
until it appears. Locally, a SQLite
database (`inbox.db3`).

**JS8** — the mode: 8-FSK tones,
FT8-family error correction, free-text
frames at four speeds.

**JS8NET** — the JS8 community's
spotting network; see *spotting*.

**MULTI** — the decoder option that
listens for all four speeds at once.

**Null sink** — a virtual PulseAudio
device that discards what it receives;
its monitor output served as the lab's
microphone.

**Offset** — a station's audio
frequency inside the passband, in
hertz above the dial; also where it
appears on the waterfall.

**PSK Reporter** — the public network
and map collecting spots: reports of
who decoded whom, where, and how
strongly.

**PTT** — push-to-talk: the act of
keying the transmitter, by hand, VOX,
or CAT command.

**Relay** — retransmitting a message
onward toward its addressee, marked
with `>`; how JS8 traffic hops past
the edge of one station's range.

**SNR** — signal-to-noise ratio, in
decibels. JS8 decodes at strikingly
negative SNRs — signals far weaker
than the noise around them.

**Spotting** — reporting the stations
you decode to a collecting network,
building the public picture of
propagation.

**Store and forward** — leaving a
message with a station that will hold
it and deliver it when the addressee
next appears; see *inbox*.

**UTC** — coordinated universal time,
amateur radio's clock. JS8 frames
begin on its boundaries, everywhere on
Earth at once.

**VOX** — voice-operated transmit: the
radio keys itself when it hears audio.
The simplest PTT method, and the one
that keys on a sneeze.

**Waterfall** — the scrolling display
of a band: frequency across, time
down, brightness for strength. The
weak-signal operator's home screen.

**WSJT-X** — the weak-signal suite by
K1JT and collaborators, ancestor and
parent project of JS8Call.
