# Limits

Outcome: a plain account of what this
guide could not prove, what JS8Call
cannot do, and where the program is
rough — so that nothing earlier in the
guide is standing on more than it
should.

## The lab's limits (the important list)

This guide's laboratory had no radio,
no antenna, no sound hardware, and no
licence. Everything it claims is
measured inside those walls, and the
walls exclude a great deal:

- **No decode of any real signal is
  claimed.** The decoder ran — over
  silence in the application (t03, t06)
  and over a laboratory tone as a file
  (t07) — and produced no decodes,
  because it was given nothing
  decodable. Package and project ship
  no sample recording (t00, t07), and
  the guide does not present anyone
  else's recording as its own result.
- **Nothing was transmitted.** Not a
  frame, not a tune carrier, not a
  heartbeat. The transmit path — the
  modulator, PTT, ALC behaviour, what
  a sent message looks like from the
  other end — is described from the
  interface and documentation only.
  The API's transmit-side message
  types were likewise left untouched
  (chapter 11).
- **Rig control was never exercised.**
  The Radio tab stood at Rig: None for
  every minute of the lab. CAT, PTT
  keying, and Hamlib against real
  hardware are unverified here.
- **On-air behaviour is documented,
  not observed.** Propagation, pile-up
  etiquette, what a busy band's
  waterfall looks like, how relays
  perform in practice — chapter 10's
  mechanics are verified as *present
  in the program*; their life on the
  air is reported from the project's
  documentation.
- **The UDP API is unverified** from
  this sandbox, which blocks UDP sends
  outright (t08). The TCP API, which
  carries the same messages, is fully
  verified.
- **Nobody heard anything.** All audio
  claims are measurements — a meter
  reading of 81 dB, files' sample
  rates — not listening. The guide
  never says a signal *sounded* like
  anything.

## The mode's limits

- **Speed.** Turbo's ~40 WPM is the
  ceiling; Normal is 16. JS8 is a
  medium for sentences, not files.
- **It is not private.** Every frame
  is decodable by every listener, and
  amateur rules forbid encryption in
  any case.
- **It depends on the clock.** Frame
  timing is unforgiving; a drifting
  computer is a deaf and mute station.
- **It needs the band.** Below the
  noise floor is not below the laws of
  propagation: a closed band carries
  nothing, at any correction strength.

## The program's limits, as found

- **`MODE.SET_SPEED` does not set the
  speed** in 2.2.0, by any message
  shape the lab tried; it reports the
  current speed instead (t05). The
  speed *numbering* also has a gap at
  3 in this build.
- **Unknown API types fail silently** —
  no error frame, no log line the lab
  could find. Clients must use
  timeouts.
- **The API has no authentication.**
  Its safety is entirely in the
  loopback binding; the settings make
  wider binding possible, and this
  guide advises against it without a
  very good reason.
- **First run on a machine without a
  sound device is noisy** — repeated
  error dialogs layered over the
  configuration window (t01). The
  program recovers completely once a
  device exists (t03), but the first
  impression is a poor one.
- **The settings file is only partly
  human.** Plain keys for the facts you
  care about; opaque Qt binary variants
  for geometry, colours, and the
  frequency table, which the lab had
  to decode byte by byte to read in
  full (t08).
