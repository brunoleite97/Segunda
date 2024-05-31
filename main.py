from func.Chat import chat
from func.SpeakOnline import Speak
from func.Listen import Listen
from func.DataOnline import Online_Scraper

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