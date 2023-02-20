from gtts import gTTS

text_to_say = "Boa noite! Tudo bem? "

language = "pt"

gtts_object = gTTS(text = text_to_say,
                  lang = language,
                  slow = False)

gtts_object.save("./gtts.wav")

from IPython.display import Audio

Audio("./gtts.wav")