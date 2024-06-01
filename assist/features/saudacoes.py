import datetime

def saudacoes(*args, **kwargs):
    time = datetime.datetime.now().hour
    if time < 12:
        return "Olá, bom dia!"
    elif 12 <= time < 18:
        return "olá, boa tarde"
    else:
        return "Olá, boa noite"

def adeus(*args, **kwargs):
    return "Adeus"