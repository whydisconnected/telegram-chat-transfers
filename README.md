# Chat Transfers — Telegram Android concepts

Photo drafts that preserve the chat, and a music queue controlled from the chat.
Native Telegram UI on Android; the films use real interaction captures. This
package contains both feature code and its isolated, signed-out demo host.

[Photo draft demo](photos.mp4) · [Music queue demo](player.mp4)

Latest movies (v34) are freshly captured on a physical1080x2410 test-emulator
display, matching the Pixel10Pro display aspect. Daniel retains the Paris
background; Alina uses a minimal dark background. Original Pixel geometry is
stationary and the metal highlights are toned down. Status glyphs follow the
user's mockup and side-inset references; native SystemUI glyphs were hidden
reversibly during capture. Native Telegram edge fading is visible beneath
that decorative status overlay. See CREDITS.md for provenance.


## What the concepts do

- Select photos in the native attachment gallery and stage them by tapping the
  exposed chat or dragging the selection into it. Read/scroll the conversation
  with the selection retained, expand the tray, reorder/remove photos, return
  to the gallery and its existing album preview, then create an ordered album.
- Drag an audio message onto the mini-player to queue it without interrupting
  playback. Inspect the native queue, swipe tracks, hold to reveal artwork and
  seek, then collapse it.

## Apply to the exact upstream revision

Base: https://github.com/DrKLO/Telegram at
`f2908b14133bbffbf7ab04f641ecb5bfaf533242` (12.10.6).

```sh
git clone --recursive https://github.com/DrKLO/Telegram.git
cd Telegram
git checkout f2908b14133bbffbf7ab04f641ecb5bfaf533242
git submodule update --init --recursive
git apply --check /path/to/this-repo/telegram-android.patch
git apply /path/to/this-repo/telegram-android.patch
python -m pip install Pillow
python /path/to/this-repo/prepare_fixture_assets.py .
```

The fixture generator also needs FFmpeg on PATH (`--ffmpeg /path/to/ffmpeg`
is supported). It creates every required media file locally: original abstract
photos, covers, avatars, status art and quiet synthesized audio. The three
commercial recordings, album covers and third-party gift artwork in the films
are **not** redistributed. Generated media uses the same filenames and duration
contracts; it is intentionally visually/audibly different from the films.

Use the upstream Android build prerequisites, your own application configuration
and debug signing. No account credentials, signing files or private service
configuration are included. Build the full debug app:

```sh
./gradlew :TMessagesProj_App:assembleAfatDebug
adb install -r /path/to/the/resulting/debug.apk
adb shell am start -n org.telegram.messenger.beta/org.telegram.ui.LaunchActivity \
  --ez transfer_demo true --ez transfer_touch_feedback true
# Photo conversation:
adb shell am start -n org.telegram.messenger.beta/org.telegram.ui.LaunchActivity \
  --ez transfer_demo true --ez transfer_touch_feedback true \
  --ez transfer_photo_caption true
```

Adjust the installed package if you customize `APP_PACKAGE`. Use a fresh,
signed-out debug installation. The host refuses activated accounts. The
upstream gallery may require the normal local media permissions.

## Source map

The patch adds seven complete Java files at their original source paths:

| File | Purpose |
|---|---|
| `Components/ChatTransferState.java` | Local ordering, selection and queue state |
| `Components/ChatTransferView.java` | Drag feedback, pending tray, reorder and springs |
| `Components/ChatTransferAlbumView.java` | Native album preview rendering adapter |
| `ChatTransferNativeActivity.java` | Native ChatActivity with fictional local messages |
| `ChatTransferFixtureData.java` | Temporary media, theme/locale fixtures and restoration |
| `ChatTransferNativeChrome.java` | Native picker/player adapters and gesture binding |
| `ChatTransferDemoActivity.java` | Touch indicator and legacy demo support |

Integration changes are in `AnimatedLinearLayout`, `AudioPlayerAlert`,
`ChatAttachAlert`, `FragmentContextView`, `SeekBarView`, `TrashView`, and one
debug-only entry in `LaunchActivity`. Unrelated drafts grouping and profile
music experiments from the working checkout are excluded.

## Current native changes

- ChatActivity owns its unmodified native edge fades, wallpaper source, opacity
  and layout. The fixture no longer replaces their drawables after layout or
  substitutes a solid black source. No gradient or status rectangle is added
  in compositing. Both edges are checked from the opening native frame.
- The local demonstration upload completes in950ms. This is fictional transport
  timing and makes no claim about real Telegram network upload speed.
- Tray expansion is critically damped, track labels enter over24dp/240ms,
  the photo drag uses a simpler path and the extra queue scroll is omitted.
- The emulator display aspect removes artificial lower padding. The captured
  native gesture handle is retained near the physical bottom of the glass.

## Verification and limits

The current v34 checkout built and ran on the owned Android emulator. Native
selection, cancellation, incremental adding, tray reordering, local album
creation, playback/queue/seek were captured and inspected. Exported v34 movies use those fresh native captures with stationary Pixel framing. A 60 fps export is not a
claim of uniformly 60 fps native rendering.

This isolated patch passes application and resulting-file hash checks against
the exact base. The standalone state checks can be run without Android:

```sh
javac -d /tmp/chat-transfer-tests \
  TMessagesProj/src/main/java/org/telegram/ui/Components/ChatTransferState.java \
  /path/to/this-repo/ChatTransferStateTest.java
java -cp /tmp/chat-transfer-tests ChatTransferStateTest
```

The separated package with generated replacement media has not received a new
full Android build/runtime pass. It is a reviewable interaction prototype, not
a production integration: message/upload completion is a local fixture;
reflection binds native views to synthetic data. Real account transport, queue
persistence, accessibility alternatives and multiple device configurations
still need integration/testing. The existing preview's own reorder gesture is
not demonstrated in the current film. iOS is tracked separately: r9 compiled
and passed programmatic photo checks, but real gestures and audio remain
unverified and are not included as proven Android functionality.

Telegram-derived source: GPL v2 or later; see LICENSE and upstream notices.
The two translation exports come from Telegram's Android localization resources.
