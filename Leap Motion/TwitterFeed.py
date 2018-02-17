def TwitterFeed(count):

    import tweepy as tp
    from gtts import gTTS
    import playsound
    import os

    consumer_key = "EqgbbGiU0DqxEawMOFIYXG9SQ"

    consumer_secret = "9TWLaawIUJ8NGiXbTRcf6ablz6EDECbDatzag0ld5WnBg2W7Rj"

    access_token = "957345473576275968-ugTVpRBp4vSgAJj9nJTrYVS2S6E6UlV"

    access_token_secret = "3vQQasBocZAMaqdrtzmlWCQfMh62N2T9E3a2zmz4PF7Qu"

    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tp.API(auth)

    timeline = api.home_timeline()

    def remove_non_ascii(text):
        return ''.join(i if ord(i)<128 else ' ' for i in text)

    count = 0
    full_message = ""

    for tweet in timeline:
        count+=1
        full_message += str(tweet.user.name) + " has tweeted: " + str(remove_non_ascii(tweet.text)) + ". "
        if count >= 1:
            break

    tts = gTTS(text=full_message, lang="en")

    try:
        tts.save("tweets" + str(count) + ".mp3")
    except:
        pass

    try:
        playsound.playsound("tweets" + str(count) + ".mp3", True)
    except:
        pass

    os.remove("tweets" + str(count) + ".mp3")
