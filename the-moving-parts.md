# The Moving Parts

Outcome: you can name each part of a
JS8Call station, say which job it does,
and point to the file or process where
it lives. Everything in this chapter was
observed in the lab — the parts are few
enough to hold in one picture.

## The application

`js8call` itself is a Qt program: the
window, the waterfall, the settings, the
message logic, the network protocol,
the API. On the lab machine it was one
of exactly two executables in its
package (t00), about six megabytes of
Debian package, and it holds no secrets:
its configuration is a plain text file
you will meet in chapter 6.

## The decoder

The second executable is `js8`, and the
division of labour is the single most
useful fact in this chapter. The
application does not decode. It starts
`js8` as a **separate process** and
feeds it audio through a shared-memory
region; the decoder does the heavy
mathematics — FFTs, synchronisation,
error correction — and hands back text.

The lab photographed the arrangement in
the process list (t01):

```
js8 -s JS8Call -w 1 -m 1 \
    -e .../usr/bin \
    -a .../.local/share/JS8Call \
    -t /tmp/JS8Call
```

Reading it: `-s JS8Call` names the
shared-memory key; `-a` gives the data
directory the decoder may write to;
`-t` its scratch space. The same `js8`
program also works alone, decoding
recorded WAV files from the command
line — chapter 11's neighbour and t07's
subject. When JS8Call seems deaf, this
split is your first diagnostic gift:
is the decoder process alive at all?

## The sound device

Between the program and the radio there
is no radio at all — there is a **sound
device**. The radio's receiver audio
flows into the computer as sound; the
computer's transmitted tones flow out
the same way. JS8Call neither knows nor
cares whether the device is a USB
headset chip inside a modern rig, a
separate interface box, or — in the lab
— a PulseAudio **null sink**, a virtual
device that accepts audio and discards
it, whose monitor output served as the
microphone (t03). The Audio settings
tab chooses input and output devices by
name; the lab's dialog read, in the
program's own words, Input
`lab.monitor`, Output `lab`.

This is also where **levels** live. The
main window's vertical meter shows the
incoming audio level in dB, and the
decoder wants it neither starved nor
slamming: the lab pushed a half-scale
test tone through its virtual device
and watched the meter answer 81 dB
(t06), the only signal that ever
reached its decoder.

## Rig control

Optionally, a library called **Hamlib**
lets the program steer the radio itself:
read and set the dial frequency, key
the transmitter, follow band changes.
In the lab the Radio tab stood at
Rig: None, PTT method VOX, its Test CAT
button greyed quiet — a faithful picture
of a station with no radio (t02). With
a rig chosen, the same tab offers CAT
control over serial or network, PTT by
CAT command, DTR or RTS line, and the
split-operation choices WSJT-X users
will recognise. Chapter 15 is plain
that none of this was exercised against
hardware here.

## The files

A JS8Call station keeps a small,
legible estate. In the lab's isolated
home directory (t01, t03):

- `~/.config/JS8Call.ini` — every
  setting, in Qt's INI dialect, under a
  `[Configuration]` section. Chapter 6
  reads it.
- `~/.local/share/JS8Call/ALL.TXT` — the
  **activity log**: a header line each
  session, then a line per decode.
- `~/.local/share/JS8Call/inbox.db3` — a
  SQLite database with one table,
  `inbox_v1`: the store-and-forward
  inbox of chapter 10, kept as data you
  could inspect with any SQLite tool.
- `~/.local/share/JS8Call/save/` — where
  recorded audio goes when saving is
  enabled.
- `timer.out` — a scratch file the
  decoder side maintains.

Nothing else hides elsewhere. Backing up
a station is copying two directories.

## The network services (optional)

Two outward connections exist, both off
by default or switched off by the lab:
**spotting** — reporting the stations
you decode to JS8NET and PSK Reporter,
so the world can see who hears whom —
and an **APRS-IS** feed for `@APRSIS`
messages. Chapter 12 covers them. They
are gravy, not plumbing: the radio
network of chapter 10 works with the
internet unplugged, which is rather its
reason to exist.
