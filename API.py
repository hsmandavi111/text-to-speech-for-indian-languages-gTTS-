!pip install gTTS
from gtts import gTTS
import IPython.display as ipd

text = "வணக்கம், கோல்ப்க்கு வரவேற்கிறோம். நான் ஒரு TTS மாடல், இன்று நான் உங்களுக்கு எப்படி உதவ முடியும்?"
tts = gTTS(text, lang='kn')
tts.save("hello_hi.mp3")
ipd.Audio("hello_hi.mp3")

Similarly, you can use other languages codes like 
'bn' for Bengali,
'gu' for Gujarati, 
'ta' for Tamil,
'te' for Telugu,
'mr' for Marathi,
'kn' for Kannada, 
'ml' for Malayalam, 
'pa' for Punjabi and 
'or' for Odia.
