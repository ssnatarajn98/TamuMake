import os, sys, inspect, time, Leap
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
class GestureListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"


    def on_frame(self, controller):
        print "Frame available"


    def on_disconnect(self, controller):
        print "Disconnected"


def main():

    controller = Leap.Controller()
    # Keep this process running until Enter is pressed
    while True:
        frame = controller.frame()
        hands = frame.hands
        fingers = frame.fingers


        for hand in hands:
            print hand.grab_strength
        time.sleep(0.2)


if __name__ == "__main__":
    main()
