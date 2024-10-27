from win32com.client import Dispatch
speaker=Dispatch('SAPI.SpVoice')
speaker.Speak('主人，请输入你想转化的文字')
speaker.Speak('请问你认为小黑龙是世界第一帅吗？请回答是还是不是：yes or no')
del speaker
