# Troubleshooting

Outcome: the failures this lab actually
met, each with the evidence and the
way out — plus the two failures your
station is most likely to meet that
the lab, having no radio, could only
prepare for.

## "Error in Sound Output / Sound Input" at first run

*Symptom (t01):* the configuration
dialog opens over error boxes —
*An error opening the audio output
device has occurred*, *Requested input
audio format is not supported on
device* — and the startup log fills
with ALSA and PulseAudio complaints.

*Cause:* there is no usable sound
device. On the lab machine there was
no sound hardware at all; on yours it
is more often a device that is busy,
unplugged, or owned by another
program.

*Fix:* give the program a device and
check the Audio tab names it. The lab
started PulseAudio with a null sink
and the errors vanished entirely on
the next start (t03). On a real
station: plug the interface in
*before* starting JS8Call, and if the
radio provides USB audio, confirm the
operating system can see it before
blaming the program.

## The waterfall is black and the meter never moves

*Symptom:* decode passes tick over
(the counter in the status bar), the
clock is right, and nothing — no
noise, no meter, no decodes.

*Work through it in order:*

1. **Is there audio at all?** Run
   chapter 13's tone test. The lab's
   meter sat at the bottom over its
   silent virtual device and jumped to
   81 dB the moment sound arrived
   (t06). A dead meter is an audio
   routing problem, full stop.
2. **Is the right device chosen?** The
   Audio tab shows what the program
   *actually* opened — the lab read
   `lab.monitor` there to confirm its
   routing (t03).
3. **Is the decoder alive?** JS8Call
   decodes in a separate process
   (chapter 3). If `js8` is not in the
   process list beside `js8call`, the
   program is a window without ears;
   restart it and watch for the child
   process.
4. Only after all three: suspect the
   band. Bands do close. ALL.TXT's
   headers will show the program was
   listening the whole time (t06).

## Decodes happen for other people, not for you — the clock

*Symptom (documented, prepared for in
chapter 4):* the waterfall shows
signals, but they start mid-row and
nothing decodes.

*Cause:* your computer's clock is off.
JS8 frames begin on UTC boundaries;
a machine seconds adrift hears every
frame in pieces. This is the most
common *invisible* failure in all the
FT8-family modes.

*Fix:* turn on network time sync, then
verify against an independent source
and restart the program. The waterfall
rows should align with the frame
boundaries afterwards.

## The API does not answer

*Symptom:* your client connects — or
cannot — and no JSON comes back.

*Check, in order (all from t02/t04):*

1. **Is it enabled?** Both *Enable TCP
   Server API* and *Accept TCP
   Requests* must be on; one without
   the other listens mutely or not at
   all. Confirm from outside:
   `ss -ltn | grep 2442` should show
   the program listening on 127.0.0.1.
2. **One connection only.** Max
   Connections defaults to 1; a
   forgotten client of yours may be
   holding the seat.
3. **Are you speaking JSON lines?**
   One object per line, newline
   terminated. The program answers
   well-formed requests immediately.
4. **Is your type real?** A misspelt
   or unknown type gets *silence*, not
   an error (t04's BOGUS exchange).
   Test with `STATION.GET_CALLSIGN`,
   the API's hello-world.
5. **Writes refused?** Anything that
   *sets* — grid, info, status — needs
   *Allow setting station information
   from the APIs*, and in this build
   `MODE.SET_SPEED` will still not
   act: that one is the program, not
   you (t05).

## The UDP API never responds (in a sandbox)

*Symptom (t08):* UDP datagrams to port
2242 vanish, and the test program
itself reports
`PermissionError: [Errno 1] Operation not permitted`.

That error is the *machine* refusing
to send UDP at all — a sandbox and
some container networks do this. It
tells you nothing about JS8Call. Use
the TCP API, which carries the same
messages, or move the experiment out
of the sandbox.

## The settings seem to vanish

*Symptom:* you set the station details
and they are gone next start.

*Reality, from t01/t02:* the settings
file begins as a two-line stub and is
only written when the dialog is saved
with OK — closing the dialog any other
way keeps nothing. And the program
keeps *named configurations* (the
file's `[MultiSettings]` section):
make sure the configuration you edited
is the one selected. When in doubt,
read the file — `MyCall=` and
`MyGrid=` are plain text (chapter 6).

## The lab's own traps, for honesty's sake

Twice, the lab's automation killed the
process it was inspecting: a `pkill`
pattern matched the command line of the
shell running it, `js8`'s parent among
the casualties. The lessons are
generic and worth printing: signal
processes by exact PID or exact name;
never pattern-match a process list
with a string your own command line
contains; and check `pgrep` output
before believing a restart worked.
