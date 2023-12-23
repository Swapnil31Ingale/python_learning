import pyttsx3

def speak_names(name_list):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Iterate through the names and speak each one
    for name in name_list:
        engine.say(name)
        engine.runAndWait()

if __name__ == "__main__":
    names = ["Uday", "Majanu", "Jethalal", "Bhide", "Popatlal"]
    speak_names(names)
