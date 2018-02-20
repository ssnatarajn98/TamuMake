def TimeRetriever(count):
    from datetime import datetime
    from gtts import gTTS
    import playsound, os

    tts = gTTS("The current time is: " + datetime.now().strftime('%H:%M:%S'))

    try:
        tts.save("Time" + str(count) + ".mp3")
    except:
        pass

    try:
        playsound.playsound("Time" + str(count) + ".mp3")
    except:
        pass

    os.remove("Time" + str(count) + ".mp3")



