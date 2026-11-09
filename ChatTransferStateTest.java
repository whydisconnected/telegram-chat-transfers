import org.telegram.ui.Components.ChatTransferState;
import java.util.Arrays;
import java.util.List;

public final class ChatTransferStateTest {
    static void check(boolean b, String message) { if (!b) throw new AssertionError(message); }
    public static void main(String[] args) {
        ChatTransferState s = new ChatTransferState();
        check(s.enqueue(1) && s.enqueue(2), "Queue accepts different tracks");
        check(s.current == 0 && s.playing, "Enqueue must preserve current playback");
        check(!s.enqueue(1) && !s.enqueue(0), "No duplicate or current-song insertion");
        s.playNext(); check(s.current == 1 && s.next.equals(Arrays.asList(2)), "FIFO consumption");
        s.select(0); s.select(1); s.select(2); s.stageSelection(0);
        check(s.attachments.equals(Arrays.asList(0, 1, 2)) && s.selected.isEmpty(), "Gallery order survives drop");
        s.move(0, 2); check(s.attachments.equals(Arrays.asList(1, 2, 0)), "Reordering follows selected photo");
        s.remove(2); check(s.attachments.equals(Arrays.asList(1, 0)), "Remove retains other photos");
        s.select(0); s.select(3); s.stageSelection(3);
        check(s.attachments.equals(Arrays.asList(1, 0, 3)), "Adding more doesn't duplicate staged photos");
        s.move(-1, 1); s.move(2, 5); check(s.attachments.equals(Arrays.asList(1, 0, 3)), "Invalid moves do nothing");
        List<Integer> album = s.takeAlbum();
        check(album.equals(Arrays.asList(1, 0, 3)) && s.attachments.isEmpty(), "Send takes ordered snapshot and clears tray");
        s.stageSelection(4); check(album.equals(Arrays.asList(1, 0, 3)), "New draft cannot mutate sent album");
        System.out.println("ChatTransferState: 11 checks passed");
    }
}
