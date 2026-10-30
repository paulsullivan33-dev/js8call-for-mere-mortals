# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's station is an invented placeholder, labelled as
   such wherever it appears.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 15 names what the lab could
   not do: no radio, no antenna, no licence, no decode of a
   real signal, nothing transmitted, rig control unexercised —
   and what the tool itself cannot do, including the API
   message this build answers without obeying.
8. **The ethics rule is in the text, early.** Transmitting on
   the amateur bands requires a licence and your own callsign;
   the placeholder callsign used by the lab is never presented
   as usable, chapter 1 and chapter 4 state the rule before any
   procedure depends on it, and the lab itself never keyed a
   transmitter, a transmit audio path, or the API's send-side
   message types.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a shared Ubuntu 24.04 sandbox with no
sound hardware, no radio, and a policy of blocking all UDP
sends. JS8Call **2.2.0** (Debian package
`js8call 2.2.0+ds-5build2`, 5.9 MB) was downloaded with
lab-private apt state, unpacked with `dpkg-deb -x` — never
installed system-wide — and run unmodified under Xvfb with an
isolated HOME. Screenshots were captured from the real windows
with ImageMagick; the GUI configuration was driven with
xdotool, typing into the application's own dialog. All
transcripts live in `js8call-lab/transcripts/`; the API client
is `js8call-lab/api_client.py`; three screenshots are in
`js8call-lab/` beside them.

Run for real, with transcripts as evidence:

- Package contents and version; `ldd` clean; the absence of
  any sample audio in the package (t00).
- First run headless: the configuration dialog on first start,
  the `js8` decoder as a separate shared-memory process
  (full command line quoted), the files created, and the
  verbatim sound-device failures of a machine with no sound
  hardware (t01).
- Configuration through the real dialog: placeholder station
  (N0CALL / AA00AA), spotting switched off, the TCP API
  enabled; the settings file growing from 2 to 160 lines with
  `MyCall`/`MyGrid`/TCP keys in plain text; the application
  listening on 127.0.0.1:2442 (t02).
- A PulseAudio null sink created for the lab; on restart,
  zero audio errors, the Audio tab naming `lab.monitor` /
  `lab` as the program's chosen devices, the configuration
  read back from disk (window identity, F2 dialog), and the
  inbox database `inbox.db3` with its `inbox_v1` table (t03).
- The TCP API end to end with the lab's own client: fifteen
  requests and their verbatim JSON replies, including the
  frequency arithmetic (dial + offset), the empty inbox, and
  the SET_GRID write changed and changed back (t04).
- The API speed numbering measured against the GUI's Mode
  menu (Normal 0, Fast 1, Turbo 2, Slow 4), and
  `MODE.SET_SPEED` refusing to act in three message shapes,
  verbatim (t05).
- The receive audio path: a lab-made 1500 Hz tone played
  into the virtual device; the input meter answering 81 dB;
  ALL.TXT afterwards containing only its session headers —
  no decode claimed or faked (t06).
- The `js8` decoder CLI over a 15-second 12 kHz WAV of the
  same tone: mode A pass, `<DecodeFinished> 0` (t07).
- The complete JS8 frequency table (eleven bands) decoded
  from the program's own saved configuration (t08).

Documented only — described from the project's documentation
and the program's visible controls, not run, and the text
does not claim otherwise:

- **Decoding a real JS8 transmission.** No genuine sample
  recording ships with the package or the project, nothing
  was received off air (no receiver, no antenna), and the
  lab would not generate one with a transmitter path.
- **Transmitting anything**, including the API's send-side
  message types, CQ, TUNE, heartbeat transmissions, and
  autoreply on the air.
- **Rig control against hardware**: CAT, PTT, band changes.
  The Radio tab is described as found (Rig: None).
- **On-air network behaviour**: relays hopping real traffic,
  heartbeat acknowledgements, store-and-forward delivery,
  propagation, and what a busy band looks like.
- **The UDP API**: the sandbox refuses UDP sends outright
  (`PermissionError`, t08); the TCP API carries the same
  message set and is the verified route.
- **Spotting as a sender**: the Reporting tab's controls and
  network names are quoted verbatim, but spotting was
  switched off for the whole lab so no report was ever made.
- **Logging a QSO**: no contact existed to log; the log
  machinery is described from its controls and settings.
- The neighbour tools of chapter 14 — characterised, not run
  or benchmarked for this guide.

Fixtures are this guide's own and deliberately generic: a
placeholder callsign and grid square, a 1500 Hz sine tone at
two sample rates, and an empty band. No real station was
named, heard, imitated, or transmitted to.
