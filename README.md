# Chat Transfers — Telegram Android concepts

Photo drafts that preserve the chat, and a music queue controlled from the chat.
Native Telegram UI on Android; the films use real interaction captures. This
package contains both feature code and its isolated, signed-out demo host.

[Photo draft demo](photos.mp4) · [Music queue demo](player.mp4)

Both movies use a stationary, original Pixel 10 Pro frame and a minimal dark
background. Hardware artwork credit and media provenance are in CREDITS.md.

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

## Verification and limits

The original v29 checkout built and ran on the owned Android emulator. Native
selection, cancellation, incremental adding, tray reordering, local album
creation, playback/queue/seek were captured and inspected. Exported v30 movies
reuse those captures with stationary Pixel framing. A 60 fps export is not a
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
