from win32com.client import Dispatch
from comtypes.client import CreateObject
from comtypes.gen import SpeechLib
speaker=Dispatch('SAPI.SpVoice')
speaker.Speak('主人，请输入你想转化的文字')
data=input('请输入：')

#speaker.Speak(data)
engine=CreateObject("SAPI.SpVoice")
stream=CreateObject('SAPI.SpFileStream')
with open('语音.txt', 'w', encoding='utf-8') as fp:
    fp.write('你输入的是：'+data)
infile='语音.txt'
outfile='语音.wav'
stream.Open(outfile,SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream=stream
f=open(infile,'r',encoding='utf-8')
theText=f.read()
f.close()
engine.speak(theText)
stream.close()
speaker.Speak('您输入的语音已保存！beybey')
for i in range(20):
    speaker.Speak('帅帅龙是宇宙第一帅')
del speaker
