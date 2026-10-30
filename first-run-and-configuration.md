# First Run and Configuration

Outcome: a configured station — real or,
in the lab's case, honestly placeholder —
with the settings saved, the settings
file read, and one restart survived.
Evidence: t01, t02, t03, and the
screenshots in `js8call-lab/`.

## The dialog that greets you

JS8Call opens its Configuration dialog
on first run, and the first tab asks for
the only two facts the program cannot
guess (t01, and the filled dialog in
`js8call-config-filled.png`):

- **My Callsign** — your callsign. The
  lab typed `N0CALL`, the placeholder
  this guide uses wherever a callsign
  must stand. Yours goes here, exactly
  as issued.
- **My Maidenhead Grid Locator** — your
  station's position in the Maidenhead
  grid, four or six characters. The lab
  used `AA00AA`; the field uppercases
  what you type.

Below them sit the **station messages**:
templates the program uses when it
speaks for you. The defaults the lab
photographed are instructive — CQ
Message `CQ CQ CQ <MYGRID4>`, Reply
Message `HW CPY?`, and Station Status
`IDLE <MYIDLE> VERSION <MYVERSION>`,
where the angle-bracket tokens are
substituted at send time. A **Callsign
Groups** field (chapter 10) and a
checkbox to sit out the `@ALLCALL` group
complete the tab. Nothing here is
complicated; all of it is identity, so
take the minute to get it right.

## The other tabs, in one pass

The dialog has eight tabs. Chapter by
chapter, the ones that matter:

- **General → Behavior**: aging and
  display habits; safe to leave alone.
- **General → Networking & Autoreply**:
  the heartbeat and autoreply rules of
  chapter 10 — pause heartbeats during
  a QSO, autoreply on at startup, ask
  before sending autoreplies, an idle
  timeout of 60 minutes.
- **Radio**: rig choice (Hamlib's list),
  CAT serial settings, PTT method —
  VOX, CAT, DTR, RTS — and the Test CAT
  button. With Rig set to None, as the
  lab left it, the rest sleeps.
- **Audio**: the input and output sound
  devices by name, each Mono or by
  channel, plus the recording directory.
- **Reporting**: QSO logging options,
  the spotting networks of chapter 12,
  and the API switches of chapter 11.
- **Frequencies**: the dial-frequency
  table of chapter 8 and an optional
  schedule for automatic band changes.
- **Saved Messages, Notifications, UI**:
  stored texts, sound alerts for events
  (a new call, a directed message, a
  heartbeat), and fonts and colours.

## Saving, and the file that proves it

Clicking OK writes everything to
`~/.config/JS8Call.ini`. The lab watched
the file grow from a two-line stub to
160 lines (t02). The lines that matter
read as plainly as a settings file ever
does:

```ini
[Configuration]
MyCall=N0CALL
MyGrid=AA00AA
TCPEnabled=true
TCPServer=127.0.0.1
TCPServerPort=2442
AcceptTCPRequests=true
```

—and beside them the machinery: CAT
ports, PTT method, heartbeat message
`HB <MYGRID4>`, the frequency table,
window geometry, colours as binary Qt
variants. You are not meant to edit this
file by hand, but knowing it is text —
greppable, back-up-able, diff-able — is
worth a great deal the first time a
setting seems to vanish. Two of the
lab's later proofs are exactly that:
the complete frequency list of chapter 8
was decoded out of this file (t08).

## The read-back test

A setting is only real if the program
reads it back. The lab restarted
JS8Call against the same home directory
and changed nothing (t03). The main
window came up titled, in effect, by
the file: **N0CALL – AA00AA** at the top
centre, the API listening again, and
the reopened dialog showed the same
callsign and grid in its fields. The
restart also carried the lab's audio
from broken to working — a virtual
PulseAudio device appeared between runs
— which is chapter 7's opening scene
and troubleshooting's first entry.

## What to set before anything else

On a real station, in order: callsign,
grid, audio devices (play the radio
through them and watch chapter 7's
meter), rig if you have CAT, and then —
before any thought of transmitting —
your clock against a known source and
your transmit audio level against
chapter 4's warning. The lab set a
sixth thing a real station should think
twice about: it turned spotting **off**,
because reporting a placeholder station
to a public network would be littering.
Your real station may leave it on,
proudly; chapter 12 explains what it
does.
