from assist.func.Chat import chat
from assist.func.SpeakOnline import Speak
from assist.func.Listen import Listen
from assist.func.DataOnline import Online_Scraper

if __name__=="__main__":
    while 1:
        Q=Listen()
        QL=Q.lower()
        GetChat=chat(QL)
        GetData=Online_Scraper(Q)
        if GetData != None:
            Speak(GetData)
        else:
            Speak(GetChat[0])