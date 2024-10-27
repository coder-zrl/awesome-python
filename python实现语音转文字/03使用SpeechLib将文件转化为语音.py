#存在问题
from comtypes.client import CreateObject
engine=CreateObject("SAPI.SpVoice")
stream=CreateObject('SAPI.SpFileStream')
from comtypes.gen import SpeechLib
infile='语音.txt'
outfile='语音.wav'
stream.Open(outfile,SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream=stream
f=open(infile,'r',encoding='utf-8')
theText=f.read()
f.close()
engine.speak(theText)
stream.close()