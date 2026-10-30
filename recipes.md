# Recipes

Outcome: four working arrangements
built from this guide's chapters. Each
recipe says which of its steps the lab
actually executed — most of the
plumbing was — and which wait for a
real station.

## 1. A receive-only listening post

*Lab status: every step executed except
connecting a receiver.*

1. Install JS8Call (chapter 5) and set
   your callsign and grid (chapter 6) —
   a listening station still identifies
   itself to its own logs, and to the
   spotting networks if you enable them.
2. Feed it receiver audio: a radio on
   the JS8 dial frequency (chapter 8),
   its audio out to the device you pick
   on the Audio tab. No radio? A
   software-defined receiver on the
   same computer works — route its
   audio through a virtual device, the
   same PulseAudio trick the lab used
   with its null sink (t03).
3. Watch the level meter while the band
   plays (chapter 7): green, not
   pinned.
4. Leave MULTI decoding on and walk
   away. The callsigns pane becomes
   your log of who the band carried
   today; `ALL.TXT` keeps the evidence
   (chapter 12).
5. Optionally, turn spotting on
   (chapter 12) and contribute your
   reception to PSK Reporter's map.

No licence is needed for any of this,
anywhere. It is the finest way to
learn the mode's rhythms before ever
transmitting.

## 2. A station dashboard from the API

*Lab status: executed in full — this is
t04 with a loop around it.*

1. Enable the TCP API exactly as
   chapter 11 describes (loopback only,
   Accept on, station-info gate your
   choice).
2. Take `js8call-lab/api_client.py` and
   keep the reads: `STATION.GET_CALLSIGN`,
   `RIG.GET_FREQ`, `RX.GET_BAND_ACTIVITY`,
   `INBOX.GET_MESSAGES`.
3. Poll them on a timer into whatever
   display you like — a file, a web
   page, a desk clock. Remember the
   protocol's manners: one JSON object
   per line, a timeout on every read,
   and no reply at all for a type the
   program does not know.
4. Do not build on `MODE.SET_SPEED`;
   in 2.2.0 it answers without acting
   (t05). Read the speed, by all means —
   and translate it with the measured
   table in chapter 11.

## 3. Prove your audio path with a tone

*Lab status: executed — t06.*

Before blaming the band, the decoder,
or the guide, prove the plumbing:

1. Generate a plain sine tone at your
   operating offset (the lab used
   1500 Hz, half scale, a few seconds —
   any audio tool can make one).
2. Play it into the device JS8Call
   records from — in the lab, a player
   aimed at the null sink whose monitor
   was the program's input.
3. Watch the receive meter. It should
   swing decisively (81 dB for the
   lab's half-scale tone). A moving
   meter proves device selection,
   routing, and level in one glance.
4. Confirm the honest negative: the
   tone must produce **no decode and no
   ALL.TXT entry**. If a steady carrier
   ever "decodes", something in your
   chain is inventing signals, and
   nothing downstream can be trusted.

On a real station the same test, done
with the radio's own audio path, is
the fastest known separator of *radio
problems* from *software problems*.

## 4. A store-and-forward drop for a net

*Lab status: assembled from verified
parts; the on-air steps are documented
(chapter 10), the local steps executed
(inbox in t03, API in t04).*

For a club or emergency net whose
members keep different hours:

1. Members agree a group name and list
   it in their Station settings
   (chapter 10), and agree the dial
   frequency and speed.
2. The drop station — one that is on
   the air most — leaves autoreply on,
   with its idle timeout set generously,
   and relaying enabled.
3. A member with traffic for an absent
   member stores the message with the
   drop station; the drop's inbox
   (`inbox.db3`, chapter 3) holds it as
   data, inspectable and back-up-able.
4. When the addressee next appears —
   heartbeat first, as always — the
   stored message is delivered, and
   the drop's API lets a dashboard show
   what is waiting for whom.

## 5. Before your first transmission

*Lab status: the lab never reaches this
recipe. It is the guide's parting gift
to your real station.*

1. Your own callsign and true grid are
   in the settings — not a placeholder,
   not a club call you are not using,
   yours (chapter 6).
2. The clock is synced and verified
   against a known source (chapter 4).
3. You have listened on this offset
   long enough to know it is clear, and
   your power is as low as the contact
   needs.
4. Transmit audio level is set so the
   radio makes power without working
   its ALC hard (chapter 4).
5. Heartbeats, autoreply, and spotting
   are set the way you would defend in
   public — because on the air, they
   are public.
