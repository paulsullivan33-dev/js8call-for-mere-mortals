# Logging and Spotting Networks

Outcome: you know what JS8Call writes
down, where it writes it, and what it
can tell the world — and what the lab
made sure it did *not* tell the world.
Logging evidence is from the files
themselves (t01, t03, t06); the
spotting behaviour is from the
Reporting tab's own labels (t02),
because the lab switched it off before
it could do anything.

## The activity log: ALL.TXT

Every session appends to
`~/.local/share/JS8Call/ALL.TXT`: a
header line with the date, the dial
frequency and the mode, then one line
per decoded frame — time, frequency,
and the decode itself — the raw diary
of the band as your station heard it.
The lab's entire ALL.TXT, after two
sessions and hours of decoding passes,
is its two headers (t06):

```
2026-10-30 14:06:17  14.078 MHz  JS8
2026-10-30 14:09:14  14.078 MHz  JS8
```

That is what an activity log looks like
for a station that heard nothing, and
it is worth seeing once: the file does
not pad, summarise or invent. On a
working station ALL.TXT grows all day,
and it is the first place to look when
someone asks *did you copy that?* — the
decode is either in the diary or it
did not happen. The same directory
holds the audio `save/` folder, where
recorded WAVs of decode periods land
when saving is enabled — the feature
that produces the very files the `js8`
decoder can re-examine (t07).

## The QSO log

Contacts are logged separately, in the
ordinary amateur way: the **LOG**
button (and the Log menu) records a
completed contact with the details a
logbook wants, and the program can
broadcast contact data to external
loggers — its settings carry servers
for the N1MM and N3FJP conventions
(chapter 6's file shows both, on
loopback ports 2333 and 1100), and the
API exposes `LOG.QSO` for programs
that want to file the contact
themselves. The lab logged no QSO —
you cannot log a contact you did not
have — and says so; the machinery is
described here from its visible
controls and configuration, not from a
transcript.

## Spotting: telling the world who you hear

A **spot** is a report: *my station
decoded your station, at this time, on
this frequency, at this SNR.* Sent to
a collecting network, spots become
maps — the living picture of which
bands are open between which places.
JS8Call's Reporting tab (t02) offers,
in its own words:

- **Enable spotting to reporting
  networks (JS8NET, PSKReporter, etc)**
  — PSK Reporter is the public map most
  operators watch; JS8NET is the JS8
  community's own.
- **Enable spotting @APRSIS messages to
  the APRS-IS network** — a bridge that
  carries specially addressed JS8
  messages into the APRS internet
  system (server `rotate.aprs2.net`,
  port 14580 in the saved settings),
  with a blocklist field for callsigns
  never to spot.

Spots describe *reception*, so a
receive-only station spots lawfully
and usefully — your ears contribute to
the map even if you never transmit.
But a spot carries your callsign and
grid as the receiving station, which is
why the lab's first act in the
Reporting tab was to turn spotting
**off**: the networks would otherwise
have been told, in good faith, that a
station called N0CALL in grid AA00AA
was listening on 20 metres. There is
no such station. Yours exists; spot
with it proudly, and let the map be
true.
