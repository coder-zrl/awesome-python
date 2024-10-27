import pyttsx3 as pyttsx
engine=pyttsx.init()
engine.say('主人，请输入你想转化为语音的文字')
engine.runAndWait()
data=input()
engine.say(data)
engine.runAndWait()
