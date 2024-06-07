import wikipedia
import re

def tell_me_about(*args, **kwargs):
    entities = kwargs.get("entities", [])
    if len(entities) == 0:
        topic = kwargs.get("query")
    else:
        topic = entities[0][0]

    try:
        wikipedia.set_lang("pt")
        page = wikipedia.page(topic)
        return page.content[:500]
    except Exception as e:
        print(e)
        return "Ocorreu um erro ao buscar a página da Wikipédia"

if __name__ == '__main__':

    query = input("Digite sua consulta: ")

    print("Entidades encontradas:", [])
    print(tell_me_about(query=query))
