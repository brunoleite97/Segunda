import datetime

def data_hora(*args, **kwargs):
    query = kwargs['query']
    if 'time' in query:
        return datetime.datetime.now().strftime("%H:%M:%S")
    elif 'date' in query:
        return datetime.datetime.now().strftime("%d/%m/$Y")
    else:
        return "Desculpe, eu não consigo entender."

print(data_hora(query="time"))