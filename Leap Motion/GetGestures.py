import os, sys, inspect, time, Leap ,requests, threading, WeatherRetriever, json, TwitterFeed, TimeRetriever
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))


arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

def CheckFist(hands, past_hands):
    for i in range(len(hands)):
        try:
            if hands[i].grab_strength > 0.8 and past_hands[i].grab_strength < 0.5:
                return True
        except IndexError:
            return False


def CheckOpen(hands, past_hands):
    for i in range(len(hands)):
        try:
            if hands[i].grab_strength < 0.5 and past_hands[i].grab_strength > 0.8:
                return True
        except IndexError:
            return False

def CheckPinch(hands, past_hands):
    for i in range(len(hands)):
        try:
            if hands[i].pinch_strength - past_hands[i].pinch_strength > 0.2:
                return True
        except IndexError:
            return False


def CheckWaveRight(hands, past_hands):
    for i in range(len(hands)):
        try:
            if hands[i].palm_velocity[0] > 400:
                return True
        except IndexError:
            return False

def CheckWaveLeft(hands, past_hands):
    for i in range(len(hands)):
        try:
            if hands[i].palm_velocity[0] < -400:
                return True
        except IndexError:
            return False

def CheckWaveUp(hands, past_hands):
    for i in range(len(hands)):
        try:
            if hands[i].palm_velocity[1] > 400:
                return True
        except IndexError:
            return False

def CheckWaveDown(hands, past_hands):
    for i in range(len(hands)):
        try:
            if hands[i].palm_velocity[1] < -400:
                return True
        except IndexError:
            return False


def main():
    count = 0

    controller = Leap.Controller()
    # Keep this process running until Enter is pressed
    while True:
        frame = controller.frame()
        past_frame = controller.frame(3)

        hands = frame.hands
        past_hands = past_frame.hands

        if CheckOpen(hands, past_hands):
            print "Open"
            time.sleep(0.3)

        elif CheckFist(hands, past_hands):
            print "Fist"
            requests.get(url='http://d1099c9b.ngrok.io/dangerText')
            time.sleep(0.3)

        elif CheckWaveRight(hands, past_hands):
            print "Wave Right"
            TimeRetriever.TimeRetriever(count)
            count+=1
            time.sleep(0.3)

        elif CheckWaveLeft(hands, past_hands):
            print "Wave Left"
            requests.get(url= 'http://d1099c9b.ngrok.io/waveOut')
            time.sleep(0.3)

        elif CheckWaveUp(hands, past_hands):
            print "Wave Up"
            TwitterFeed.TwitterFeed(count)
            count += 1
            time.sleep(0.3)

        elif CheckWaveDown(hands, past_hands):
            print "Wave Down"
            WeatherRetriever.Weather(count)
            count+=1
            time.sleep(0.3)

        elif CheckPinch(hands, past_hands):
            time.sleep(0.3)
            frame = controller.frame()
            past_frame = controller.frame(3)

            hands = frame.hands
            past_hands = past_frame.hands
            print "Pinched", hands[0].pinch_strength
            url = "http://d1099c9b.ngrok.io/giveme"
            payload = {"PinchVal": hands[0].pinch_strength}
            headers = {'content-type' : 'application/json'}
            requests.post(url= url, data= json.dumps(payload), headers= headers)
            time.sleep(0.3)



if __name__ == "__main__":
    main()
