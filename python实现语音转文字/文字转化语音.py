from win32com.client import Dispatch
from comtypes.client import CreateObject
from comtypes.gen import SpeechLib
speaker=Dispatch('SAPI.SpVoice')
speaker.Speak('主人，请输入你想转化的文字')
data=input('请输入：')
speaker.Speak('问题来了，请问你认为小黑龙是世界第一帅吗？请回答是还是不是：please say yes or no')
a=input('请回答：')
if a=='是':
    speaker.Speak('你输入的是：张瑞龙是宇宙，诶呀，不对，')
    speaker.Speak('哦，哈哈，其实是')
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
else:
    speaker.Speak('答案错误，程序终止。再见，goodbye')
del speaker
