def Weather(count):
    import gtts, weather, playsound, os
    weather = weather.Weather()


    location = weather.lookup_by_location("College Station")

    forecast_high = int(location.forecast()[0].high()) * 9/5 + 32
    forecast_low = int(location.forecast()[0].low()) * 9/5 + 32

    condition = location.condition().text()

    message = "The high for today is " + str(forecast_high) + " Fahrenheit, and the low is " + str(forecast_low) +" Fahrenheit. The condition should be " + condition

    tts = gtts.gTTS(text=message, lang="en")
    try:
        tts.save("Weather" + str(count) + ".mp3")
    except:
        pass

    try:
        playsound.playsound("Weather" + str(count) + ".mp3", True)
    except:
        pass

    os.remove("Weather" + str(count) + ".mp3")




