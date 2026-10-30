# Installing JS8Call

Outcome: JS8Call on the machine, its
version proven, and a clear picture of
what the installation contains. The
lab's exact route — a package unpacked
by hand, nothing installed system-wide —
is in t00; a normal install on your own
machine is simpler, and both are given.

## The ordinary way

JS8Call is free software from the
project's own site (js8call.com), with
installers for Windows and macOS and
packages or build instructions for
Linux. On Debian and Ubuntu it is in
the distribution's universe repository,
which is where the lab's copy came
from:

```bash
sudo apt install js8call
```

That places two programs on the system
— `js8call` and `js8`, the decoder —
plus documentation and a desktop entry.
Start it from the menu or by typing
`js8call`. Windows and macOS users get
the same program from the project's
installer; nothing in the following
chapters depends on the difference.

## What the lab actually did

The lab machine's package state is
shared with other work, so the guide
was written against the Ubuntu package
**downloaded but not installed**, then
unpacked into a lab directory and run
from there (t00). The procedure is
worth keeping in the guide because it
doubles as an inspection of what an
install contains:

```bash
apt-get install --download-only -y js8call   # with lab-private apt state
dpkg-deb -x js8call_2.2.0+ds-5build2_amd64.deb ~/js8call-root
```

The unpacked tree held two executables
(`usr/bin/js8call`, `usr/bin/js8`), the
project's README and install notes, a
changelog, a copyright file, an icon —
and, noted for later, **no sample audio
whatsoever** (t07 leans on that
absence). A check with `ldd` confirmed
every shared library the binary needs —
Qt 5, FFTW, Hamlib, SQLite — already
resolves on the machine; on a bare
system the package manager fetches them
as dependencies in the ordinary way.

## Proving the version

The lab's evidence is the package
itself:

```
Package: js8call
Version: 2.2.0+ds-5build2
Description: Amateur Radio Digital Mode
             providing weak signal messaging
```

2.2.0 is the project's version; `+ds`
and the rest are Debian's packaging
suffixes. Newer releases exist — the
project has continued past 2.2 — and the
guide's behaviour notes are versioned
accordingly: everything in chapters 6
to 12 was observed on this 2.2.0 build,
and the one place version really bites,
the API's speed numbering, is flagged
where it appears (chapter 11, t05). On
your machine, the program's Help → About
dialog states its version in the
ordinary way.

## First launch expectations

Started with an empty home directory,
JS8Call does two things immediately: it
opens its **Configuration dialog** over
the main window — callsign and grid
empty and highlighted, asking to be
filled — and it creates its files:
`~/.config/JS8Call.ini` and the data
directory `~/.local/share/JS8Call/`
(t01). If your machine has no usable
sound device, it will also complain
about that, in dialogs and in its log,
exactly as the lab's did. The next
chapter takes the dialog field by
field.
