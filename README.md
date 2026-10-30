# JS8Call for Mere Mortals

Some signals are too weak to hear. Down
in the noise of an HF band, below the
level where headphones find anything at
all, a computer can still pull out a
message — a whole sentence, typed by
someone on another continent, carried on
a signal weaker than the static around
it. **JS8Call** is the program that does
this with a keyboard attached: real
conversations, typed both ways, over
**JS8**, a digital mode built from the
bones of FT8, the weak-signal mode that
changed HF operating. Where FT8 trades
fixed, terse exchanges — callsign, grid,
signal report, goodbye — JS8Call trades
*text*: questions, answers, news,
greetings, and a small network protocol
of heartbeats, relays and stored
messages that keeps working when the
person you want is not on the air.

This guide explains how JS8 works, how
to install JS8Call and set up a station,
how to read its waterfall, and how its
messaging network fits together. Then it
does the part most guides skip: it is
honest about its own laboratory. The lab
that wrote this guide had **no radio, no
antenna, and no licence to transmit** —
it is a computer in a rack, and nothing
in it was ever connected to a
transmitter. So JS8Call was installed,
started, configured, listened to its own
silence, and driven through its
automation API, and every one of those
steps is in the transcripts. What the
lab could not do — hear a real station,
decode a real transmission, send so much
as a carrier — it did not fake, and
chapter 15 says exactly where the line
falls.

One rule belongs here, before anything
else, because everything in this guide
hangs on it: **transmitting on the
amateur bands requires an amateur radio
licence**, in every country, and your
callsign — your real one, issued to you —
is the identity you transmit with.
Receiving needs no licence at all, and a
great deal of this guide is useful with
the transmitter never switched on. The
lab's station is invented on purpose: a
placeholder callsign, **N0CALL**, and a
placeholder grid, in a program that was
never attached to anything that could
put it on the air. When you set up your
own station, the placeholder is where
*your* callsign goes.

## What this guide covers

- [**What JS8Call is**](what-js8call-is.md) —
  the mental model: FT8's ears, a
  keyboard's voice, and a network that
  passes notes
- [**JS8 — the mode**](js8-the-mode.md) —
  tones, frames and forward error
  correction: how a sentence survives a
  signal you cannot hear, and the four
  speeds
- [**The moving parts**](the-moving-parts.md) —
  the application, the separate decoder
  process, the sound card, the rig
  control, and the files it keeps
- [**What you need**](what-you-need.md) —
  the radio, the interface, the computer,
  the clock — and the licence, honestly
  itemised
- [**Installing JS8Call**](installing-js8call.md) —
  the packages, what is inside them, and
  the version evidence
- [**First run and configuration**](first-run-and-configuration.md) —
  the dialog that greets you, your
  callsign and grid, and the settings
  file where they land
- [**The main window and waterfall**](the-main-window-and-waterfall.md) —
  every pane of the window the lab
  photographed, and how to read a
  waterfall that is showing you noise
- [**Frequencies and band activity**](frequencies-and-band-activity.md) —
  the eleven dial frequencies from the
  program's own table, offsets, and the
  heartbeat sub-band
- [**Sending and receiving messages**](sending-and-receiving.md) —
  the compose box, directed and group
  messages, and the frame clock that
  governs both directions
- [**Messages, heartbeats, relays and the inbox**](message-types-and-network-features.md) —
  the network layer: heartbeat
  announcements, automatic queries,
  relays through third stations, groups,
  and store-and-forward
- [**Automation — the API**](automation-the-api.md) —
  the JSON-over-TCP interface, exercised
  end to end by the lab's own client,
  quirks included
- [**Logging and spotting networks**](logging-and-psk-reporter.md) —
  the activity log, the QSO log, and the
  reporting networks that map who hears
  whom
- [**Recipes**](recipes.md) — a receive-only
  listening post, an API-driven station
  dashboard, a store-and-forward drop,
  and the checks to run before your
  first transmission
- [**The neighbours**](the-neighbours.md) —
  WSJT-X and FT8, Fldigi, FSQ, and the
  other ways keyboards meet HF
- [**Limits**](limits.md) — what a lab
  with no radio cannot prove, what the
  mode cannot do, and where the program
  is rough
- [**Troubleshooting**](troubleshooting.md) —
  the sound-device errors, the silent
  waterfall, the API that will not
  answer, and the traps this guide's lab
  fell into
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Operating. This guide teaches the
software and the mode; it does not
teach HF operating practice, antenna
building, or contest technique, and it
cannot — its lab never made a contact.
Getting licensed has its own guide in
this series. It also does not cover
building JS8Call from source, the
experimental forks of the program, or
digital modes beyond the comparisons in
chapter 14.

## How to use this guide

Read chapters 1 to 3 for the model
before installing anything — knowing
which part decodes, which part talks to
the radio, and which part is just a
filing cabinet turns later confusion
into a named problem. Chapters 5 and 6
get you a running, configured program;
chapter 7 teaches the window. The lab's
transcripts live in
`js8call-lab/transcripts/`, its API
client is `js8call-lab/api_client.py`,
and its screenshots are in
`js8call-lab/` beside them — every claim
in the chapters that carries a (t00)
style reference can be checked there.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [WSJT-X for Mere Mortals](https://paulsullivan33-dev.github.io/wsjtx-for-mere-mortals/)
- [Ham Radio for Mere Mortals](https://paulsullivan33-dev.github.io/ham-radio-for-mere-mortals/)
- [FreeDV for Mere Mortals](https://paulsullivan33-dev.github.io/freedv-for-mere-mortals/)
- [Fldigi for Mere Mortals](https://paulsullivan33-dev.github.io/fldigi-for-mere-mortals/)
- [RTL-SDR for Mere Mortals](https://paulsullivan33-dev.github.io/rtl-sdr-for-mere-mortals/)
- [Linux for Mere Mortals](https://paulsullivan33-dev.github.io/linux-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/js8call-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/js8call-for-mere-mortals/blob/main/LICENSE-CODE).
