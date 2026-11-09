# v30 presentation and source credits

Both movies reuse the real, inspected native Telegram Android v29 captures.
Only the external framing/background changed in v30. Touch feedback comes
from actual MotionEvents in the original take. No new app build, synthetic
UI animation, optical flow or fake gesture was inserted for this revision.

Pixel frame: original Pixel 10 Pro hardware at
https://screenshots.guru/frames/png/pixel-10-pro-frame.png , offered at
https://screenshots.guru/frames under Apache 2.0 / Android Open Source Project.
The device, lens, side buttons, corners and metallic finish retain the provider's
original geometry. The complete native capture is uniformly fitted; a little
black padding handles its different aspect ratio. No UI is stretched or cropped.
The standalone frame is not included in this repository.

Background and compositing are procedural. No other concept's pixels are copied.
White tap feedback is native captured feedback. The references supplied for
review are Multi-Action Swipe by @riveaux and Video message shapes by @mazurov;
neither their code nor their media is incorporated here.

The photo film shows fictional Daniel Orlov, stock gallery/preview, the custom
draft tray and local grouped-message insertion. Its simulated upload completion
is not network transport. The native preview's own reorder gesture is not in
the current film. Photo fixtures include Unsplash Paris imagery; the custom
status is ResistanceDog-16794 artwork from https://t.me/nft/ResistanceDog-16794 .
Names and ownership are fictional demo data.

The player film shows fictional Alina Vetrova. It plays the same native queue,
swipes and release-only seek as v29. Audio is the exact already-validated v29
encoded soundtrack, copied without re-encoding, using original track PCM aligned
to measured playback transitions. It is not pristine emulator-capture PCM and
does not demonstrate iOS audio. Track/cover references:

- Daft Punk — Get Lucky: https://music.apple.com/us/album/random-access-memories/617154241
- The Weeknd — Blinding Lights: https://music.apple.com/us/album/after-hours/1499385848
- Tame Impala — The Less I Know the Better: https://music.apple.com/us/album/currents/1440838039

The source package does not redistribute those original media files. Its generator
creates original abstract replacement photos and synthesized test tones instead.
Telegram-derived code retains GPL v2 or later and upstream copyright notices.
Translation exports are Telegram Android localization resources.
